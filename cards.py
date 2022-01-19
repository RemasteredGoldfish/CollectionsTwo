import random

cardSign = ['Hearts', 'Spade', 'Clubs', 'Diamonds']
cardElement = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

for i in range(1):
    for i in range(1,8):
        randomPoint = random.choice(cardElement)
        randomSign = random.choice(cardSign)
        randomCard = randomPoint,randomSign
        print('card', i ,randomCard)

for color in cardSign:
    for card in cardElement:
        combine = color + ' ' + card
        print(combine)