import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog
import os


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="选择图片",
    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
)

if not file_path:
    print("未选择图片")
    exit()


img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

if img is None:
    print("读取失败")
    exit()


thresh = simpledialog.askinteger(
    "阈值调节",
    "请输入二值化阈值 (0-255)",
    minvalue=0,
    maxvalue=255,
    initialvalue=80
)

if thresh is None:
    print("未设置阈值")
    exit()


_, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)


save_path = file_path.replace(".", "结果.")
cv2.imencode('.png', binary)[1].tofile(save_path)
print("已保存:", save_path)


os.startfile(save_path)