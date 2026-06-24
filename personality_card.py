"""
Code to AI — Week 1 Project
Personality Card

"""

# Asking user for input
name = input("Enter your name: ")
city = input("Enter your  city: ")
age = int(input("Enter your age: "))
superpower = input("Enter your superpower: ")
luckynum = int(input("Enter your lucky number:  "))
ques = int(input("Enter a number greater than  99999: "))

# Header
print("➖" * 35)
print(f"           ⭐ My Personality Card ⭐")
print("➖" * 35)

# Calculating  statistics
print(f"🪪 Name            :  {name}")
print(f"🏙️ City            :  {city}")
print(f"🔞 Age             :  {age} ({age * 12} Months!)")
print(f"🦸 Superpower?     :  {superpower}")
print(f"🔮 Age in 2050     :  {2050 - 2026 + age}")
print(f"🍀 Lucky Num * 7   :  {luckynum * 7} ")
print(f"⁉️'a' in the name? :  {'a' in name}")
print(f"⁉️ over 18?        :  {age > 18}")
print(f"Are you smart?      :  {ques:,}")

# Ending code with message
print("➖" * 35)
print("\nMade with Python 🐍 -- Code to AI")
