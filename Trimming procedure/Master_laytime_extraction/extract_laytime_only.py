#!/usr/bin/env python3
"""
Extract only laytime-affecting sentences/paragraphs from each rule.
If a laytime keyword appears in a paragraph, keep the whole paragraph.
"""

import re
from datetime import datetime

# Keywords that indicate laytime calculation impact
LAYTIME_PATTERNS = [
    r'\blaytime\b',
    r'\bdemurrage\b',
    r'\bdespatch\b',
    r'\btime\s+(?:lost|used|saved|occupied|taken|spent)',
    r'(?:time|period)\s+(?:shall|will|may|must|to)\s+(?:not\s+)?count',
    r'(?:not\s+)?count\s+as\s+(?:laytime|time)',
    r'time\s+(?:running|commence|commencing|suspended|cease|ceasing)',
    r'weather\s+working\s+day',
    r'working\s+(?:day|time|hours)',
    r'excepted\s+(?:period|time|day)',
    r'waiting\s+time',
    r'detention',
    r'allowed\s+(?:laytime|time)',
]

# Exclusion patterns - paragraphs that contain ONLY these topics should be excluded
# even if they contain time-related words in a different context
EXCLUSION_PATTERNS = [
    r'freight.+payable.+within',  # Freight payment terms
    r'notice.+delivered by hand',  # Notice delivery procedures
    r'transmitted by (fax|e-?mail)',  # Communication methods
    r'ISPS Code.*Security certificate',  # Security compliance (unless mentions time counting)
    r'Hague.+rules.*entitled to.*benefit',  # Hague Rules reference
    r'calibration scale.*tanks',  # Equipment specifications
    r'Plimsoll marks.*draft marks',  # Vessel markings
    r'International ship Security certificate',  # Certificate names without impact
]

# Configuration data patterns - these are settings that will be OCR'd separately
# Remove these entirely as they're input data, not calculation logic
CONFIGURATION_PATTERNS = [
    r'SUPERHOLIDAY',  # Superholiday lists
    r'holidays?.+(to be )?excluded.+laytime.+calculation.+(are )?(listed )?as follows',  # Holiday list headers
    r'^\s*•\s+\d+(st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December)',  # Holiday dates
    r'^\s*•\s+(Christmas|Easter|New Year|Good Friday)',  # Named holidays
    r'^\s*•\s+At\s+\w+.+(from|to)\s+\d+:\d+',  # Port-specific time exclusions
    r'THE OWNERS\s+THE CHARTERERS\s*$',  # Signature line
    r'Page \d+ of \d+\s*-?\s*$',  # Page markers
    r'Demurrage.+(shall be paid|payable).+at the rate of.+per day',  # Demurrage rate specifications
    r'Despatch.+(shall be paid|payable).+at.+(the rate|half)',  # Despatch rate specifications
    r'at the rate of.+per day.+pro rata',  # Generic rate specifications
]

def is_configuration_data(text):
    """Check if text is configuration data (settings) rather than operational rules."""
    # Check for configuration patterns
    for pattern in CONFIGURATION_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
            return True
    return False

def contains_laytime_reference(text):
    """Check if text contains laytime-related keywords and is not purely administrative."""
    text_lower = text.lower()
    
    # First check if this is configuration data that should be OCR'd separately
    if is_configuration_data(text):
        return False
    
    # Check if paragraph matches exclusion patterns (administrative/non-laytime content)
    for pattern in EXCLUSION_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            # Double check: if it ALSO has explicit laytime counting language, keep it
            explicit_laytime = (
                re.search(r'shall not count as laytime', text_lower) or
                re.search(r'not.+count.+as.+laytime', text_lower) or
                re.search(r'time.+count.+laytime', text_lower) or
                re.search(r'laytime.+not.+count', text_lower)
            )
            if not explicit_laytime:
                return False  # Exclude administrative content without laytime impact
    
    # Check for laytime keywords
    for pattern in LAYTIME_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    return False

def is_section_header(line):
    """Check if line is a section header (just a number and title, no detailed text)."""
    stripped = line.strip()
    # Match patterns like "21 Accessible Space/Grab Discharge" or "20. VESSEL GEAR CLAUSE"
    # These are typically short and don't contain detailed provisions
    if re.match(r'^\d+\.?\s+[A-Z][A-Za-z\s/&\-]+$', stripped) and len(stripped) < 80:
        return True
    return False

def split_into_paragraphs(text):
    """Split rule text into logical paragraphs by clause markers."""
    paragraphs = []
    current_para = []
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Skip empty lines but track them
        if not stripped:
            if current_para:
                current_para.append(line)
            continue
        
        # Skip section headers (they'll be filtered later)
        if is_section_header(stripped):
            if current_para:
                paragraphs.append('\n'.join(current_para))
                current_para = []
            # Add header as separate item so we can filter it
            paragraphs.append(line)
            continue
        
        # Check if this starts a new numbered/lettered clause
        # More strict patterns to better split clauses
        is_new_clause = bool(
            re.match(r'^\d+\.\d+\s', stripped) or  # 20.3
            re.match(r'^\([a-z]\)\s', stripped) or  # (a)
            re.match(r'^[a-z]\.?\s', stripped) or    # a) or a.
            re.match(r'^\([0-9]+\)\s', stripped) or # (1)
            re.match(r'^[A-Z]\.\s', stripped) or     # A.
            re.match(r'^\([A-Z]\)\s', stripped) or   # (A)
            re.match(r'^Rider Clause', stripped) or  # Rider Clause No: XX
            re.match(r'^Clause \d+', stripped) or    # Clause 16
            re.match(r'^CLAUSE \d+', stripped)       # CLAUSE 46
        )
        
        # Start new paragraph if we hit a clause marker
        if is_new_clause and current_para:
            paragraphs.append('\n'.join(current_para))
            current_para = []
        
        current_para.append(line)
    
    # Add final paragraph
    if current_para:
        paragraphs.append('\n'.join(current_para))
    
    return paragraphs

def extract_laytime_paragraphs(rule_text):
    """Extract only paragraphs that affect laytime from a rule."""
    paragraphs = split_into_paragraphs(rule_text)
    
    # Filter paragraphs that contain laytime references
    laytime_paras = []
    for para in paragraphs:
        # Skip section headers even if they accidentally match
        if is_section_header(para.strip()):
            continue
            
        if contains_laytime_reference(para):
            # Clean up the paragraph
            cleaned = para.strip()
            if cleaned:
                laytime_paras.append(cleaned)
    
    return laytime_paras

def process_master_file(input_file, output_file):
    """Process the MASTER file and extract only laytime provisions."""
    print("📖 Reading MASTER file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    output_lines = []
    rules_processed = 0
    rules_with_laytime = 0
    total_paras_extracted = 0
    
    # Create new header
    output_lines.append("# MASTER CP LAYTIME RULES - LAYTIME CALCULATION ONLY\n\n")
    output_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    output_lines.append("**Source:** MASTER_CP_LAYTIME_RULES.md\n")
    output_lines.append("**Processing:** Extracted only paragraphs affecting laytime calculation\n\n")
    output_lines.append("This document contains only the specific provisions from charter party clauses\n")
    output_lines.append("that directly affect laytime counting, suspension, or calculation.\n")
    output_lines.append("Full commercial context has been removed.\n\n")
    output_lines.append("---\n\n")
    
    # Parse by charter sections
    charter_pattern = r'\n## ([A-Z_\s]+)\n'
    charters = re.split(charter_pattern, content)
    
    # Process each charter (skip header - first element)
    i = 1
    while i < len(charters) - 1:
        charter_name = charters[i].strip()
        charter_content = charters[i + 1]
        
        # Extract all rules for this charter
        rule_pattern = r'### ' + re.escape(charter_name) + r' - Rule \d+\n\n```\n([\s\S]*?)\n```'
        rules = re.findall(rule_pattern, charter_content)
        
        charter_laytime_rules = []
        
        for rule_text in rules:
            rules_processed += 1
            
            # Extract laytime paragraphs
            laytime_paras = extract_laytime_paragraphs(rule_text)
            
            if laytime_paras:
                charter_laytime_rules.append(laytime_paras)
                rules_with_laytime += 1
                total_paras_extracted += len(laytime_paras)
        
        # Write charter section if it has laytime rules
        if charter_laytime_rules:
            output_lines.append(f"## {charter_name}\n\n")
            output_lines.append(f"**Laytime rules:** {len(charter_laytime_rules)}\n\n")
            
            for idx, paras in enumerate(charter_laytime_rules, 1):
                output_lines.append(f"### {charter_name} - Rule {idx}\n\n")
                output_lines.append("```\n")
                output_lines.append('\n\n'.join(paras))
                output_lines.append("\n```\n\n")
        
        i += 2
    
    # Write output
    print(f"✍️  Writing output file...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(output_lines))
    
    print(f"\n📊 Extraction complete:")
    print(f"   Total rules processed: {rules_processed}")
    print(f"   Rules with laytime provisions: {rules_with_laytime}")
    print(f"   Rules removed (no laytime impact): {rules_processed - rules_with_laytime}")
    print(f"   Total laytime paragraphs extracted: {total_paras_extracted}")
    print(f"\n✅ Output written to: {output_file}")
    
    # Show file size comparison
    import os
    orig_size = os.path.getsize(input_file)
    new_size = os.path.getsize(output_file)
    reduction = ((orig_size - new_size) / orig_size) * 100
    print(f"\n📦 File size:")
    print(f"   Original: {orig_size:,} bytes")
    print(f"   Extracted: {new_size:,} bytes")
    print(f"   Reduction: {reduction:.1f}%")

if __name__ == '__main__':
    input_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES.md'
    output_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    print("🔍 Extracting laytime-only provisions from MASTER file...\n")
    process_master_file(input_file, output_file)
