import smtplib
import random
import pandas
import datetime as dt

my_email="YOUR EMAIL"
password="YOUR PASSWORD"

df=pandas.read_csv("birthdays.csv")
birthday_info={row["name"]:{"email": row.email, "month":row.month, "day": row.day} for (index, row) in df.iterrows()}

now = dt.datetime.now()
for (bday_name, bday_dates) in birthday_info.items():
    if bday_dates["month"]==now.month and bday_dates["day"]==now.day and now.hour==0 and now.minute==0 and now.second==0:
        file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as birthday_letter:
            msg=birthday_letter.read()
            birthday_msg=msg.replace("[Name]", bday_name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=bday_dates["email"],
                                msg=f"subject:Happy Birthday! \n\n{birthday_msg}")

