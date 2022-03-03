n,m,k =map(int,input().split())
data=list(map(int, input().split()))
data.sort()
first = data[n-1]
second =data[n-2]

quotient=m//(k+1)
remainder=m%(k+1)
result=quotient*(k*first+second) +remainder*first


print(result)