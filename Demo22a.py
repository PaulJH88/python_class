import random

booked_rooms = []

def room_availability():
    room = random.randint(1,100)
    while room in booked_rooms:
        room = random.randint(1,100)

    booked_rooms.append(room)
    return room

def get_price(room):
    return room*10