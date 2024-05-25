message = input(" > ")
words = message.split(" ")   # to split words what we will enter in the input.
emojis = {
    ":)": "😂",
    ":(": "😭"
}
output = ""
for item in words:
    output += emojis.get(item, item) + " "
print(output)



