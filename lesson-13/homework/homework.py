#1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import datetime

def age_calculator(birthday):
    today=datetime.today()
    birthday=datetime.strptime(birthday, "%Y-%m-%d")

    years=today.year-birthday.year
    months=today.month-birthday.month
    days=today.day-birthday.day 

    if days<0:
        months-=1
        prev_month=(today.month-1) if today.month>1 else 12
        prev_year=(today.year-1) if today.year>1 else today.year-1
        days +=(datetime(prev_year,prev_month,1)- datetime(prev_year,prev_month-1,1)).days

    if months<1:
        years-=1 
        months+=12 
    return years,months,days

birthday=input('Enter birthday(YYYY-MM-DD):')
years,months,days=age_calculator(birthday) 

print(f'Siz {years} yosh, {months} oylik, {days} kun.')

#2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
from datetime import datetime
def days_until_next_birthday(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    days_remaining = (next_birthday - today).days
    return days_remaining

birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
days_remaining = days_until_next_birthday(birthdate)

print(f"Keyingi tugilgan kuningizgacha {days_remaining} kun qoldi.")
#3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
from datetime import datetime, timedelta

def calculate_meeting_end(current_datetime, hours, minutes):
    meeting_start = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M")
    duration = timedelta(hours=hours, minutes=minutes)
    meeting_end = meeting_start + duration
    return meeting_end

current_datetime = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Enter meeting duration (hours): "))
minutes = int(input("Enter meeting duration (minutes): "))

meeting_end = calculate_meeting_end(current_datetime, hours, minutes)
print(f"Meeting: {meeting_end.strftime('%Y-%m-%d %H:%M')} da tugaydi!")

#4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
import pytz

def convert_timezone(date_time,from_tz,to_tz):
    from_tz=pytz.timezone(from_tz)
    to_tz=pytz.timezone(to_tz)

    local_time=datetime.strptime(date_time, "%Y-%m-%d %H:%M") 
    local_time=from_tz.localize(local_time)

    converted_time=local_time.astimezone(to_tz)

    return converted_time

date_time=input("Enter the date and time (YYYY-MM-DD HH:MM):")
from_tz=input("Enter your current timezone (e.g., 'America/New_York'):")
to_tz=input("Enter the target timezone (e.g., 'Asia/Tokyo'):")

converted_time = convert_timezone(date_time, from_tz, to_tz)

print(f"The converted date and time in {to_tz} is: {converted_time.strftime('%Y-%m-%d %H:%M %Z')}")


#6. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
import re

def validate_email():
    email = input("Enter an email address: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    validate_email() 