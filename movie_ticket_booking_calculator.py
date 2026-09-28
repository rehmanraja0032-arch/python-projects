"""Movie Ticket Booking System
Checks eligibility, applies charges and discounts, and prints a ticket receipt.
"""


def get_service_charge(seat_type):
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    return service_charges


def get_discount(is_member, age):
    discount = 0
    if is_member and age >= 21:
        discount = 3
    return discount


base_price = 15

print('=== Movie Ticket Booking ===')
age = int(input('Age: '))
seat_type = input('Seat type (Premium / Gold / Standard): ').strip().title()
show_time = input('Show time (Morning / Afternoon / Evening): ').strip().title()
member_answer = input('Are you a member? (y/n): ').strip().lower()
weekend_answer = input('Is it a weekend? (y/n): ').strip().lower()

is_member = False
if member_answer == 'y':
    is_member = True

is_weekend = False
if weekend_answer == 'y':
    is_weekend = True

print('')
if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

discount = get_discount(is_member, age)
if discount > 0:
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend:
    extra_charges = 2

if age > 17 and (age >= 21 or show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = get_service_charge(seat_type)
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount

    print('')
    print('------------------------------')
    print('          YOUR TICKET')
    print('------------------------------')
    print(f'Show:            {show_time}')
    print(f'Seat:            {seat_type}')
    print(f'Base price:      ${base_price}')
    print(f'Extra charges:   ${extra_charges}')
    print(f'Service charges: ${service_charges}')
    print(f'Discount:       -${discount}')
    print('------------------------------')
    print(f'Final price:     ${final_price}')
    print('------------------------------')
else:
    print('Ticket booking failed due to restrictions')
    if age <= 17:
        print('Reason: you must be 18 or older.')
    else:
        print('Reason: Evening shows are only for age 21+ or members.')

input('\nPress Enter to close...')