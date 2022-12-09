print('Uppercase code points')
print(ord('A'))
print(ord('B'))
print(ord('Z'))
print('Lowercase code points')
print(ord('a'))
print(ord('b'))
print(ord('z'))

#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print(f"{ch}", end="")

uppercase("BaBa")