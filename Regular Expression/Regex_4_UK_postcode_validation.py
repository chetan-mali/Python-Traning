# We write an expression, which is capable of recognizing the postal codes or postcodes of the UK.

"""
   Postcode units consist of between five and seven characters,
    which are separated into two parts by a space.
    The two to four characters before the space represent the so-called outward
    code or out code intended to direct mail from the sorting office to the delivery office.
    The part following the space, which consists of a digit followed by two uppercase characters,
    comprises the so-called inward code, which is needed to sort mail at the final delivery office.
    The last two uppercase characters do not use the letters CIKMOV,
    so as not to resemble digits or each other when hand-written.

    The outward code can have the form: One or two uppercase characters,
    followed by either a digit or the letter R,
    optionally followed by an uppercase character or a digit.
    (We do not consider all the detailed rules for postcodes,
    i.e only certain character sets are valid depending on the position
    and the context.) 
"""
import re

example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]
expr = re.compile("^([A-Z]{1,2}[0-9A-Z]{0,2})\s{1}([0-9][^CIKMOV0-9\s\W]{2})$")
for code in example_codes:
    if len(expr.findall(code)) != 0:
        print("Valid Code :",code)
    else:
        print("Invalid Code :",code)