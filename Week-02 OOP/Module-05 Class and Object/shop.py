

class Shop:
    card = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_card(self, items):
        self.card.append(items)

mehzabeen = Shop('mehzabeen')
mehzabeen.add_to_card('shoes')
mehzabeen.add_to_card('iphone')
mehzabeen.add_to_card('ladis watch')
print(mehzabeen.card)

Rasel = Shop('Rasel sarker')
Rasel.add_to_card('cricket bat')
Rasel.add_to_card('football')
Rasel.add_to_card('Tshirt')
Rasel.add_to_card('rolax watch')
print(Rasel.card)
        