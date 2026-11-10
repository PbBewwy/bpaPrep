# Name: Adam Gavel
# Date: 11/9/2026
# Program Name: Program Help Screen
# Description: Gradebook version 1.0 help (-h) command output, written only in print.

# Title
print("=" * 44)
print("  GRADEBOOK  version 1.0\n  A tool for tracking class scores")
print("=" * 44)

# Usage
print("USAGE:")
print("  gradebook [option] [file]")

# Options
print()
print("Options:")
print("  -a    Add a new score")
print("  -l    List all scores")
print("  -r    Print a report")
print("  -h    Show this help screen")

# Examples
print()
print("EXAMPLES:")
print("  gradebook -l C:\\BPA\\scores.txt\n  gradebook -a \"Quiz 3\"")

# Footer
print("-" * 44)
print("Tip: options are case sensitive.")
print("-A is not the same as -a.")
print("=" * 44)

#print("Debug mode is on.")