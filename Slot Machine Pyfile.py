import random

bank = 1000
backout = True
debt = 0

while backout:
    print(f"Your current bank acount is {bank}")
    spins = int(input("How many spins do you want? "))
    bet = int(input("How much do you want to bet per spin? "))

    if bet * spins > bank:
        print(f"You can't afford that! Your bank is {bank}.")
        loan = input("Do you wish to take a loan? (yes/no) ")
        if loan.lower() == "yes":
            debtAdd = int(input("How much do you wish to withdraw? "))
            debt = debt + debtAdd
            bank = bank + debtAdd
            print(f"You've withdrawed {debtAdd}. Your debt is {debt}")
        else:
            continue

    bank -= bet * spins
    totalWinnings = 0

    for i in range(spins):
        slot1 = random.randint(1, 7)
        slot2 = random.randint(1, 7)
        slot3 = random.randint(1, 7)
        slots = (slot1, slot2, slot3)
        print(slot1, slot2, slot3)
        
        if slots == (7, 7, 7):
            print("Jackpot!!!")
            totalWinnings += bet * 777
        elif slots == (3, 3, 3):
            print("Lucky Threes!!!")
            totalWinnings += bet * 30
        elif slots == (4, 4, 4):
            print("Misfortune 4!!!")
            totalWinnings += bet * 10
        elif slots == (5, 5, 5):
            print("High Fives!!!")
            totalWinnings += bet * 5
        elif slots == (3, 3, 3):
            print("Cool Twos!!!")
            totalWinnings += bet * 2
        elif slots == (6, 6, 6):
            print("Devilish!!!")
            totalWinnings += bet * 25
        elif slots == (1, 1, 1):
            print("Pity!")
            totalWinnings += bet * 2
            
    totalWinningsTemp = totalWinnings
    payment = min(totalWinnings, debt)
    debt -= payment
    totalWinnings -= payment
    bank += totalWinnings
    print(f"You won {totalWinningsTemp} and your bank is now {bank}.")

    if debt > 0:
        print(f"Also you're in debt by {debt}... You better get the money back before the end of the month...")

    answer = input("Do you want to back out now? (yes/no) ").lower()
    backout = (answer != "yes")

print(f"You left with a bank of {bank}. Thanks for playing!")
