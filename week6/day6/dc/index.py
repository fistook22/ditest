cypher_text = ''
text = ''
user_text = ''
user_text = input('would you like to encrypt or decrypt?')
if  user_text == 'encrypt':
    text = input('what is your secret massage?')
    for letter in text:
        text = cypher_text + chr(ord(letter) + 3)
        print(text)
    
if user_text == 'decrypt':
        text = input('what is the encrypted massage you got?') 
        for letter in text:
            text = cypher_text + chr(ord(letter) - 3)
            print(text)

# text = "defghijk"

