a ,b, c = map(int,input().split(','))

if(a == 7):
    print(b*c)
elif(b == 7):
    print(c)
elif(c == 7):
    print(-1)
else:
    print(a*b*c)
