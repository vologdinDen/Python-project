from random import randint
import sqlite3

class Bank:

    def create_card(self):
        print("Your card has been created")

        customer_account_number = f"400000{str(randint(100000000, 1000000000))}"
        customer_account_number = self.lugh(customer_account_number)
        print(f"Your card number:{customer_account_number}")

        PIN = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
        print(f"Your card PIN: {PIN}")
        
        cur.execute(f'INSERT INTO card (number, pin, balance) VALUES ({customer_account_number},{PIN},{0})')
        conn.commit()
        return False

    def lugh(self, account_number):
        checksum = 0
        for i in account_number:
            if int(i) * 2 > 9:
                checksum += int(i) * 2 - 9
            else:
                checksum += int(i) * 2
        last_char = str(10 - checksum % 10)
        return f"{account_number}{last_char}"

    def log_info(self):

        login_menu = {
        "1": self.show_balance,
        "2": self.add_income,
        "3": self.do_transfer,
        "4": self.close_account,
    }

        card_number = str(input("Enter your card number:"))
        try:
            card_pin_db = str(cur.execute(f'SELECT pin FROM card WHERE number = {card_number}').fetchone())
            card_pin = card_pin_db[2:6]
        except sqlite3.OperationalError:
            print("Wrong input")
            return 
        
        PIN_number = str(input("Enter your PIN:"))
        if PIN_number != card_pin:
            print("Wrong card number or PIN!")
        else:
            self.card_number = card_number
            print("You have successfully logged in!")
            while True:
                print("1. Balance")
                print("2. Add income")
                print("3. Do transfer")
                print("4. Close account")
                print("5. Log out")
                print("0. Exit")
                choise = input()

                if choise in login_menu:
                    login_menu[choise]()
                elif choise == "5":
                    print("You have successfully logged out!")
                    return False
                elif choise == "0" or choise == "4":
                    database.close()
                    return True
                else:
                    print("Wrong input")

    def show_balance(self):
        balance = cur.execute(f'SELECT balance FROM card WHERE number = {self.card_number}').fetchone()
        print(f"Your balance: {balance[0]}\n")

    def add_income(self):
        income = int(input("Enter income:"))
        cur.execute(f"UPDATE card SET balance = balance + {income} WHERE number = {self.card_number}")
        conn.commit()

    def do_transfer(self):
        print("Transfer")
        transfer_card = str(input("Enter the number of the card you want to transfer to: "))

        try:
            card_id = str(cur.execute(f'SELECT id FROM card WHERE number = {transfer_card}').fetchone())
        except sqlite3.OperationalError:
            print("Wrong input")
            return
        
        if card_id != 'None':
            money_for_transfer = int(input("Enter how much money you want to transfer:"))

            if money_for_transfer > cur.execute(f'SELECT balance FROM card WHERE number = {self.card_number}').fetchone()[0]:
                print("Not enough money!")

            else:
                print("Success!")
                cur.execute(f'UPDATE card SET balance = balance - {money_for_transfer} WHERE number = {self.card_number}')
                conn.commit()
                cur.execute(f'UPDATE card SET balance = balance + {money_for_transfer} WHERE number = {transfer_card}')
                conn.commit()

    def close_account(self):
        cur.execute(f'DELETE FROM card WHERE number = {self.card_number}')
        conn.commit()
        print("Your account is closed")


 

if __name__ == "__main__":
    database = open('card.s3db', 'a+')
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS card('
                'id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, '
                'number TEXT, '
                'pin TEXT, '
                'balance INTEGER DEFAULT 0)')
    conn.commit()

    bank = Bank()

    main_menu_command = {
        "1": bank.create_card,
        "2": bank.log_info,
        "0": database.close,
    }

    while True:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choose = input()

        if choose in main_menu_command:
            exit_check = main_menu_command[choose]()

            if choose == "0" or exit_check:
                print("Bye!")
                break
        else:
            print("Wrong input")    