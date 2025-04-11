#No parameter, no return
def meeting():
    print("\nThe meeting starts at 9:00 am.")

meeting()

#with parameter, no return
def meeting2(time, organiser):
    print("\nThe meeting starts at ",time)
    print("The meeting will be conducted by: ",organiser)

meeting2("10:00 am", "John")
meeting2("12:00pm", "Mariya")
meeting()

#no parameter, with return
def meeting3():
    return "\nThe meeting starts at 11:00am.\nIt will be conducted by Cynthia."

print(meeting3())
res = meeting3()
print(res)

#with parameter and with return
def meeting4(time, organiser):
    str1 = "\nThe meeting starts at "+time
    str2 = ".\nIt will be conducted by "+organiser+"."
    str3 = str1+str2
    return str3

print(meeting4("9:00am", "Peter"))

#with parameter, no return
def meeting2(time, organiser = "Rachel"):
    print("\nThe meeting starts at ",time)
    print("The meeting will be conducted by: ",organiser)

meeting2(organiser= "John", time="10:00am")
meeting2("12:00pm", "Mariya")
meeting2("10:30am")
meeting()
Trial10.py

def external(list1):
    sum = 0
    for x in list1:
        sum += x
    
    print("Sum: ", sum)

    def average():
        avg = sum/len(list1)
        print("Average of the ",list1," is: ",avg)

    average()

l1 = [1,6,4,8,2,9,4,7,3,2]
external(l1)
trial11.py

num = 100

def mul():
    global num
    num = 10
    print("Mul:",num*50)

mul()
print("Multiplication:",num*50)