import re
import sys

def main():
    return print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
              r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    main()