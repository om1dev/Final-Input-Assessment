stream1 = [101, 102, "None", "A", 103, "Om", 104]
stream2 = [102, 104, "105", None, 106, "107"]

# Merge streams and ensure uniqueness
merged_stream = set(stream1 + stream2)

print("-----------------------------------------------------------------------------------------------------------------")
print(f"The Merged Stream is: {merged_stream}")
print("-----------------------------------------------------------------------------------------------------------------")

# Initialize structures
cleaned_set = set()
error_log = []

# Process data
for item in merged_stream:
    try:
        value = int(item)   # Try converting to integer
        cleaned_set.add(value)
    except:
        error_log.append(item)  # Log invalid data

# Output results
print(f"The Cleaned Set is: {cleaned_set}")
print(f"The Error Log is: {error_log}")
print("-----------------------------------------------------------------------------------------------------------------")