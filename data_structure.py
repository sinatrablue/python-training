import collections
import string
from dataclasses import dataclass

my_d = {
    "robot": "Bender",
    "crab": "Zoidberg",
    "seasons": 10
}

print(my_d)

my_d["seasons"] = 11

print(my_d)

ord_d = collections.OrderedDict(one=11, two="Bender", three="Zoidberg");

print(ord_d)

ord_d["one"] = "Fry"

print(ord_d)

###### CLASS ######
class Team:
    def __init__(self, member1, member2, totalEffective) -> None:
        self.member1 = member1
        self.member2 = member2
        self.totalEffective = totalEffective

    def __repr__(self) -> str:
        rep = "#################### #################### ####################\n"
        rep += "Members are : " + self.member1 + " & " + self.member2 + '\n'
        rep += "There are " + str(self.totalEffective) + " members in total"
        return rep

equip1 = Team("Fry", "Bender", 2)
equip2 = Team("Leela", "Zoidberg", 3)

print(equip1)
print(equip2)

# Now same stuff but with some nice help
@dataclass
class Equip:
    mb1: str
    mb2: str
    totEff: int

e1 = Equip("Fry", "Bender", 2)
e2 = Equip("Leela", "Zoidberg", 3)

print(e1)
print(e2)

e1.mb2 = "Flexo"
e1.totEff = 1234145

print(e1)

# Named tuple
mmb = collections.namedtuple("Eqp", "Pilot Shooter Total")("Leela", "Fry", 5)
print(mmb)
