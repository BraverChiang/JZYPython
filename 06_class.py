# 29 class and object. 30 init. 31 class and instance variable.
# 32 Inheritance. 33 Multiple Inheritance.
# 34 thread.

class Enemy:
    life = 3

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

    def be_attacked(self):
        print("ouch!")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life))


enemy1 = Enemy(88)
enemy3 = enemy1
enemy2 = Enemy(12)

enemy1.be_attacked()
enemy1.check_life() # 剩下2条命

enemy2.check_life() # 剩下3条命, 这个Object是全新的
enemy3.check_life() # 剩下2条命, 这个Object就是enemy1.
enemy3.get_energy()


# 30 init.
class Tuna:

    def __init__(self):
        print("booobooobooo")

    def swim(self):
        print("I'm swimming")

flipper = Tuna()
flipper.swim()

# 31 class and instance variable.
class Girl:
    gender = "female"      # class variable

    def __init__(self, name):
        self.name = name   # instance variable


r = Girl("Rackel")
s = Girl("Stanky")

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

# 32 Inheritance.
class Parent():
    def print_last_name(self):
        print("Jiang")

class Child(Parent):

    def print_first_name(self):
        print("Brave")

    # overriding
    def print_last_name(self):
        print("Chiang")



chil = Child()
chil.print_last_name()

# 33 Multiple Inheritance.
class Mario():
    def move(self):
        print("I am moving")

class Shroom():
    def eat_shromm(self):
        print("Now I am big!")


class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.eat_shromm()

# 34 thread.

import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = Messenger(name="Send out messages")
y = Messenger(name="Receive messages")
x.start() # run()
y.start() # run()