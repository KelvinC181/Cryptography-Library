class stringTranslation:
    def string_to_ascii(self, sentence):
        """
        treat each letter as a unit of a base 256 number, then conver this number to decimal
        e.g. ab  ->  97 98 -> 97*1 + 98*256
        """
        ascii_output = 0
        power = 1
        if not sentence or not isinstance(sentence, str):
            raise ValueError("empyt string")
        #for each number, take its ascii order and put it as a digit of the 
        for letter in sentence:
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
        if ascii <= 0 or not isinstance(ascii, int):
            raise ValueError("invalid ascii code")
        charlist = []
        while ascii > 0:
            #gets last digit of the base 256 number
            charlist.append(chr(ascii%256))
            #removes last digit
            ascii //= 256
        
        return "".join(charlist)


"""
to do:
learn bitwise operations to make this O(N) instead of O(N^2)
"""

test = stringTranslation()
trail = test.string_to_ascii("abc def")
print(test.string_to_ascii("abcdefghijk"))
print(trail)
print(test.ascii_to_string(trail))

        