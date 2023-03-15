sentence = [ "a new world recored was set",
              "in the holy city of ayodhya",
              "on the eve of diwali on tuesday",
              "with over three lakh diya or learthen lamps",
              "lit up simultaneously on the banks of the sarayu river"
            ]
stopwords = [ 'was','for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']


sentence = [[j for j in i.split() if(j not in stopwords)] for i in sentence]
print(sentence)