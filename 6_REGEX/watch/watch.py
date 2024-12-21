import re
import os
os.system("clear")


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"^<(.*| )(?P<http>https?://).*(?:youtube\.com/)(?:embed/)(?P<embed>[a-zA-z0-9_-]+)(?:.*)"
    if match := re.search(pattern, s, re.IGNORECASE):
        embed = match.group("embed")
        return f"https://youtu.be/{embed}"


...


if __name__ == "__main__":
    main()