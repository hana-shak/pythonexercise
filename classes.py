class User:
    # constructor self = this used all time in class
   def __init__(self, name, email, age):
       self.name = name
       self.email = email
       self.age = age

   def greeting(self):
       return f'My name is {self.name} & I am {self.age}'
   def has_birthday(self):
       self.age += 1

# Extends classes
# class Customer extends User => in php or javascript
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} & I am {self.age} & my balance is {self.balance} JD'

brad = User('lolo','lolo@gmail.com',37)

janet = Customer('jojo','jojo@test.com',16)
janet.set_balance(500)
print(janet.greeting())

# print(brad.name)
brad.has_birthday()
# print(brad.greeting())