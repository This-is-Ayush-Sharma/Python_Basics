

def translate(lists, dicts):
    print("Message in English:-",' '.join(lists))
    print("Message in Swedish:-",end=' ')
    for i in lists:
        print(dicts[i],end= ' ')
    

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