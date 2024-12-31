import os 
#os.system("clear")
import re
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
patron_total = r"[\"\x20-\x2F]\s*"
flag_comillitas = False
flag_listo = False

while True:
    user_date = input("Insert date: ")
    #user_date = user_date.replace(" ", "")
    if user_date[0] == user_date[-1] and user_date[0] == '"':
        flag_comillitas = True
        user_date = user_date.replace('"','').strip()
    date_by_user = re.split(patron_total, user_date)

    if len(date_by_user) > 3:
        continue
    try:
        month, day, year = date_by_user
    except:
        continue


    if month.isalpha():
        try:
            day = int(day)
            year = int(year)

            for i in range(len(months)):
                if (months[i] == month) and (day > 0 and day <= 31) and (year >= 0):
                    month_number = i + 1
                    if user_date.find("/") > -1:
                        break
                    elif user_date.find(",") == len(month) or user_date.find(",") == len(month) + 1 :
                        continue
                    elif user_date.find(",") == -1:
                        continue
                    print(f"{year}-{month_number:02d}-{day:02d}")
                    flag_listo = True
                    break

        except:
            continue
        if flag_listo:
            break
        continue

    try:
        day = int(day)
        month = int(month)
        year = int(year)

        if (month > 0 and month < 13) and (day > 0 and day < 32) and (year >= 0):
            if flag_comillitas == True:
                print(f'"{year}-{month:02d}-{day:02d}"\n', end=" ")
            else:
                print(f"{year}-{month:02d}-{day:02d}", end="")
            break
        elif (month < 0 or month >= 13) or (day < 0 or day > 31) or (year < 0):
            continue
    except:
        continue


