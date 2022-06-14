import random
x = 10 #対象文字
y = 2  #欠損文字
alphabet = [chr(i)for i in range(65,65+26)]



print("対象文字:")
alphabet_A = random.sample(alphabet,x)
print(alphabet_A)



print("表示文字:")
alphabet_B = random.sample(alphabet_A,x-y)
print(alphabet_B)



anser = int(input("欠損文字はいくつあるでしょうか？"))
if anser == y:
    print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
else:
    print("不正解です。またチャレンジしてください")



anser2 = input("1つ目の文字を入力してください")





anser2 = input("2つ目の文字を入力してください")