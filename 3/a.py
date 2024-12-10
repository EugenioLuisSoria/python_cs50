import re
patron = r"[\x20-\x2F]\s*"

date_by_user = input("Insert your date: ").lower().capitalize().strip()

date_by_user = re.split(patron, date_by_user)

print(date_by_user)