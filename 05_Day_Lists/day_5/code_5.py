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
print("\n8. NUMBER OF COMPANIES")
print(f"Number of companies: {len(it_companies)}")

# First, middle, last company (9)
print("\n9. FIRST, MIDDLE, LAST COMPANY")
first_company = it_companies[0]
middle_position = len(it_companies) // 2
middle_company = it_companies[middle_position]
last_company = it_companies[-1]
print(f"First company: {first_company}")
print(f"Middle company: {middle_company}")
print(f"Last company: {last_company}")

# Modify a company (10)
print("\n10. MODIFY A COMPANY")
it_companies_copy = it_companies.copy()
it_companies_copy[2] = "Alphabet"
print(f"Original: {it_companies}")
print(f"Modified: {it_companies_copy}")

# Add a company (11)
print("\n11. ADD A COMPANY")
it_companies.append("Netflix")
print(f"New list: {it_companies}")

# Insert in middle (12)
print("\n12. INSERT IN MIDDLE")
new_middle = len(it_companies) // 2
it_companies.insert(new_middle, "Tesla")
print(f"After inserting: {it_companies}")

# Change to uppercase (13)
print("\n13. CHANGE TO UPPERCASE")
it_companies[0] = it_companies[0].upper()
print(f"Uppercase list: {it_companies}")

# Join with hashtag (14)
print("\n14. JOIN WITH HASHTAG")
joined_companies = "#; ".join(it_companies)
print(f"Joined companies: {joined_companies}")

# Check if company exists (15)
print("\n15. CHECK IF COMPANY EXISTS")
company_to_check = "Google"
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list")
else:
    print(f"{company_to_check} does not exist in the list")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(f"\nReset list for remaining exercises: {it_companies}")

# Sort the list (16)
print("\n16. SORT THE LIST")
it_companies.sort()
print(f"Sorted list: {it_companies}")

# Reverse the list (17)
print("\n17. REVERSE THE LIST")
it_companies.reverse()
print(f"Reversed list: {it_companies}")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(f"\nReset list: {it_companies}")

# Slice first 3 companies (18)
print("\n18. SLICE FIRST 3 COMPANIES")
it_first = it_companies[0:3]
print(f"First three companies: {it_first}")

# Slice last 3 companies (19)
print("\n19. SLICE LAST 3 COMPANIES")
it_last = it_companies[-3:]
print(f"Last three companies: {it_last}")

# Slice middle company/companies (20)
print("\n20. SLICE MIDDLE COMPANY/COMPANIES")

# Remove first company (21)
print("\n21. REMOVE FIRST COMPANY")

# Remove middle company (22)
print("\n22. REMOVE MIDDLE COMPANY")

# Remove last company (23)
print("\n23. REMOVE LAST COMPANY")

# Remove all companies (24)
print("\n24. REMOVE ALL COMPANIES")

# Join lists (26)
print("\n26. JOIN LISTS")

# Create full_stack with insertions (27)
print("\n27. CREATE FULL_STACK WITH INSERTIONS")
