
def check_birth_year():
    try:
        age = input("How old are you? ")
        age_num = int(age)

        if age_num < 0:
               raise Exception("Your age must be greater than 0")
        
        birth_year = 2025 - age_num
        print("You were born in the year", birth_year)
        complete = True    


    except ValueError as te:
                print("Please enter a numerical value: ", te)
                check_birth_year()

check_birth_year()