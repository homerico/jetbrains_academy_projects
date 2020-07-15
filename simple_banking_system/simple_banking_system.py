class Card:
    def __init__(self, card_num, pin):
        self.card_number = card_num
        self.card_pin = pin
        self.balace = 0


def create_account(customer_account_length=9):
    card_num = "400000"
    for i in range(customer_account_length):
        card_num += str(random.randint(0, 9))
    card_num += "9"
    pin = ''
    for i in range(4):
        pin += str(random.randint(0, 9))
    return int(card_num), pin


def log_in(user_card_num, user_pin):
    user_permission = [card_position for card_position, card in enumerate(credit_cards)
                       if user_card_num == card.card_number and user_pin == card.card_pin]
    if len(user_permission) == 1:
        print("You have successfully logged in!")
        return True, user_permission[0]
    else:
        print("Wrong card number or PIN!")
        return False, None


credit_cards = list()
execution = True
while execution:
    answer = int(input("""1. Create an account
    2. Log into account
    0. Exit
    """))
    if answer == 0:
        break
    elif answer == 1:
        card_num, pin = create_account()
        credit_cards.append(Card(card_num, pin))
        print(f"""Your card has been created
Your card number:
{card_num}
Your card PIN:
{pin}
""")
    else:
        user_card_num = int(input("Enter your card number:\n"))
        user_pin = input("Enter your PIN:\n")
        logged, card_id = log_in(user_card_num=user_card_num, user_pin=user_pin)
        while logged:
            logged_input = int(input("""1. Balance
2. Log out
0. Exit
"""))
            if logged_input == 0:
                execution = False
                break
            elif logged_input == 1:
                print(f"Balance: {credit_cards[card_id].balace}")
            else:
                print("You have successfully logged out!")
                break

print("Bye!")

