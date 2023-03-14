# s = input()

def OutputGen(s):
    if(len(s)<2):
        print(-1)
    else:
        print(s[0:2] + s[len(s)-2:len(s)])
    
OutputGen("w3resource")
OutputGen("w3")
OutputGen("A")