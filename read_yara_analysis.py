#!/usr/bin/env python3
"""
Script to read and analyze Yara spot CP Analysis.xlsx
"""

import pandas as pd
import sys

def read_excel_file(filename):
    """Read all sheets from Excel file"""
    try:
        # Read all sheets
        excel_file = pd.ExcelFile(filename)
        print(f"=== EXCEL FILE STRUCTURE ===")
        print(f"File: {filename}")
        print(f"Number of sheets: {len(excel_file.sheet_names)}")
        print(f"Sheet names: {excel_file.sheet_names}\n")
        
        # Read each sheet
        for sheet_name in excel_file.sheet_names:
            print(f"\n{'='*80}")
            print(f"SHEET: {sheet_name}")
            print(f"{'='*80}\n")
            
            df = pd.read_excel(filename, sheet_name=sheet_name)
            
            print(f"Shape: {df.shape} (rows: {df.shape[0]}, columns: {df.shape[1]})")
            print(f"\nColumn names:")
            for i, col in enumerate(df.columns, 1):
                print(f"  {i}. {col}")
            
            print(f"\n--- First 10 rows of data ---\n")
            print(df.head(10).to_string())
            
            print(f"\n--- Sample of non-null data ---")
            # Show sample rows with actual content
            non_empty = df.dropna(how='all')
            if len(non_empty) > 0:
                print(f"\nNon-empty rows: {len(non_empty)}")
                print(non_empty.head(15).to_string())
            
    except Exception as e:
        print(f"Error reading file: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    import os
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "Yara spot CP Analysis.xlsx")
    read_excel_file(filename)
