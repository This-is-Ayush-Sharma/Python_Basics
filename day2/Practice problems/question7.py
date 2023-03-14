

def translate(list, dict):
    print("Message in English:-",' '.join(list))
    print("Message in Swedish:-",end=' ')
    for i in list:
        print(dict[i],end= ' ')
    

translate(["merry","christmas","and","happy","new","year"],
        {
            "merry": "god",
            "christmas": "jul",
            "and": "och",
            "happy": "gott",
            "new": "nytt",
            "year": "ar"
        }
    )