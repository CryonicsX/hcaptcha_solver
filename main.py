import random
from enum import Enum
 
class Card(Enum):
    Visa = 0
    Mastercard = 1

 
def computeCheckDigit(cardNumber):
    total = 0
    digits = cardNumber[::-1]
    for i in range(len(digits)):
        digit = int(digits[i])
        if i % 2 == 0:
            digit *= 2
        total += sum(map(int, str(digit)))
    return (total * 9) % 10
 
def fillToLength(text, length):
    toAdd = length - len(text)
    for _ in range(toAdd):
        text += str(random.randint(0, 9))
    return text
 
def genCardNumber(cardType):
    if cardType == Card.Visa:
        length = 16
        prefix = str(4)
    elif cardType == Card.Mastercard:
        length = 16
        prefix = str(random.randint(51, 55))
    elif cardType == Card.AmericanExpress:
        length = 15
        prefix = str(random.choice([34, 37]))
    else:
        raise Exception("Invalid card type!")
    cardNumber = fillToLength(prefix, length - 1)
    return cardNumber + str(computeCheckDigit(cardNumber))
 

def generateCVV():
   am = random.randint(0, 9)
   yarak = random.randint(0, 9)
   amcık = random.randint(0, 9)
   cvv = str(am) + str(yarak) + str(amcık)
   return cvv


def generateEXP():
	ay = random.randint(1,12)
	yıl = random.randint(21,35)
	if ay < 10:
		ay = f"0{ay}"
	return f"{ay}/{yıl}"


cart_type = input("enter card type (visa/master) => ").lower()
count = int(input("how much will you produce => "))

if cart_type == "visa":
	with open('ccler.txt', 'a') as f:
		    f.write("ID      CART      CARD NUMBER      SKT      CVV\n\n")
		    for x in range(0,count):
		        f.write(f"{x}      VISA      {genCardNumber(Card.Visa)}      {generateEXP()}      {generateCVV()}\n")
		
		        print(f"{genCardNumber(Card.Visa)} | {generateEXP()} | {generateCVV()}")


elif cart_type == "master":
	with open('ccler.txt', 'a') as f:
		    f.write("ID      CART      CARD NUMBER      SKT      CVV\n\n")
		    for x in range(0,count):
		        f.write(f"{x}      MASTERCARD      {genCardNumber(Card.Visa)}      {generateEXP()}      {generateCVV()}\n")
		
		        print(f"{genCardNumber(Card.Mastercard)} | {generateEXP()} | {generateCVV()}")

    
else:
    print("invalid cart (VİSA/MASTER)")

