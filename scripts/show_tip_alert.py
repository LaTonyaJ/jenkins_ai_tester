#!/usr/bin/env python3
# scripts/show_tip_alert.py
"""
Standalone script to display the Engineering Tip of the Day alert window.
This script can be run independently to show the latest tip in a nice turtle graphics window.
"""

import sys
import os
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app.turtle_alert import show_tip_alert

def main():
    """Main function to display the tip alert."""
    print("🚀 Engineering Tip of the Day Alert")
    print("=" * 40)
    
    # Check if tip file exists
    tip_file = project_root / "artifacts" / "tip_of_day.txt"
    
    if not tip_file.exists():
        print(f"⚠️  Tip file not found: {tip_file}")
        print("💡 Generate a new tip first by running:")
        print("   python -m app.generate_tip")
        
        # Show alert with default message
        show_tip_alert("No tip available yet! Run 'python -m app.generate_tip' to generate a new engineering tip.")
    else:
        # Show the tip alert
        print(f"📖 Reading tip from: {tip_file}")
        show_tip_alert()
    
    print("✅ Alert window closed.")

if __name__ == "__main__":
    main()