n = list(map(int, input()))
left_number=0
right_number=0
even=True

for i in range(0,len(n)//2):
    left_number+=n[i]
    right_number+=n[len(n)-1-i]

if left_number==right_number:
    print("LUCKY")
else:
    print("READY")


