# Challenge 1: The Data Profiler (Easy) 
# Goal: Master basic data manipulation and string formatting. 
# ● Topics: Variables, Data Types, Strings, Lists. 
# ● Task: Create a script that takes a list of "raw" sensor readings (strings with extra 
# whitespace and mixed casing) and converts them into a clean, numerical list. 
# ● Objective: 1. Create a list of strings: [" 23.5 ", "low", " 45.0", "HIGH ", "30.2"]. 
# 2. Use a loop to strip whitespace and convert all strings to lowercase. 
# 3. Identify which values are numbers and store them in a new list as floats.



list1 = [" 23.5 ", "low", " 45.0", "HIGH ", "30.2"]

# Step 1: Strip whitespace and convert to lowercase
cleaned_list = []
for item in list1:
    cleaned_list.append(item.strip().lower())
print("Cleaned List (Strip whitespace and converted to lowercase list is ):\n", cleaned_list)

# Step 2: Identify which values are numbers and store them in a new list as floats.
numeric_values = []
for item in cleaned_list:
    if item.replace('.', '', 1).isdigit():  
        numeric_values.append(float(item)) 
print("Numeric Values (Identified numeric values as floats list is ):\n", numeric_values)

