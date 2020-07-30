import sqlite3
import random
 
 
class Card:
    def __init__(self, card_num, pin):
        self.card_number = card_num
        self.card_pin = pin
        self.balace = 0
 
 
def checksum(original_card_num):
    original_card_num = [int(num) for num in original_card_num]
    for index, num in enumerate(original_card_num):
        if index % 2 == 0:
            original_card_num[index] *= 2
        if original_card_num[index] > 9:
            original_card_num[index] -= 9
    return str((10 - (sum(original_card_num) % 10)) % 10)
 
 
def create_account(customer_account_length=9):
    global id_
    while id_ in [intern_id[0] for intern_id in cur.execute("SELECT id FROM card")]:
        id_ += 1
    card_num = "400000"
    pin = ''
    for i in range(customer_account_length):
        card_num += str(random.randint(0, 9))
    card_num += checksum(card_num)
    for i in range(4):
        pin += str(random.randint(0, 9))
    cur.execute("""
    INSERT INTO card VALUES (
        ?,
        ?,
        ?,
        0
    );""", (id_, card_num, pin))
    conn.commit()
    return card_num, pin
 
 
def log_in(user_card_num, user_pin):
    cur.execute("SELECT id FROM card WHERE number=? AND pin=?", (user_card_num, user_pin))
    user_permission = cur.fetchone()
    if user_permission != None:
        print("You have successfully logged in!")
        return True, user_permission[0]
    else:
        print("Wrong card number or PIN!")
        return False, None
 
 
credit_cards = list()
id_ = 0
execution = True
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS card (
    id INTEGER,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT  0
);""")
conn.commit()
while execution:
    answer = int(input("""1. Create an account
2. Log into account
0. Exit
"""))
    if answer == 0:
        break
    elif answer == 1:
        card_num, pin = create_account()
        print(f"""Your card has been created
Your card number:
{card_num}
Your card PIN:
{pin}
""")
    else:
        user_card_num = input("Enter your card number:\n")
        user_pin = input("Enter your PIN:\n")
        logged, card_id = log_in(user_card_num=user_card_num, user_pin=user_pin)
        while logged:
            logged_input = int(input("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""))
            if logged_input == 0:
                execution = False
                break
            elif logged_input == 1:
                cur.execute("SELECT balance FROM card WHERE id=?", (card_id, ))
                print("Balance: ",cur.fetchone()[0])
            elif logged_input == 2:
                income = int(input("Enter income:\n"))
                cur.execute('UPDATE card SET balance=balance+? WHERE id=?', (income, card_id))
                conn.commit()
                print("Income was added!\n")
            elif logged_input == 3:
                recipient = input("""Transfer\nEnter card number:\n""")
                if recipient[-1] != checksum(recipient[0:-1]):
                    print("Probably you made mistake in the card number. Please try again!")
                    continue
                cur.execute("SELECT id FROM card WHERE number=?", (recipient, ))
                recipient_id = cur.fetchone()
                if recipient_id is None:
                    print("Such a card does not exist.")
                    continue
                elif recipient_id[0] == card_id:
                    print("You can't transfer money to the same account!")
                    continue
                recipient_id = recipient_id[0]
                value = int(input("Enter how much money you want to transfer:\n"))
                cur.execute("SELECT balance FROM card WHERE id=?", (card_id, ))
                if value > cur.fetchone()[0]:
                    print("Not enough money!")
                    continue
                SQL_script = f"""UPDATE card SET balance=balance-{value} WHERE id={card_id};
                                 UPDATE card SET balance=balance+{value} WHERE id={recipient_id}"""
                cur.executescript(SQL_script)
                conn.commit()
                print("Success!")
            elif logged_input == 4:
                cur.execute("DELETE FROM card WHERE id=?", (card_id, ))
                conn.commit()
                print("The account has been closed!")
                break
            else:
                print("You have successfully logged out!")
                break
conn.close()
print("Bye!")
