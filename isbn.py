class ISBN13(object):
    def __init__(self,number):
        self.number = number
        self.int_list = []
        self.int_dict = {}
        self.true_isbn = True
    def str_to_int(self):
        no_space = self.number.strip(" ")
        for str in no_space:
            if str != "-":
                self.int_list.append(str)
        for str in self.int_list:
            if str.isspace():
                self.int_list.remove(str)
    def check_digit(self):
        self.str_to_int()
        i = 0
        val_prod = 0
        for digit in self.int_list:
            dig_index = self.int_list.index(digit)
            self.int_dict.update({str(i):digit})
            i += 1
            if i == 13:
                i = 0
                
        for key, value in self.int_dict.items():
            if int(key) % 2 == 0:
                val_prod += int(value) * 1
            else:
                val_prod += int(value) * 3
                
        val_prod_mod = val_prod % 10
        val_prod_mod_diff = 10 - val_prod_mod
        digit_to_check = val_prod_mod_diff % 10
        
        if (str(digit_to_check) == self.int_dict["12"]):
            print ("This is a legitimate ISBN-13 number.")
        else:
            print ("This is not a legitimate ISBN-13 number.")
            self.true_isbn = False


def test_func():
    a_var = ISBN13("978 0 471 48648 0")
    b_var = ISBN13("233 9 791 82129 7")
    a_var.check_digit()
    b_var.check_digit()

test_func()

"""
ISBN - International Standard Book Number
-----------------------------------------
There are two ISBN standards: ISBN-10 and ISBN-13.
Support for ISBN-13 is essential, whereas support
for ISBN-10 is optional.
Here are some valid examples of each:

ISBN-10:    0471958697
            0 471 60695 2
            0-470-84525-2
            0-321-14653-0

ISBN-13:    9780470059029
            978 0 471 48648 0
            978-0596809485
            978-0-13-149505-0
            978-0-262-13472-9

ISBN-10 is made up of 9 digits plus a check digit (which
may be 'X') and ISBN-13 is made up of 12 digits plus a
check digit. Spaces and hyphens may be included in a code,
but are not significant. This means that 9780471486480 is
equivalent to 978-0-471-48648-0 and 978 0 471 48648 0.

The check digit for ISBN-10 is calculated by multiplying
each digit by its position (i.e., 1 x 1st digit, 2 x 2nd
digit, etc.), summing these products together and taking
modulo 11 of the result (with 'X' being used if the result
is 10).

The check digit for ISBN-13 is calculated by multiplying
each digit alternately by 1 or 3 (i.e., 1 x 1st digit,
3 x 2nd digit, 1 x 3rd digit, 3 x 4th digit, etc.), summing
these products together, taking modulo 10 of the result
and subtracting this value from 10, and then taking the
modulo 10 of the result again to produce a single digit.


To do:
Check if the string is also a valid ISBN-10."""
