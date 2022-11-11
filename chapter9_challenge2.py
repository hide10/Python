answer = input("ファイルに書込む言葉を入力してください")
with open("c9output.txt", "w", ) as f:
    f.write(answer)
