import re

string = "12345"

if parteStr := re.search(r"(?P<caca>23)", string):
    print(parteStr.group("caca"))