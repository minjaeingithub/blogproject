from faker import Faker

myfake = Faker()

Faker.seed(1)

print(myfake.name()) 
print(myfake.address())
#print(myfake.text()) 
#print(myfake.state())
#print(myfake.sentence())
print(myfake.random_number())

views.py DB for 
blog = Blog()
