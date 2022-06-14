import random
from re import A
num = random.randint(0,3)#azasu

if num == 0:
    print("問題：サザエの旦那の名前は？")
    x = input("")
    if x == "ますお" or "マスオ":
        print("正解")
    else:
        print("不正解")

elif num == 1:
    print("問題:カツオの娘の名前は？")
    x = input("")
    if x == "わかめ" or "ワカメ":
        print("正解")
    else:
        print("不正解")
        
else:
    print("問題：タラオはカツオから見てどんな関係？")
    x = input("")
    if x == "おい" or "甥" or "甥っ子" or "おいっこ":
        print("正解")
    else:   
        print("不正解")