# String concatenation (1-2)
print("\n1-2. STRING CONCATENATION")
space = " "
string_1 = "Thirty" + space + "Days" + space + "Of" + space + "Python"
string_2 = "Coding" + space + "For" + space + "All"
print(string_1)
print(string_2)

# Company variable (3-5)
print("\n3-5. COMPANY VARIABLE")
company = "Coding For All"
print(f"Word: {company}")
print(f"Length of the word company: {len(company)}")

# Case conversion (6-7)
print("\n6-7. CASE CONVERSION")
upper_method = "uppercase"
lower_method = "LOWERCASE"
print(upper_method.upper())
print(lower_method.lower())

# Formatting methods (8)
print("\n8. FORMATTING METHODS")
print(f"Capitalize(): {company.capitalize()}")
print(f"Title(): {company.title()}")
print(f"Swapcase(): {company.swapcase()}")

# Slice the first word (9)
print("\n9. SLICE THE FIRST WORD")
print(f"Slicing the first word: {company[4:]}")

# Check for Coding (10)
print("\n10. CHECK FOR \"CODING\"")
print(f"Contains \"Coding\"? {"Coding" in company}")
print(f"Finding \"Coding\": {company.find("Coding")}")
print(f"Using the index: {company.index("Coding")}") #both index and find behave the same except if index doesn't find the character(s) then it returns error but find gives out -1

# Replacing words (11-12.)
print("\n11-12. REPLACING WORDS")
pfe = "Python for Everyone"
print(f"Original: {company}")
print(f"Replaced: {company.replace("Coding", "Python")}")
print(f"Original: {pfe}")
print(f"Replaced: {pfe.replace("Everyone", "All")}")

# Split strings (13-14)
print("\n13-14. SPLIT STRINGS")
print(f"Split \"Coding For All\": {company.split()}")
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f"Split tech companies: {company.split(", ")}")

# Index access (15-17)
print("\n15-17. INDEX ACCESS")
print(f"Exercise 15: {company[0]}")
print(f"Exercise 16: {company[-1]}")
print(f"Exercise 17: {company[10]}")

# Create acronym (18-19)
print("\n18-19. CREATE ACRONYM")
def create_acronym(phrase):
    words = phrase.split()
    acronym = "".join(word[0].upper() for word in words)
    return acronym

pfe_acronym = create_acronym("Python for Everyone")
print(f"Acronym for \"Python for Everyone\": {pfe_acronym}")

cfa_acronym = create_acronym("Coding for All")
print(f"Acronym for \"Coding for All\": {cfa_acronym}")

# Find first occurence (20-22)
print("\n20-22. FIRST OCCURENCE")
cfap = "Coding For All People"
print(f"Original: {company}")
print(f"Position of C: {company.index("C")}")
print(f"Position of F: {company.index("F")}")
print(f"Original: {cfap}")
print(f"Position of last I: {cfap.rfind("I")}")

# Because sentence (23-27.)
