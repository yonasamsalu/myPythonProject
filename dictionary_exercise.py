"""
1. The code starts by asking the user to input a phone number using the input() function.
       The input is stored in the variable phone.
2. Next, there's a dictionary called digits_mapping which maps
       each digit (as a string) to its corresponding word representation.
3. Then, there's an empty string variable called
      output which will store the converted phone number.
4. The code then iterates over each character in the phone string using a for loop.
5. For each character in the phone string, it checks if it exists in the digits_mapping dictionary
    using the .get() method. If the character exists in the dictionary, it adds its corresponding word
     representation to the output string. If the character is not found in the dictionary, it adds ! to the output string.
6.Finally, the code prints the output string, which contains the phone number converted into words where possible,
        and ! for any characters that are not digits.

So, for example, if you input the phone number "1234", the output would be "One Two Three Four".
If you input a phone number with characters other than digits, such as "abc123", it would output "!!!One Two Three".
"""
phone = input("Phone: ")
digits_mapping={
    "d": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four "
}
output = ""
for character in phone:
    output +=digits_mapping.get(character, "!" )
print(output)