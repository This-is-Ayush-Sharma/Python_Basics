
def Check_Palindrome(n):
    return True if(str(n)[::-1]==str(n)) else False

check_prm = lambda n : str(n)[::-1]==str(n)
n = 1221 + 1

while(not check_prm(n)):
    n+=1

print(n)


