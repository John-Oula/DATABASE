from peewee import *
from os import path
njia = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(njia,"users.db"))

class Student(Model):
    name = CharField()
    email = CharField()
    password = CharField()
    class Meta:
        database = db

class Employee(Model):
    name = CharField()
    salary = IntegerField()
    password = CharField()
    class Meta:
        database = db

Student.create_table(fail_silently=True)
Employee.create_table(fail_silently=True)
Student.create(name="King",
                     email = "king@gmail.com",
                     password = "King12345")
Student.create(name="John",
                     email = "john@gmail.com",
                     password = "john12345")
Student.create(name="Njagi",
                     email = "njagi@gmail.com",
                     password = "Njagi12345")

user1 =Student.get(id=1)
print(user1.name,user1.email,user1.password)
user1 =Student.get(id=2)
print(user1.name,user1.email,user1.password)

Employee.create(name="Job",
                     salary = 10000,
                     password = "job12345")
Employee.create(name="Calvin",
                     salary = 12000,
                     password = "calvin12345")
Employee.create(name="Nigel",
                     salary = 20000,
                     password = "nigel12345")
user1 =Employee.get(id=1)
print(user1.name,user1.salary,user1.password)
user1 =Employee.get(id=2)
print(user1.name,user1.salary,user1.password)
user1 =Employee.get(id=3)
print(user1.name,user1.salary,user1.password)



