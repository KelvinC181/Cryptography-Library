class stringTranslation:
    def string_to_ascii(self, string):
        """
        encode string to their ascii-code then stack the ascii codes to one base 256 number
        """
        ascii_output = 0
        power = 1
        if not string:
            raise ValueError("empyt string")
        for i,letter in enumerate(string):
            ascii_output += (ord(letter) * power)
            power *=256
        return ascii_output

    def ascii_to_string(self, ascii):
        """
        turn each last digit back to its ascii code and then into character
        append each character to list then join them into the original sentense

        *I originally use += on empty string, but due to the way python handles strings as immutable objects,
         it creates a new string each time which makes it is significantly slower
        """
        charlist = []
        while ascii > 0:
            #gets last digit of the base 256 number
            charlist.append(chr(ascii%256))
            #removes last digit
            ascii //= 256
        
        return "".join(charlist)

test = stringTranslation()
trail = test.string_to_ascii("abc def")
print(trail)
print(test.ascii_to_string(trail))

        