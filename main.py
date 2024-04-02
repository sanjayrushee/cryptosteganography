import tkinter as tk 
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Convert encoding data into 8-bit binary form using ASCII value of characters
def genData(data):
    newd = []
    for i in data:
        newd.append(format(i, '08b'))
    return newd

# Pixels are modified according to the 8-bit binary data and finally returned
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    for i in range(lendata):
        pix = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

def encode():
    img_path = filedialog.askopenfilename(title="Select Image")
    image = Image.open(img_path, 'r')

    file_path = filedialog.askopenfilename(title="Select File")
    file = open(file_path, 'rb')
    data = file.read()

    newimg = image.copy()
    encode_enc(newimg, data)
    new_img_name = filedialog.asksaveasfilename(title="Save Image As", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"),("All files", "*.*")))
    newimg.save(new_img_name)
    #entry_encode_data.delete(0, tk.END)  # Clear the encoded text entry


def decode():
    img_path = filedialog.askopenfilename(title="Select Image")
    image = Image.open(img_path, 'r')
    data = []
    imgdata = iter(image.getdata())
    while True:
        pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]]
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        
        data += int(binstr, 2).to_bytes(1, byteorder='big')
        if (pixels[-1] % 2 != 0):
            break
    #decoded_label.config(text="Decoded Data: " + data)
    file_path = filedialog.asksaveasfilename(title="Save File As", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"),("All files", "*.*")))
    file = open(file_path, 'wb')
    data = bytearray(data)
    file.write(data)

decode()
'''root = tk.Tk()
root.title("Steganography")
root.geometry("1360x710")
root.config(bg="#F0F0F0")

bg_image = PhotoImage(file="./templates/background.png")
background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

encodebtn = PhotoImage(file="./templates/encode.png")
button_encode = tk.Button(image=encodebtn, command=encode, bd=0, bg="#AEE2BA", activebackground="#AEE2BA")
button_encode.place(x=533, y=300)

decodebtn = PhotoImage(file="./templates/decode.png")
button_decode = tk.Button(image=decodebtn, command=decode,bd=0, bg="#AEE2BA", activebackground="#AEE2BA")
button_decode.place(x=535, y=406)

decoded_label = tk.Label(root, text="", bg="#AEE2BA",font=("Helvetica", 14))
decoded_label.place(x=469, y=512)

entry_encode_data = tk.Entry(root,font=("Helvetica", 12))
entry_encode_data.place(x=390, y=204, width=620, height=40)

root.mainloop()'''
