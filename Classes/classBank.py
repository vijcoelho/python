import random as rd

class Bank:
    def __init__(self):
        self.current_account = int(input("Put your current account: "))
        self.Food_card_1 = rd.randint(1000,9999)
        self.Food_card_2 = rd.randint(1000,9999)
        self.Food_card_3 = rd.randint(1000,9999)
        self.Food_card_4 = rd.randint(1000,9999)
        self.Credit_card_1 = rd.randint(1000,9999)
        self.Credit_card_2 = rd.randint(1000,9999)
        self.Credit_card_3 = rd.randint(1000,9999)
        self.Credit_card_4 = rd.randint(1000,9999)
    
    def verification(self):
        print(f"That's your current account: {self.current_account}")
        print(f"This is your food card: {self.Food_card_1}.{self.Food_card_2}.{self.Food_card_3}.{self.Food_card_4}")
        print(f"And there here is your credit card: {self.Credit_card_1}.{self.Credit_card_2}.{self.Credit_card_3}.{self.Credit_card_4}")

client = Bank()
client.verification()




