import tkinter as tk
from tkinter import messagebox


#ゲームオーバー
def gameOver():
    messagebox.showinfo("Information", "GAME OVER!")
    exit()

#ゲームクリア
def gameClear():
    messagebox.showinfo("Information", "CONGRATULATIONS!!!!")
    exit()


#ラケット
rack_x =170; keyPress_R = False; keyPress_L = False
def rightKeyPress(event):
    global keyPress_R
    keyPress_R = True
def rightKeyRelease(event):
    global keyPress_R
    keyPress_R = False
def leftKeyPress(event):
    global keyPress_L
    keyPress_L = True
def leftKeyRelease(event):
    global keyPress_L
    keyPress_L = False
def drawRacket():
    global rack_x
    can.create_rectangle(rack_x, 580, rack_x+60, 595, fill="white")
    if keyPress_R==True and rack_x<=350:
        rack_x += 5
    if keyPress_L==True and rack_x>=-10:
        rack_x -= 5

if __name__== "__main__":
    #ウインドウ
    root = tk.Tk()
    root.title("ブロック崩し")
    root.geometry("625x825")
    root.resizable(False, False)
    #キャンバス
    can = tk.Canvas(root, width=600, height=800,bg="black")
    drawRacket()
    root.bind("<KeyPress-Right>", rightKeyPress)
    root.bind("<KeyRelease-Right>", rightKeyRelease)
    root.bind("<KeyPress-Left>", leftKeyPress)
    root.bind("<KeyRelease-Left>", leftKeyRelease)
root.mainloop()

