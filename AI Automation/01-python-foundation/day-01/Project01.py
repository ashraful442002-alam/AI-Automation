# Lead Qualification System v1

name = input("Customer name:\n")

email = input("Email: \n")

company = input("Company name: \n")

budget = int(input("Monthly budget: \n"))

if budget >= 1000:
    lead_type = "HIGH-VALUE"
    action = "Contact sales immediately"
elif budget >=500:
    lead_type = "MID-VALUE"
    action = "Follow-up sequence"

else:
    lead_type = "LOW-VALUE"
    action = "Marketing list"



print ("=====================")
print ("Lead Qualification")
print("======================")


print("Name: " , name)
print("Email: ", email)
print("Company: ", company)
print("Budget: ", budget)

print ("Classification: ",lead_type)


print("Action:\n",action)
