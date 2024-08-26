#დაწერეთ პროგრამა, რომელიც იღებს ორი ადამიანის ასაკს და განსაზღვრავს ვინ არის უფროსი

age1 = int(input("enter first person age "))
age2 = int(input("enter second person age "))

if age1 > age2:
    print("first person > second person")
elif age1 < age2:
    print("second person is chief")
else: 
    print("both person are same age")
