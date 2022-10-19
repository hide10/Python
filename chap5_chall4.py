fav_musicans = ["Jay Z", "Adventure Club", "John Lennon"]

songs = {"John Lennon": "Stand by Me",
         "Kanye West": "Homecoming",
         "Swedish House Mafia": "Don't You Worry Child"
         }

locations = [(40.7128, 74.0059), (31.0461, 34.8516), (8.3405, 115.0920)]

me = {
    "height": "160",
    "fav_color": "Orange",
    "fav_author": "Orwell"
}

answer = input("Type height, fav_color or fav_author")
 
if answer in me:
    result = me[answer]
    print(result)
