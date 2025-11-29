# ATM WITHDRAWAL MACHINE

balance = 5000
pin = 2007
attempt = 0
phone = "+919471417287"   

while True:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("PIN verified")
        print("Your balance is:", balance)

        amt = int(input("Enter amount to withdraw: "))

        if amt <= balance:
            balance = balance - amt
            print("Amount withdrawn:", amt)
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance")

        break

    else:
        attempt += 1
        print("Wrong PIN!")

        if attempt == 3:
            print("\nATM Card Blocked!")
            print("SMS sent to your number:", phone)
            print("Reason: 3 incorrect PIN attempts")
            break
