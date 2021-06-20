from tkinter import *

'''
Program to implement a Caesar Cipher

v1.0 works in console

v2.0 create a GUI for program
'''

'''
Function that will encrypt an alphabet string by shifting letters by n letters
:param str: String that will be shifted
:param n: The number of letters that the string is shifted by
'''


def encrypt(str, n):
    result = " "

    for i in range(len(str)):
        curr = str[i]
        # Check if upper case
        # ASCII code for 'A' is 65
        if (curr.isupper()):
            result += chr((ord(curr) + n - 65) % 26 + 65)
        elif (curr.islower()):  # ASCII is lower case
            result += chr((ord(curr) + n - 97) % 26 + 97)
        else:  # neither upper nor lower
            result += curr
    return result


'''
Function that can decrypt the Caesarean Cipher given the total number of digits shifted
:param str: String that will be shifted
:param n: The number of letters that the string is shifted by
'''


def decrypt(input, n):
    result = " "
    for i in range(len(input)):
        curr = input[i]
        # Check if current char is uppercase
        if (curr.isupper()):
            result += chr((ord(curr) - n - 65) % 26 + 65)
        # Check if current char is lowercase
        elif (curr.islower()):
            result += chr((ord(curr) - n - 97) % 26 + 97)
        else:
            result += curr
    return result


'''
Helper function that will print the encryption to console
'''


def print_encrypt():
    string = f"(str.get())"
    shift = n.get()
    res = encrypt(input.get(), shift)
    print(res)

print(encrypt("A", 1))

'''
Helper function that will print the decryption to console
'''

def print_decrypt():
    string = f"(str.get())"
    shift =  n.get()
    res = decrypt(str.get(), shift)
    print(res)

### Building a GUI ###
cipher = Tk()
cipher.title("Caesar Cipher")
cipher.geometry("250x400")

# String input and int input
input = StringVar()
n = IntVar()

# Text and entry to insert encrypt
encrypt_txt = Label(cipher, text="Enter string to encrypt",
                    font=("Arial", 11)).place(x=10, y=10)

encrypt_entry = Entry(cipher, textvariable=input, bg="white",
                      width=20, font=("Arial", 11)).place(x=10, y=30)


# Text entry to insert decrypt
decrypt_txt = Label(cipher, text = "Enter string to decrypt",
                   font = ("Arial", 11)).place(x = 10, y = 140)

decrypt_entry = Entry(cipher, textvariable = str, bg = "white",
                  width = 20, font = ("Arial",11)).place(x = 10, y = 160)



# Text and entry spot to insert integer to shift text by
n_txt = Label(cipher, text="Enter number of letters to shift by",
              font=("Arial", 11)).place(x=10, y=90)

n_entry = Entry(cipher, textvariable=n, bg="white", width=20,
                font=("Arial", 11)).place(x=10, y=110)

encrypt_call = Button(cipher, text="ENCRYPT!", width=10, command=print_encrypt).place(x=10, y=60)
decrpyt_call = Button(cipher, text="DECRYPT!", width=10, command=print_decrypt).place(x=10, y=190)
# Output = Text(cipher, height = 2, width = 20).place(x = 10, y = 70)
cipher.mainloop()
