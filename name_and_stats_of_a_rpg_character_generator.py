"""RPG Character Creator
Builds a character with Strength, Intelligence and Charisma stats.
Each stat must be a whole number between 1 and 10.
"""

full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 10 or intelligence > 10 or charisma > 10:
        return "All stats should be no more than 10"
    return f"{name}\nSTR {full_dot*strength}{empty_dot*(10-strength)}\nINT {full_dot*intelligence}{empty_dot*(10-intelligence)}\nCHA {full_dot*charisma}{empty_dot*(10-charisma)}"


print('=== RPG Character Creator ===')
name = input('Character name (no spaces, max 10 letters): ').strip()
strength = int(input('Strength (1-10): '))
intelligence = int(input('Intelligence (1-10): '))
charisma = int(input('Charisma (1-10): '))

result = create_character(name, strength, intelligence, charisma)
print('')
print(result)

input('\nPress Enter to close...')