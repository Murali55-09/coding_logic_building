# Take a character and check if it is a letter, a digit, or neither.

ch = '34'

if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print(f"Letter is", ch)

elif '0' <= ch <= '9':
    print(f"Digit is", ch)

# Learning: All comparisons are numeric.
# Characters are compared using ASCII/Unicode values.
# C allows implicit conversion, Python does not.

# ASCII comparison is fast, predictable, and interview-preferred
# Built-ins handle Unicode, not ideal for systems/DSA
# Letters & digits occupy fixed ASCII ranges
# Unicode characters will fail ASCII-based checks