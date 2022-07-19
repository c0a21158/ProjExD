import tkinter as tk
from tkinter import messagebox

#ウインドウ
win = tk.Tk()
win.title("ブロック崩し")
win.geometry("625x825")
win.resizable(False, False)

#キャンバス
can = tk.Canvas(bg="black", width=600, height=800)
can.place(x=10, y=10)

block = []
for x in range(8) :
    for y in range(1) :
        block.append({"x":x*75+5, "y":y*40+10, "st":1})

def drawBlock() :
    block_count = 0
    for i in range(len(block)):
        x = block[i]["x"]
        y = block[i]["y"]
        st = block[i]["st"]
    #     if ball_y<=y+30 and ball_x>=x-10 and ball_x<=x+60 and st==1 :
    #         by *= -1
    #         block[i]["st"] = 0
        if st==1 :
            can.create_rectangle(x, y, x+70, y+30, fill="white")
            block_count += 1
    # if block_count == 0:
    #     exit()

def gameLoop():
    can.delete("all")
    drawBlock()
    win.after(15, gameLoop)
gameLoop()

#ウインドウループ
win.mainloop()