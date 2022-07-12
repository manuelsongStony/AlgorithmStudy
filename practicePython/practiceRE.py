import re


if re.match(r'[a-z]s', 'ss'):
    print("good")

if None:
    print("bad")

pass1="1q2w3e4r!!"

if re.match(".[A-Za-z]+.", pass1):
    print("success")

if re.match("[A-Za-z]+.", pass1):
    print("success2")