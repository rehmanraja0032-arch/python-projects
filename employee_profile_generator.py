"""Employee ID Card Generator
Takes employee details, builds a unique employee code and prints an ID card.
Every answer is checked right after it is typed. If it is wrong, the program stops.
Practices: input(), functions, conditionals, string methods, slicing, f-strings.
"""


def create_employee_code(first_name, last_name, department, joining_year, employee_number):
    """Build a code like DEV-2026-JD-001."""
    initials = first_name[0] + last_name[0]
    return f"{department}-{joining_year}-{initials}-{employee_number:03d}"


def get_level(experience_years):
    """Return the experience level based on years of experience."""
    if experience_years < 2:
        return "Junior"
    elif experience_years < 5:
        return "Mid-level"
    else:
        return "Senior"


print ("=== Employee ID Card Generator ===")

first_name = input("First name: ").strip()
if not first_name.replace(" ", "").isalpha():
    print("Error: name must contain letters only.")
    exit()
first_name = first_name.title()

last_name = input("Last name: ").strip()
if not last_name.replace(" ", "").isalpha():
    print("Error: name must contain letters only.")
    exit()
last_name = last_name.title()

age_text = input("Age (18-65): ").strip()
if not age_text.isdigit():
    print("Error: age must be a whole number.")
    exit()
age = int(age_text)
if age < 18 or age > 65:
    print("Error: age must be between 18 and 65.")
    exit()

position = input("Position: ").strip()
if not position.replace(" ", "").isalpha():
    print("Error: position must contain letters only.")
    exit()
position = position.title()

salary_text = input("Monthly salary ($): ").strip()
if not salary_text.replace(".", "", 1).isdigit():
    print("Error: salary must be a positive number.")
    exit()
salary = float(salary_text)
if salary <= 0:
    print("Error: salary must be more than 0.")
    exit()

experience_text = input("Years of experience: ").strip()
if not experience_text.isdigit():
    print("Error: experience must be a whole number.")
    exit()
experience_years = int(experience_text)
if experience_years > age - 18:
    print(f"Error: experience cannot be more than {age - 18} years for age {age}.")
    exit()

department = input("Department code (3 letters, e.g. DEV): ").strip().upper()
if len(department) != 3 or not department.isalpha():
    print("Error: department code must be exactly 3 letters.")
    exit()

year_text = input("Joining year: ").strip()
if not year_text.isdigit():
    print("Error: year must be a whole number.")
    exit()
joining_year = int(year_text)
if joining_year < 1990 or joining_year > 2100:
    print("Error: joining year must be between 1990 and 2100.")
    exit()

number_text = input("Employee number (1-999): ").strip()
if not number_text.isdigit():
    print("Error: employee number must be a whole number.")
    exit()
employee_number = int(number_text)
if employee_number < 1 or employee_number > 999:
    print("Error: employee number must be between 1 and 999.")
    exit()

full_name = first_name + " " + last_name
code = create_employee_code(first_name, last_name, department, joining_year, employee_number)
level = get_level(experience_years)

print("\n" + "=" * 40)
print(f"{'EMPLOYEE ID CARD':^40}")
print("=" * 40)
print(f"Name:        {full_name}")
print(f"Age:         {age} years old")
print(f"Position:    {position} ({level})")
print(f"Experience:  {experience_years} years")
print(f"Salary:      ${salary:,.2f} / month")
print(f"Employee ID: {code}")
print("=" * 40)

# Slicing: decode the information back out of the employee code
print("\n--- Decoded from Employee ID ---")
print(f"Department:      {code[0:3]}")
print(f"Joining year:    {code[4:8]}")
print(f"Initials:        {code[9:11]}")
print(f"Employee number: {code[-3:]}")