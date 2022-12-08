#!/usr/bin/env python3

import string

# print(string.ascii_uppercase)
# print(string.digits)

flag = []

with open("message.txt") as filp:
	
	contents = filp.read()
	numbers = [int(val) for val in contents.split()]
	for number in numbers:
		modulus = number % 37

		if modulus in range(26):
			flag.append(string.ascii_uppercase[modulus])
		elif modulus in range(26,36):
			flag.append(string.digits[modulus - 26])
		else:
			flag.append("_")

print("picoCTF{%s}" % "".join(flag)) 