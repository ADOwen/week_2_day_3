# to get the square footage of a house

def square_feet(length, width):
    area = length * width
    return area

# get the circumference


def get_circumference(radius):
    circumference = 3.14 * radius**2
    return circumference

# get a one up on your adversaries


def scouter(power_level):
    if int(power_level) > 9000:
        print("Ugh!!! it's over 9,000!")
    else:
        print("Hmph, cannon fodder")

# who is finkle?


def is_finkle(name):
    if name.title() == 'Einhorn':
        print("Finkle IS Einhorn!")
    else:
        print(f"Finke is definitely not {name}, back to the drawing board")
