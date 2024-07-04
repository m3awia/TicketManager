import random

class User:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_user_name(self):
        return self.name

    def get_user_number(self):
        return self.number

class Payment:
    def __init__(self, card_number, name, ex_date, cvc_num, user):
        self.card_number = card_number
        self.name = name
        self.ex_date = ex_date
        self.cvc_num = cvc_num
        self.user = user

    def check(self):
        # Check card number format (16 digits)
        if not (self.card_number.isdigit() and len(self.card_number) == 16):
            return False
        
        # Check expiry date format (MM/YY)
        if not (len(self.ex_date) == 5 and self.ex_date[:2].isdigit() and self.ex_date[2] == '/' and self.ex_date[3:].isdigit()):
            return False
        
        # Check CVC number format (3 digits)
        if not (self.cvc_num.isdigit() and len(self.cvc_num) == 3):
            return False
        
        # Additional checks can be added for name if needed
        return True

    def generate_reservation_number(self):
        # Generate a random reservation number
        return random.randint(10000, 99999)

    def send_sms(self):
        
        # Generate reservation number
        reservation_number = self.generate_reservation_number()

        # Send SMS
        message_body = f"Hello {self.user.get_user_name()}, your reservation (#{reservation_number}) has been confirmed. Enjoy your movie🎬⭐!"
        print(message_body)
      
        
# main
if __name__ == "__main__":
    # Create a user
    user = User("John Doe", "+966544079083")

    # Make a payment (example data)
    payment1 = Payment("1234567812345678", "John Doe", "12/23", "123", user)

    # Check payment details
    if payment1.check():
      
        print("Payment successful and reservation confirmed.")
        payment1.send_sms()
    else:
        print("Invalid payment details.")
