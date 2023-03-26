#!/usr/bin/python3
for alpha_letters in range(97, 123):
    if alpha_letters == 113 or alpha_letters == 101:
        continue
    print("{:c}".format(alpha_letters), end="")
