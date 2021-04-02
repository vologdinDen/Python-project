from random import randint
import sqlite3

#Create database
database = open('card.s3db', 'a+')
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS card('
            'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
            'number TEXT, '
            'pin TEXT, '
            'balance INTEGER DEFAULT 0)')
conn.commit()


class Card:    
    # Create card and pin
    
    def create_card(self):
        print("Your card has been created")
        customer_account_number = "400000" + str(randint(100000000, 1000000000))

        for i in range(10):
            check_str = customer_account_number + str(i)
            if self.lugh(check_str):
                customer_account_number += str(i)
                break
        
        print(f"Your card number:{customer_account_number}")

        PIN = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        print(f"Your card PIN: {PIN}")
        
        # Add card to database
        cur.execute(f'INSERT INTO card (number, pin, balance) VALUES ({customer_account_number},{PIN},{0})')
        conn.commit()

    # Try to login
    def log_info(self, exitcheck):
        card_number = str(input("Enter your card number:"))
        # Check if there is a card with this number in the database
        try:
            card_pin_db = str(cur.execute(f'SELECT pin FROM card WHERE number = {card_number}').fetchone())
            card_pin = card_pin_db[2:6]
        except sqlite3.OperationalError:
            print("Wrong input")
            return exitcheck
        
        # Checking it out PIN
        PIN_number = str(input("Enter your PIN:"))
        if PIN_number != card_pin:
            print("Wrong card number or PIN!")
        else:
            print("You have successfully logged in!")
            while True:
                # Managming the card
                print("1. Balance")
                print("2. Add income")
                print("3. Do transfer")
                print("4. Close account")
                print("5. Log out")
                print("0. Exit")
                choise = int(input())

                if choise == 1:
                    balance = cur.execute(f'SELECT balance FROM card WHERE number = {card_number} and pin = {card_pin}').fetchone()
                    print(f"Your balance: {balance[0]}\n")
                elif choise == 2:
                    self.add_income(card_number)
                elif choise == 3:
                    self.do_transfer(card_number)
                elif choise == 4:
                    self.close_account(card_number)
                    break
                elif choise == 5:
                    print("You have successfully logged out!")
                    break
                elif choise == 0:
                    print("Bye!")
                    exitcheck = True
                    database.close()
                    break
                else:
                    print("Wrong input")
        return exitcheck

    # We put money on the card and update the information in the database
    def add_income(self, card_number):
        income = int(input("Enter income:"))
        cur.execute(f"UPDATE card SET balance = balance + {income} WHERE number = {card_number}")
        conn.commit()

    #We transfer money from one account to another and update the database
    def do_transfer(self, card_number):
        print("Transfer")
        card_num = str(input("Enter card number:"))
        is_good = self.lugh(card_num)

        # Check input information
        try:
            check = str(cur.execute(f'SELECT id FROM card WHERE number = {card_num}').fetchone())
        except sqlite3.OperationalError:
            print("Wrong input")
            return
        
        if is_good == False:
            print("Probably you made mistake in the card number. Please try again!")
            return

        if check != 'None':
            trans = int(input("Enter how much money you want to transfer:"))

            if trans > cur.execute(f'SELECT balance FROM card WHERE number = {card_number}').fetchone()[0]:
                print("Not enough money!")

            else:
                print("Success!")
                # Update database
                cur.execute(f'UPDATE card SET balance = balance - {trans} WHERE number = {card_number}')
                conn.commit()
                cur.execute(f'UPDATE card SET balance = balance + {trans} WHERE number = {card_num}')
                conn.commit()

    # Delete card from the database
    def close_account(self, card_number):
        cur.execute(f'DELETE FROM card WHERE number = {card_number}')
        conn.commit()

    # Checking the card number 
    def lugh(self, card_num):
        checksum = 0

        try:
            for i in range(0, len(card_num)):

                if int(card_num[i]) * 2 > 9:
                    checksum += int(card_num[i]) * 2 - 9
                else:
                    checksum += int(card_num[i]) * 2

            if checksum % 10 == 0:
                return True
            return False
        except ValueError:
            pass


exitcheck = False
new_card = Card()
while exitcheck == False:
    # Main menu
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choose = int(input())

        if choose == 1:
            new_card.create_card()
        elif choose == 2:
            exitcheck = new_card.log_info(exitcheck)
        elif choose == 0 or exitcheck == True:
            print("Bye!")
            database.close()
            exitcheck = True
        else:
            print("Wrong input") 
