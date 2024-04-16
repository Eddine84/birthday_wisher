##################### Hard Starting Project ######################
import smtplib 
import datetime as dt
import pandas as pd
import random
MY_EMAIL = "dzfullstackdev@gmail.com"
MY_PASSWORD = "acmx gozv lvmo hpkb"



now = dt.datetime.now()

month = now.month
day = now.day
today = (month,day)

try:
    data_csv = pd.read_csv("./birthdays.csv")
    data_frame = pd.DataFrame(data_csv)
    dict_df = data_frame.to_dict(orient='records')

except:
     print("file not found")

else:
    for person in dict_df:
        if day == person["day"] and month == person["month"]:
            try:
                random_letter = random.randint(1,4)
                with open(f"./letter_templates/letter_{random_letter}.txt") as data:
                        letter = data.read()
                        letter_to_send = letter.replace("[NAME]", person["name"])
            except FileNotFoundError:
                print(FileNotFoundError)
            else: 
                with smtplib.SMTP("smtp.gmail.com",587) as connection:
                        connection.starttls()
                        connection.login(MY_EMAIL,MY_PASSWORD)
                        connection.sendmail(from_addr=MY_EMAIL,to_addrs=person["email"],msg=f"Subject:person\n\n {letter_to_send}")



# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



