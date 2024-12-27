import sys, re, inflect
from datetime import date 
p = inflect.engine()

class Born: 
    @classmethod
    def get(cls):
        birth = input("Birth date: ")
        datepattern = r"^(?P<year>[0-9]{4})\-(?P<month>(0?[1-9]|1[0-2]))\-(?P<day>(0?[1-9]|[1-2][0-9]|3[0-1]))$"
        if to_verify := re.search(datepattern, birth):
            year = int(to_verify.group("year"))
            month = int(to_verify.group("month"))
            day = int(to_verify.group("day"))
            try:
                birth = date(year,month,day)
                return birth
            except:
                sys.exit("Invalid date format")   
        else:
            sys.exit("Invalid date format")

class Today:
    @classmethod
    def get(cls):
        today = date.today()
        return today

def main():
    born = Born.get()
    today =Today.get()
    dif = today - born
    dif = dif.days
    total_minutes = dif * 1440
    words = p.number_to_words(total_minutes,andword="")
    print(f"{words.capitalize()} minutes")


if __name__ == "__main__":
    main()