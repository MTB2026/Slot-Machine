import random

bankAccount = 1000
backout = True
debt = 0

while backout:
    print(f"\nYour current bank account is £{bankAccount}")  
    spins = int(input("How many spins do you want? "))
    bet = int(input("How much do you want to bet per spin? "))

    if spins <= 0 or bet <= 0:
        print("Spins and bet amount must be greater than zero")
        continue

    if bet * spins > bankAccount:
        print(f"You can't afford that, your bank account is £{bankAccount}.")
        loan = input("Do you wish to take a loan? (yes/no) ")
        if loan.lower() == "yes":
            debtAdd = int(input("How much do you wish to withdraw? "))

            if debtAdd <= 0:
                print("Loan amount must be greater than zero")
                continue

            debt = debt + debtAdd
            bankAccount = bankAccount + debtAdd
            print(f"You've withdrawn {debtAdd}. Your debt is £{debt}")
        else:
            continue

    bankAccount -= bet * spins
    totalWinnings = 0

    for i in range(spins):
        slot1 = random.randint(1, 7)
        slot2 = random.randint(1, 7)
        slot3 = random.randint(1, 7)
        slots = (slot1, slot2, slot3)

        symbols = {1: "🍒", 2: "🍋", 3: "🍊", 4: "🔔", 5: "⭐", 6: "😈", 7: "💎"}
        print(f"  {symbols[slot1]}  {symbols[slot2]}  {symbols[slot3]}")

        if slots == (7, 7, 7):
            print("  💎 JACKPOT! 💎")
            totalWinnings += bet * 777
        elif slots == (6, 6, 6):
            print("  😈 Devilish! 😈")
            totalWinnings += bet * 25
        elif slots == (3, 3, 3):
            print("  🍊 Lucky Threes! 🍊")
            totalWinnings += bet * 30
        elif slots == (4, 4, 4):
            print("  🔔 Misfortune 4! 🔔")
            totalWinnings += bet * 10
        elif slots == (5, 5, 5):
            print("  ⭐ High Fives! ⭐")
            totalWinnings += bet * 5
        elif slots == (1, 1, 1):
            print("  🍒 Pity! 🍒")
            totalWinnings += bet * 2
        elif slots == (2, 2, 2):
            print("  🍋 Cool Twos! 🍋")
            totalWinnings += bet * 2
        elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            print("  Close! Two of a kind!")
            totalWinnings += bet

    totalWinningsTemp = totalWinnings
    payment = min(totalWinnings, debt)
    debt -= payment
    totalWinnings -= payment
    bankAccount += totalWinnings

    print(f"\nYou won £{totalWinningsTemp} and your bank account is now £{bankAccount}.")
    if debt > 0:
        print(f"You're in debt by £{debt}... You better get the money back before the end of the month...") 

    if bankAccount <= 0 and debt > 0:
        print("💸 You're broke AND in debt. Game over!")
        break

    answer = input("\nDo you want to back out now? (yes/no) ").lower()  
    backout = (answer != "yes")

print(f"\nYou left with a bank account of £{bankAccount}. Thanks for playing!")
