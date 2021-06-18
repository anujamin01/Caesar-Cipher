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
        if(curr.isupper()):
            result += chr((ord(curr) + n - 65) % 26 + 65)
        elif(curr.islower()): # ASCII is lower case
            result += chr((ord(curr) + n - 97) % 26 + 97)
        else: # neither upper nor lower
            result+=curr
    return result

'''
Function that can decrypt the Caesarean Cipher given the total number of digits shifted
:param str: String that will be shifted
:param n: The number of letters that the string is shifted by
'''
def decrypt(str, n):
    result = " "
    for i in range(len(str)):
        curr = str[i]
        # Check if current char is uppercase
        if(curr.isupper()):
            result+=chr((ord(curr) - n - 65) % 26 + 65)
        # Check if current char is lowercase
        elif (curr.islower()):
            result += chr((ord(curr) - n - 97) % 26 + 97)
        else:
            result+=curr
    return result

# Basic test 

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123 @#$abcdefghijklmnopqrstuvwxyz"
n = 4
result = encrypt(s,n)
print(encrypt(s,n))
print('\n')
print(decrypt(result,n))


