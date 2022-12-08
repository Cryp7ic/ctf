#!/usr/bin/env python3

import string

flag = []

with open("message.txt") as filp:
	
	contents = filp.read()
	numbers = [int(val) for val in contents.split()]
	print(numbers)
	for number in numbers:
		modulus = pow(number, -1, 41)
		print(modulus)

		if modulus in range(1, 27):
			flag.append(string.ascii_uppercase[modulus-1])
		elif modulus in range(27,37):
			flag.append(string.digits[modulus - 27])
		else:
			flag.append("_")

print("picoCTF{%s}" % "".join(flag)) 