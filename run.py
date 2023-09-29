#!/usr/bin/env python3

import osint

print("Input target phone number: ")

number = input()

data = osint.get_data(number)

print(data)￼
