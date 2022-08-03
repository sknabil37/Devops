from helper import validate_and_execute

user_input = ""
while user_input != "exit":
    user_input = input("Hello User Kindly insert number & conversion unit!\n")
    days_and_units = user_input.split(":")
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    validate_and_execute(days_and_units_dictionary)
