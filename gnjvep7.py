songs = {"1": "fun",
         "2": "blue",
         "3": "me",
         "4": "floor",
         "5": "life"
         }

n = input("数字を入力して下さい:")
if n in songs:
    song = songs[n]
    print(song)
else:
    print("見つかりません")
