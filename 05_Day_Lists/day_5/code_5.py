# Declare an empty list (1)
print("\n1. DECLARE AN EMPTY LIST")
empty_list = list()
print(f"Empty list: {empty_list}")
print(f"Empty list type: {type(empty_list)}")

# List with more than 5 items (2)
print("\n2. LIST WITH MORE THAN 5 ITEMS")
alien_stage = ["Mizi", "Sua", "Ivan", "Till", "Luka", "Hyuna"]
print(f"Alien stage characters: {alien_stage}")

# Find length (3)
print("\n3. FIND LENGTH")
print(f"Length of the list: {len(alien_stage)}")

# Get first, middle, last item (4)
print("\n4. GET FIRST, MIDDLE, LAST ITEM")
first_item = alien_stage[0]
middle_index = len(alien_stage) // 2
middle_item = alien_stage[middle_index]
last_item = alien_stage[-1]
print(f"List: {alien_stage}")
print(f"First item: {first_item}")
print(f"Middle item: {middle_item}")
print(f"Last item: {last_item}")

# Mixed data types list (5)
print("\n5. MIXED DATA TYPES")
mixed_list = ["Tibah Hussain", 20, 1.64, "single", "Vor der Grieb 1A"]
print(f"Mixed data types list: {mixed_list}")

# IT companies list (6-7)
print("\n6-7. IT COMPANIES LIST")
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(f"IT companies: {it_companies}")

# Number of companies (8)
print(f"\n8. NUMBER OF COMPANIES")
print(f"Number of companies: {len(it_companies)}")

# First, middle, last company (9)
print(f"\n9. FIRST, MIDDLE, LAST COMPANY")
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f"First company: {first_company}")
print(f"Middle company: {middle_company}")
print(f"Last company: {last_company}")
