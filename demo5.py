num = 11

if num > 15:                         #simple if
    print("Good day!")

print("Busy")

if num%2 ==0:                       #if with else
    print(num," is even")
else:
    print(num, " is odd")

marks = 85                          #else if ladder

if marks >= 80:
    print("A grade")
elif marks >= 70:
    print("B grade")
elif marks>= 60:
    print("C grade")
elif marks >=50:
    print("D grade")
else:
    print("Fail!")

if num>=10:                         #nested If
    if marks >= 85:
        print(num, " is amaing!")
    else:
        print(num, "is not amazing")
else:
    print("Criteria failed!")

color = "Orange"
distance = "Far away"

if color == "Red":
    print("Stop...")
elif color == "Orange":
    if distance == "Nearby":
        print("Speed up")
    else:
        print("Wait")
else:
    print("Go ahead!")