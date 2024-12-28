import pytest, sys


class Jar:

    def __init__(self, capacity_init=int(12), cookies_in_jar=0, cookie_emoji="🍪"):
        if capacity_init < 0:
            raise ValueError()
        self.capacity_init = capacity_init
        self.cookies_in_jar = cookies_in_jar
        self.cookie_emoji = cookie_emoji

    def __str__(self):
        return f"{self.cookie_emoji * self.cookies_in_jar}"

    def deposit(self, n):
        if (self.cookies_in_jar + n) > self.capacity_init:
            raise ValueError
        else:
            self.cookies_in_jar += n

    def withdraw(self, n):
        if (self.cookies_in_jar - n) < 0:
            raise ValueError
        else:
            self.cookies_in_jar -= n

    @property
    def capacity(self):
        return self.capacity_init

    @property
    def size(self):
        return self.cookies_in_jar


