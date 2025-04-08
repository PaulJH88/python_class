ages = [2, 5, 13, 66]
museum_card = [True, False]
ticket_price = 0

for card in museum_card:
    for age in ages:
        if card == False:
            if (age < 3):
                ticket_price = 0
            elif (age >= 3 and age < 12):
                ticket_price = 7
            elif (age >= 12 and age < 65):
                ticket_price = 10
            else:
                ticket_price = 6.75
        elif card == True:
            if (age < 3):
                ticket_price = 0
            elif (age >= 3 and age < 12):
                ticket_price = 5
            elif (age >= 12 and age < 65):
                ticket_price = 7
            else:
                ticket_price = 5

        print("Age is", age, "Card is", card, "Cost is", ticket_price)


