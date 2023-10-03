#
def test_config():
    return True


def get_factorial(n):
    sum = 1

    for val in range(2, n + 1):
        sum *= val
    return sum

def sum_odd_numbers(num): 
    sum = 0
    while num > 0:
        if(num%2==1):
            sum = sum + num
        num = num - 1
    return sum


def display_menu():
    print("1) Factorial")
    print("2) Sum odd numbers")
    print("3) Exit")

def run_menu():
    display_menu()
    option = input("Choose what you would like to do(1, 2, or 3): ")
    handle_menu_option(option)

def handle_menu_option(option):
    if(option == "1"):
        selected_option_1
    elif (option == "2"):
        selected_option_2
    elif (option == "3"):
        selected_option_3
    else:
        print("Invalid input")

def selected_option_1():
    num = int(input("Choose a number you want to factorial: "))
    if num < 1 or num > 10:
        while num < 1 or num > 10:
            print("invalid")
    elif num > 0 and num < 11:
        get_factorial
    else:
        get_factorial

def selected_option_2():
    sum = int(input("Choose a number between 1 and 100: "))
    if sum < 1 or sum >= 100:
        while sum < 1 or sum > 100:
            print("invalid")
    elif sum > 0 and sum <= 100:
        sum_odd_numbers
    else:
        sum_odd_numbers

def selected_option_3():
    print("User selected to exit. Do you want to continue? Y/N ")
    option = 'Y' or 'N' 
    if option == 'Y':
        return handle_menu_option
    elif option == 'N':
        print("exit")
