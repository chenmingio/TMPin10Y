class Employee(object):

    def __init__(instance, firstname, lastname, pay):  # it received the instance as first argument automatically
        instance.first = firstname
        instance.last = lastname
        instance.pay = pay

    def fullname(instance):
        return f"{instance.first} {instance.last}"

    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount


class Developer(Employee):
    pass


emp_1 = Developer('ming', 'chen', 1000000)
emp_2 = Developer('bao', 'ye', 999999)

print(emp_1.pay)
print(emp_2.pay)

print(Employee.__dict__)
print(Developer.__dict__)
