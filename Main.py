import os
import tkinter as tk
import tkinter.messagebox
from tkinter import Entry
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

def check():
    tk.messagebox.showinfo(title='Hi', message='检测开始，loading')
    pass

def selectPath():
    path_ = askopenfilename()
    path.set(path_)
    img_open = Image.open(e1.get())
    img_open = img_open.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    l1.config(image=img)
    l1.image = img

if __name__=='__main__':

    os.chdir('/home/jzy/Desktop/M_Rasp-GUI-Control_')

    root=tk.Tk()
    root.title('应用程序窗口')  # 窗口标题
    root.resizable(False, False)  # 固定窗口大小
    windowWidth = 1000  # 获得当前窗口宽
    windowHeight = 800  # 获得当前窗口高
    screenWidth, screenHeight = root.maxsize()  # 获得屏幕宽和高
    geometryParam = '%dx%d+%d+%d' % (
        windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2)
    root.geometry(geometryParam)  # 设置窗口大小及偏移坐标
    root.wm_attributes('-topmost', 1)  # 窗口置顶

    # label文本
    label_text = tk.Label(root, text='Auto Lab', font="Verdana 20 bold")
    label_text.grid(row=0, column=2)

    button_bitmap = tk.Button(root, text='Check Sample', command=check)
    button_bitmap['width'] = 30
    button_bitmap['height'] = 2
    button_bitmap.grid(row=20, column=2)

    # .................................. Left ...................................
    # Todo：
    #       增加如果不选择
    # 设置左侧显示
    left_frame = tk.Frame(root)
    left_label = tk.Label(left_frame, text='待检测图片').grid(row=0, column=1)
    left_frame.grid(row=1, column=0)

    # 路径选择 # 读取图片
    path = tk.StringVar()
    tk.Button(left_frame, text="路径选择", command=selectPath).grid(row=1, column=1)
    e1 = Entry(left_frame, text=path)
    e1.grid(row=2, column=1)
    l1 = tk.Label(left_frame)
    l1.grid(row=3, column=1)

    # .................................. Right ..........................................
    # 设置右侧显示
    right_frame = tk.Frame(root)
    right_frame.grid(row=1, column=3)

    input_label = tk.Label(right_frame).grid(row=0, column=1)

    # .....................................................................





    root.mainloop()



