
# Input: A dictionary where keys are dates and values are prices. 
dict1 = {
    "10-03-2026": 100,
    "11-03-2026": 150,
    "12-03-2026": 200,
    "13-03-2026": 250,
    "14-03-2026": 300
}

# Calculate the average price using a for loop. 
x = 0
count = 0
for i in dict1:
    x += dict1[i]
    count += 1

avg = x/count
print(f"----------------------------------------------------")
print(f"The Average price is: {avg}")
print(f"----------------------------------------------------")

 
# Identify "Volatility Days"—any day where the price is 5% higher or lower than the average. 
print(f"----------------------------------------------------")
percentage = 0.05 * avg
print(f"The 5% of the total average is: {percentage}")
low_percentage = avg - (0.05 * avg)
print(f"The -5% value of the total average is: {low_percentage}")
high_percentage = avg + (0.05 * avg)
print(f"The +5% value of the total average is: {high_percentage}\n")

result = []
for i in dict1:
    if dict1[i] > high_percentage:
        print(f"{i} is a Volatility Day with price {dict1[i]} which is higher than the average.")
        result.append((i, "high volatility"))
    elif dict1[i] < low_percentage:
        print(f"{i} is a Volatility Day with price {dict1[i]} which is lower than the average.")
        result.append((i, "low volatility"))

print(f"\nThe Volatility Days are: {result}")
print(f"----------------------------------------------------")



