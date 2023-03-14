one_rp = int(input())
five_rp = int(input())

z = int(input())

def check(x,y,z):
    if((5*y+x) <= z):
        print(-1)
    else:
        print("Number of 1 needed:-",z%5)
        print("Number of 5 needed:-",z//5)

check(one_rp,five_rp,z)
    