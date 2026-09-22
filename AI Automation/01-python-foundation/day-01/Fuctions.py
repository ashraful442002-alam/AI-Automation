# function = reusable block of code

def greet_customer():
    print("Hello , customer!")


greet_customer()



# function with parameter
 
def greet(name):
    print(f"Hello {name}!")

greet("mu")



def introduce(name, country):
    print(f"My name is {name}.")
    print(f"I am from {country}.")
introduce("Ashraful", "Bangladesh")



def total(price, quantity):
    total = price * quantity
    print(total)
total(500,100)



# Return 

def add(a,b):
    return a+b
result = add(10,20)
print(result)


# Funtion + Loop

def welcome(name):
    print(f"Hello {name}!")

customer = ["Rahim", "Karin", "Hasan"]

for customers in customer:
    welcome(customers) 



### Function + Loop + Condition

def qualify_lead(budget):

    if budget >= 1000:
        return "HIGH-VALUE"

    elif budget >= 500:
        return "MID-VALUE"

    else:
        return "LOW-VALUE"


budgets = [500, 7000, 300, 120]

for budget in budgets:
    result = qualify_lead(budget)
    print(f"Budget: {budget} → {result}")