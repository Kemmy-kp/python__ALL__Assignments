#Write python program that user to enter only odd numbers, else will raise an exception.

class EvenNumberError(Exception):
    pass

def get_odd_number():
    try:
        num = int(input("Please enter an odd number: "))
        if num % 2 == 0:
            raise EvenNumberError("You entered an even number!")
        else:
            print(f"You entered {num}, which is an odd number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except EvenNumberError as e:
        print(e)

get_odd_number()
