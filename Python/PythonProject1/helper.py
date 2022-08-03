
def days_of_units(num_of_days, conversion_units):
    if conversion_units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        print("unsupported unit")


def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_value = int(days_and_units_dictionary["days"])
        if user_input_value > 0:
            calculated_value = days_of_units(user_input_value, days_and_units_dictionary["units"])
            print(calculated_value)
        elif user_input_value == 0:
            print("You enetered 0 please enter valid positive number")
        else:
            print("Kindly insert a valid positive number")
    except ValueError:
        print("Your input is not a valid number. Dont ruin my program!")