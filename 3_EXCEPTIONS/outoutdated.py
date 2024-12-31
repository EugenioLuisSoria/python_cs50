# Initiate the list
month_li = [
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

# Start infinite loop that breaks when a valid date is entered
while True:
    # Prompt the user for a date (format: 9/8/1636 or september 8, 1636)
    input_date = input("Date (in month/day/year order): ").strip()

    # Attempt to transform date into yyyy-mm-dd format
    try:
        # Split month, day and year by "/" separator and convert to integer
        month, day, year = map(int, input_date.split("/"))

        # Check whether month and day fall within expected ranges
        if 1 <= month <= 12 and 1 <= day <= 31:
            # If so, then print year, month, and date
            print(year,f"{month:02}",f"{day:02}", sep = "-")

            # Break out of the loop
            break

        else:
            # Check if date string starts not with a number but a letter
            if not input_date[0].isdigit():
                # Split the date by space
                month, day, year = input_date.split(" ")

                # A comma (,) will remain, so need to get rid of that
                day = day.replace(',', '')

                # Convert day and year to integers; will deal with month after
                day = int(day)
                year = int(year)

                # Capitalize month for case insensitivity
                month = month.capitalize()

                # Need to check if the month exists in the list
                if month in month_li and (1 <= day <= 31):
                    print(year,f"{month_li.index(month) + 1:02}", f"{day:02}", sep = "-")
                    break

    except:
        pass