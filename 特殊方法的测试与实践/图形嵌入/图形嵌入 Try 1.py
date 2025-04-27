import turtle
import tkinter as tk
from PIL import Image, ImageTk

# 创建 turtle 绘图并保存为图像
pen = turtle.Turtle()
for _ in range(4):
    pen.forward(100)
    pen.right(90)
pen.getscreen().getcanvas().postscript(file="turtle_output.eps")

# 将 EPS 文件转换为 PNG 文件
from PIL import Image
img = Image.open("turtle_output.eps")
img.save("turtle_output.png", "png")

# 创建 tkinter 窗口
root = tk.Tk()
root.title("Turtle in Tkinter")

# 加载图像并显示
img_tk = ImageTk.PhotoImage(Image.open("turtle_output.png"))
label = tk.Label(root, image=img_tk)
label.pack()

# 运行 tkinter 主循环
root.mainloop()