import inspect


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

class JarritoAdentro(Jar):
    def __init__(self,pedito):
        super().__init__()
        self.pedito = pedito


    def __str__(self):
        return f"{self.capacity_init} {self.pedito}"
    

#INHERITANCE OF CLASSES:
ped = JarritoAdentro(pedito="pfff")
print(ped)


#LISTAR METODOS DE UNA CLASE/OBJETO
for i in range(len(dir(Jar))):
    print(dir(Jar)[i])
print("------------------------------------------------------")
j = Jar()
metodos = inspect.getmembers(j, inspect.ismethod)
for metodo in metodos:
    print(metodo)
