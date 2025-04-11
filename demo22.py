import math, demo22a

guests_no = int(input("Please enter no. of guests: "))
nights = int(input("Please enter no. of nights: "))

rooms = []
total = 0

for room in range(math.ceil(guests_no/2)):
    room = demo22a.room_availability()
    rooms.append(room)
    total += demo22a.get_price(room) * nights

print("Rooms: ",rooms)
print("Total fare: $", total)