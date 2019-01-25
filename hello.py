year_of_birth=int(input("year_of_birth"))

def age_calc(yearofbirth):
   age=(2019-year_of_birth)

   if age < 18 :
       print("your are a minor")

   elif age < 35 :
       print("you are a youth")

   else :
       print("you are an elder")

age_calc(year_of_birth)
