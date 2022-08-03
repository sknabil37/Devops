import datetime

user_input = input("Enter your Goal with deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear User! Time remaining for your goal: {goal} is {hours_till} hours")
