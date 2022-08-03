# ============================================================================================
"""calculation_to_units = 24
name_of_units = "hours"

def days_of_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    elif num_of_days == 0:
        return "You enetered 0 please enter valid positive number"


def validate_and_execute():
    if user_input.isdigit():
        user_input_value = int(user_input)
        calculated_value = days_of_units(user_input_value)
        print(calculated_value)
    else:
        print("Your input is not a valid number. Dont ruin my program!")

user_input = input("Hello User Kindly insert number to get units of it\n")
validate_and_execute()"""
# ===========================================================================================
"""calculation_to_units = 24
name_of_units = "hours"

def days_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        user_input_value = int(user_input)
        if user_input_value > 0:
            calculated_value = days_of_units(user_input_value)
            print(calculated_value)
        elif user_input_value == 0:
            print("You enetered 0 please enter valid positive number")
        else:
            print("Kindly insert a valid positive number")
    except ValueError:
        print("Your input is not a valid number. Dont ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hello User Kindly insert number to get units of it\n")
    validate_and_execute()"""
# ===========================================================================================
"""calculation_to_units = 24
name_of_units = "hours"

def days_of_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        user_input_value = int(num_of_elements)
        if user_input_value > 0:
            calculated_value = days_of_units(user_input_value)
            print(calculated_value)
        elif user_input_value == 0:
            print("You enetered 0 please enter valid positive number")
        else:
            print("Kindly insert a valid positive number")
    except ValueError:
        print("Your input is not a valid number. Dont ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hello User Kindly insert number to get units of it\n")
    for num_of_elements in set(user_input.split(", ")):
        validate_and_execute()"""
# =========================================================================================

