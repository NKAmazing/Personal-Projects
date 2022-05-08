import string
import re
import sys

rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
print('Hello World!'.translate(rot13))
# 'Uryyb Jbeyq!'


# CODIGO COMENTADO QUE PUEDE SERVIR DESPUES

# def rot13(s):
#     chars = "abcdefghijklmnopqrstuvwxyz"
#     trans = chars[13:] + chars[:13]
#     rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
#     print(''.join( rot_char(c) for c in s ))

# if __name__ == '__main__':
#     s = "hello world"
#     rot13(s)

# a = []

# for i in sys.stdin:
#     print(i)
#     if i[:3] == "bye":
#         break
#     a.append(i)

# print(a)