
def find_more_than_average(tup):
    avg = sum(tup)/len(tup)
    count = 0
    for i in  tup:
        if(i > avg):
            count+=1
    return ((count/len(tup))*100)

def generate_fequency(tup):
    x = [int(0) for i in range(0,26)]
    for i in tup:
        x[i]+=1
    return x

def sort_marks(tup):
    # tup.sorted()
    # lists = list(tup)
    # lists.sort()
    return sorted(tup)

print(find_more_than_average((12,18,25,24,2,5,18,20,20,21)))
print(generate_fequency((12,18,25,24,2,5,18,20,20,21)))
print(sort_marks((12,18,25,24,2,5,18,20,20,21)))