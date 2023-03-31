text = "the sun rises in the east"
vocab = ["sun", "in", "east", "doctor", "day"]

def find(text, vocab):
    text = text.split()
    support = []
    for i in text:
        if(i not in vocab):
            support.append(i)
    
    return set(support)

print(find(text, vocab))