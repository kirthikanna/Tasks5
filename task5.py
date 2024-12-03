from functools import reduce
import re
class mail:
    special_char = ['!', '#', '@', '$', '%', '^', '&', '*', '_', ' ', ':']
    def __init__(self, email, mobile, password):
        self.email = email
        self.mobile = mobile
        self.password = password
    def user_address(self):
        self.low = str.lower(self.email)
        self.b = re.split("@", self.low)
        # print(self.b[0])
        if len(self.low) <= 30:
            for i in self.b[0]:
                for j in self.special_char:
                    if i == j:
                        print("invalid because usage of special character not allowed")
                        break
        elif self.b[1] != "gmail.com":
            print("invalid email because of user address is not in format")
        else:  # if the length is not matching it will throw an error
            print("invalid email", self.email)
    def mobile_number(self):
        if len(self.mobile) == 7:
            if self.mobile.isnumeric():
                print("valid bangladesh mobile number\n", self.mobile)
            else:
                print("enter number not valid usage of characters rather than numbers")
        else:
            print("entered number is not valid")


    def pass_word(self, up, low, number, special):
        self.up = 0
        self.low = 0
        self.number = 0
        self.special = 0
        if len(self.password) == 16:
            print("the given password length is matching")
            for i in self.password:
                if i.isupper():
                    # print(type(self.up))
                    self.up += 1
                # print(self.up)
                if i.islower():
                    self.low += 1
                # print(self.low)
                if i.isdigit():
                    self.number += 1
                    # print(type(self.number))
                    # print(self.number)
                if i == '@' or i == '#' or i == '$' or i == '%' or i == '&':
                    self.special += 1
                    # print(self.special)
            # print(self.up+self.low+self.number+self.special)
            if self.up >= 1 and self.low >= 1 and self.number >= 1 and self.special >= 1 and (
                    self.up + self.low + self.number + self.special) == len(self.password):
                print("password is valid", self.password)
            else:
                print("given password is invalid")
        else:
            print("the given length is more or lesser than specified length")


obj = mail("Keerthana20@gmail.com", "1234567",  "Keerthana@67")
obj.user_address()
obj.mobile_number()
obj.pass_word('up', 'low', 'number', 'special')