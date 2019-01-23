year_of_birth=int(input("year_of_birth"))

def age_calc(yearofbirth):
   age=("2019-year_of_birth")

   if age < 18 :
    print("your are a minor and you are () years old")

   elif age < 35 :
    print("you are a youth and you are () years old")

   else :
    print("you are an elder and you are () years old")

print(age_calc)
