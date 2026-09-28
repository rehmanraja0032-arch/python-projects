"""Bill Splitter
Splits a restaurant bill (including tip) equally between friends.
"""


def calculate_split(appetizers, main_courses, desserts, drinks, tip_percent, num_of_friends):
    """Return subtotal, tip, total and the amount each person pays."""
    subtotal = appetizers + main_courses + desserts + drinks
    tip = subtotal * tip_percent / 100
    total = subtotal + tip
    per_person = total / num_of_friends
    return subtotal, tip, total, per_person


print("=== Bill Splitter ===")

appetizers = float(input("Appetizers: "))
main_courses = float(input("Main courses: "))
desserts = float(input("Desserts: "))
drinks = float(input("Drinks: "))
tip_percent = float(input("Tip % (e.g. 25): "))
num_of_friends = int(input("Number of friends: "))

amounts = [appetizers, main_courses, desserts, drinks, tip_percent]

if num_of_friends < 1:
    print("Error: there must be at least 1 person.")
elif min(amounts) < 0:
    print("Error: amounts and tip cannot be negative.")
else:
    subtotal, tip, total, per_person = calculate_split(
        appetizers, main_courses, desserts, drinks, tip_percent, num_of_friends
    )

    print("\n--- Receipt ---")
    print(f"Subtotal:          ${subtotal:,.2f}")
    print(f"Tip ({tip_percent:g}%):".ljust(19) + f"${tip:,.2f}")
    print(f"Total:             ${total:,.2f}")
    print(f"Friends:           {num_of_friends}")
    print(f"Each person pays:  ${per_person:,.2f}")