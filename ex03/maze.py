import tkinter as tk
import maze_maker as mm


def key_down(event):#keyが押されたとき
    global key#global変数
    key = event.keysym
    print(f"{key}キーが押されました")
    

def key_up(event):
    global key#global変数
    key = ""

def main_proc():#こうかとんの移動方法の設定とマップの生成
    global cx, cy,mx,my#global変数


    delta = {                   #キー：押されているキーkey/値:移動幅リスト[x,y]
        "Up"   :[0,-1],
        "Down" :[0,+1],
        "Left" :[-1,0],
        "Right":[+1,0],
    }

    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0:
            my, mx = my+delta[key][1] ,mx+delta[key][0]

        if key == "r":
            Re()
        if key == "b":
            bg = "blue"
    except:
        pass

    cx, cy = mx*100+50 , my*100+50
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

def Re(event): #リスタート
    global cx,cy,mx,my,key
    if key == "r" :
        cx,cy = 1,1
        root.after(100,Re)


if __name__ == "__main__": #メイン
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width= 1500,height=900,bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)

    tori = tk.PhotoImage(file="ex03/fig/5.png")
    
    mx ,my = 1,1
    cx, cy = mx*100 + 50, my*100 +50
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key = ""
    root.bind("<KeyPress>" ,key_down,Re)
    
    root.bind("<KeyRelease>",key_up)
    
    root.after(100,main_proc)
    root.mainloop()