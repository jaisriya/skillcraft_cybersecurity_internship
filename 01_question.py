def caesar_cipher(text,shift,mode):
    result=""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result +=chr((ord(char)-65+shift)%26+65)
            else:
                result +=chr((ord(char)-97+shift)%26+97)
        else:
           result+= char
    return result

message=input("enter your message:")
shift=int(input("enter shift value:"))

encrypted=caesar_cipher(message,shift,"encrypt")
print("encrypted message:",encrypted)

decrypted=caesar_cipher(encrypted,-shift,"decrypt")
print("decrypted message:",decrypted)


