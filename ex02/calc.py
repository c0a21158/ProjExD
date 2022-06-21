import tkinter as tk
import tkinter.messagebox as tkm

#ボタンをクリックしたときの関数
def button_click(event):
    txt = event.widget["text"]

    if txt == "=":
        A = entry.get()
        sum = eval(A)
        entry.delete(0,tk.END)
        entry.insert(tk.END,sum)
    else:
        entry.insert(tk.END,txt)

if__name__="__main__"

root = tk.Tk()
root.title("電卓")

entry = tk.Entry(root,
                justify = "right",
                width = 15,
                font = ("Times New Roman",40)
                )
entry.grid(row = 0,column=0,columnspan=3)


r, c = 1, 0 #r:行番号　c:列番号
for num in range(9,-1,-1) :
    btn = tk.Button(root,
                    text=f"{num}",
                    width=4,
                    height=2,
                    font=("Times New Roman",30)
                    )


    btn.bind("<1>",button_click)
    btn.grid(row = r,column = c)
    c += 1
    if (num-1)%3 == 0:
        r +=1
        c = 0

#足し算の追加
btn = tk.Button(root,
                text=f"+",
                width=4,
                height=2,
                font=("Times New Roman",30)
                )
btn.grid(row = r,column= c)
btn.bind("<1>",button_click)
#＝の追加
btn = tk.Button(root,
                text=f"=",
                width=4,
                height=2,
                font=("Times New Roman",30)
                )
btn.grid(row = r,column= c+1)
btn.bind("<1>",button_click)

#*の追加
btn = tk.Button(root,
                text=f"*",
                width=4,
                height=2,
                font=("Times New Roman",30)
                )
btn.grid(row = r+1,column= c)
btn.bind("<1>",button_click)

#/の追加
btn = tk.Button(root,
                text=f"/",
                width=4,
                height=2,
                font=("Times New Roman",30)
                )
btn.grid(row = r+1,column= c+1)
btn.bind("<1>",button_click)

#**の追加
btn = tk.Button(root,
                text=f"**",
                width=4,
                height=2,
                font=("Times New Roman",30)
                )
btn.grid(row = r+1,column= c-1)
btn.bind("<1>",button_click)

btn = tk.Button(root,
                text=f"-",
                width=4,
                height=2,
                font=("Times New Roman",30)
                )
btn.grid(row = r+1,column= c+2)
btn.bind("<1>",button_click)

root.mainloop()