#print(chr(ord('a')+1))

position=input()
row=int(position[1])
column=ord(position[0])-ord('a')+1

count=8

if column<3:
    count-=2
    if column==1:
        if row>2 and row<7:
            count-=1
        count-=1
if column>7:
    count -= 2
    if column==8:
        if row>2 and row<7:
            count-=1
        count-=1
if row<3:
    count -= 2
    if row==1:
        if column>2 and column<7:
            count-=1
        count-=1
if row>7:
    count -= 2
    if row==8:
        if column>2 and column<7:
            count-=1
        count-=1

print(count)
