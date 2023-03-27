
l1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
l2 = ['y' , 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

w = ""

for i in range(0,len(l1)):
    w = w+str(l1[i]) + str(l2[len(l2)-i-1])+" "
    
w.replace("None","")
print(w)