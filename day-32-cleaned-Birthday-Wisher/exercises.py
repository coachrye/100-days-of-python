# import smtplib
#
# my_email = YourEmail
# password = YourPassword
#
# # connection = smtplib.SMTP("smtp.gmail.com")
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ryan.salvanera@mailnxt.com",
#         msg="Subject:Hello\n\nThis is the body of my email.")
#
# # connection.close()
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
#
# date_of_birth = dt.datetime(year=1977, month=9, day=18)
# print(date_of_birth)
import datetime
import datetime as dt
import random
import smtplib

weekday = dt.datetime.now().weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
        # This also works
        # quotes = [line.strip() for line in quote_file]
        quotes = quote_file.readlines()
        quote_of_the_week = random.choice(quotes)

    print(quote_of_the_week)

    my_email = "ryan.salvanera@gmail.com"
    password = "B@dB0y34"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ryan.salvanera@mailnxt.com",
            msg=f"Subject:Quote of the Week\n\n{quote_of_the_week}")
