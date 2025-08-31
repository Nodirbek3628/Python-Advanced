from collections import namedtuple

Person = namedtuple("Person",["name","eamil","password"])


person = Person(name="ali",eamil="ali@gmail.com", password="ali124")


a = person.name
b = person.eamil

print(a)
print(b)
