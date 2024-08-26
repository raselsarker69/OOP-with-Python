

class Phone:
    manufacturer = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price


    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)


my_phone = Phone('Rasel sarker','samsung',12500)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_Phone = Phone('Robuiya akter', 'iPhone', 120000)
print(her_Phone.owner, her_Phone.brand, her_Phone.price)