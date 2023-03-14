
def Add(s):
    if(len(s)<3):
        print(s)
    else:
        if(s[-3:] == "ing"):
            s=s+"ly"
        else:
            s=s+"ing"
        print(s)

Add("sleep")   # sleeping
Add("amazing") # amazingly
Add("is")      # is