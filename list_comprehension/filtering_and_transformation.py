"""
List Comprehension Practice
Topic: Filtering and Transformation
Focus: Safe data handling and type validation

This file demonstrates how to safely filter and transform data
while handling None values and validating data types properly.
"""

# ----------------------------------------
# Numbers: Filtering and Transformation
# ----------------------------------------

numbers = [0, 1, 2, None, 3, "", 4]
# Using isinstance to ensure only valid integers are processed
newnumbers = [2 * x for x in numbers if isinstance(x, int)]

print(newnumbers)



# ----------------------------------------
# Name Cleaning: Filtering and Transformation
# ----------------------------------------

names = [" Ali ", None, "  Sara", "", "Omar  "]
# Ensuring values are strings and not empty after stripping spaces
newnames = [x.strip().lower() for x in names if isinstance(x, str) and x.strip()]
 
print(newnames) 


# ----------------------------------------
# Edge Case: Safe Numeric Conversion
# ----------------------------------------

values = ["90", "85.5", "N/A", "", None, 100]

cleaned_values = []

for value in values:
    try:
        cleaned_values.append(float(value))
    except (TypeError, ValueError):
        continue

print(cleaned_values)




