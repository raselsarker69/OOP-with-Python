

class Shop:
    Shoping_mall = 'Bashundhra Shoping complex'

    def __init__(self,buyer):
        self.buyer = buyer
        self.card = []

    def add_to_card(self,item):
        self.card.append(self,item)

Rasel = Shop('Rasel sarker')
Rasel.add_to_card('cricket bat')
Rasel.add_to_card('football')
Rasel.add_to_card('Tshirt')
Rasel.add_to_card('rolax watch')
print(Rasel.card)


# mehzabeen = Shop('mehzabeen')
# mehzabeen.add_to_card('shoes')
# mehzabeen.add_to_card('iphone')
# mehzabeen.add_to_card('ladis watch')
# print(mehzabeen.card)

       