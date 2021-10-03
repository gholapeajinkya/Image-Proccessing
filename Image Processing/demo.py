from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np
import cv2
import datetime
from tkinter import messagebox

# Read Image to be Proccessed
def getImage():
    try:
        filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        return filename
    except: 
        messagebox.showinfo("Alert", "Something went wrong")
        return

# Save Proccessed Image
def saveImage():
    try:
        img = cv2.cvtColor(th, cv2.COLOR_BGR2RGB)
        file = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print(file)
        cv2.imwrite(file,img)
        messagebox.showinfo("Save", "Image Saved")
    except: 
        messagebox.showinfo("Message", "first browse an image using Browse Image button")

def sel(x):
    try:
        global selection
        selection = var.get()
        global th
        th = cv2.adaptiveThreshold(grayscaled, selection , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)       
        img2 = Image.fromarray(th)
        img2 = img2.resize((500, 350), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)

        panel = Label(window, image = img2)
        panel.image = img2
        panel.place(x=515, y=10)
    except: 
        messagebox.showinfo("Alert", "Something went wrong")
        return

# Process Image
def proceessImage():
    try:
        filename = getImage()
        print(filename)
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((500, 350), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        panel = Label(window, image = img)
        panel.image = img
        panel.place(x=10, y=10)
        global var
        var = IntVar()
        scale = Scale(window, variable = var ,orient=HORIZONTAL,command = sel, length=300,from_=0, to=255)
        scale.place(x=500, y=380)

        if filename:
            img = cv2.imread(filename)
            global grayscaled
            grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    except: 
        messagebox.showinfo("Alert", "Something went wrong")
        return
        


if __name__ == '__main__':
    window = Tk()
    window.iconbitmap('icon.ico')
    window.title("Threshold")

    btn1 = Button(window, text = "Browse Image",activebackground="#2896F6",command=proceessImage)
    btn1.pack()
    btn1.place(x=100,y=400)

    btn2 = Button(window, text = "Save Image",activebackground="#2896F6",command=saveImage)
    btn2.pack()
    btn2.place(x=200,y=400)
    
    window.geometry("1030x480")
    window.resizable(False, False)
    window.mainloop()
