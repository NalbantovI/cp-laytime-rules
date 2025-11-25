#!/usr/bin/env python3
"""
Remove WORLDFOOD Rule 1 which contains corrupted extraction with mixed line numbers.
This rule was already identified as corrupted during vessel gear breakdown cleanup.
"""

import re

def cleanup_worldfood(content):
    """Remove corrupted WORLDFOOD Rule 1 and renumber Rule 2."""
    
    print("=" * 100)
    print("WORLDFOOD CORRUPTED RULE REMOVAL")
    print("=" * 100)
    print()
    
    # Remove WORLDFOOD Rule 1 (entire corrupted rule)
    pattern_remove = r'### WORLDFOOD - Rule 1\n\n```\n.*?```\n\n'
    content = re.sub(pattern_remove, '', content, flags=re.DOTALL)
    print("✓ Removed WORLDFOOD Rule 1 (corrupted extraction with mixed line numbers)")
    
    # Renumber Rule 2 to Rule 1
    content = re.sub(r'### WORLDFOOD - Rule 2', '### WORLDFOOD - Rule 1', content)
    print("✓ Renumbered WORLDFOOD Rule 2 → Rule 1")
    
    # Update rule count from 2 to 1
    content = re.sub(r'(## WORLDFOOD\n\n\*\*Laytime rules:\*\*) 2', r'\1 1', content)
    print("✓ Updated WORLDFOOD rule count: 2 → 1")
    
    return content

def main():
    filepath = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Store original stats
    original_lines = content.count('\n')
    original_rules = content.count('### ')
    
    # Remove corrupted WORLDFOOD Rule 1
    content = cleanup_worldfood(content)
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Calculate new stats
    new_lines = content.count('\n')
    new_rules = content.count('### ')
    lines_removed = original_lines - new_lines
    rules_removed = original_rules - new_rules
    
    print()
    print("=" * 100)
    print(f"Lines removed: {lines_removed}")
    print(f"Rules: {original_rules} → {new_rules} (-{rules_removed})")
    print(f"Total lines: {original_lines} → {new_lines}")
    print("=" * 100)
    print()
    print("Why removed:")
    print("  → WORLDFOOD Rule 1 contained severely corrupted extraction")
    print("  → Mixed line numbers (252-307) indicating extraction error")
    print("  → Interleaved text from different charter sections")
    print("  → No coherent laytime calculation logic")
    print("  → Previously identified as corrupted during vessel gear cleanup")
    print()
    print("✅ CLEANUP COMPLETE!")
    print()

if __name__ == '__main__':
    main()
