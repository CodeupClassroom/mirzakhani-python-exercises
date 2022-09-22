def iterate(n):
    return n + 1

def is_vowel(somestring):
    if type(somestring) == str:
        if len(somestring) == 1 and somestring.isalpha():
            return somestring.lower() in list('aeiou')
        else:
            return False
    else:
        return False
    
def calculate_tip(bill, tip_percent = 0.2):
    return bill * tip_percent

def get_letter_grade(somegrade):
    if somegrade >= 90:
        return 'A'
    elif somegrade >= 80:
        return 'B'
    elif somegrade >= 70:
        return 'C'
    elif somegrade >= 60:
        return 'D'
    else:
        return 'F'