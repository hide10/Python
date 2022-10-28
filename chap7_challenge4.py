numbers = [1, 5, 8]
while True:
    num = input("num or q(exit)")
    if num == "q":
        break
    try:
        num = int(num)
    except ValueError:
        print("数字かqを入力して下さい")
    if num in numbers:
        print("正解")
    else:
        print("不正解")
