OFFSET_LEFT = 0
OFFSET_TOP = 0
WIDTH_OF_PIXEL = 0
HEIGHT_OF_PIXEL = 0
TOP_LEFT_X = 0
TOP_LEFT_Y = 0

from tkinter import *
from tkinter import filedialog
import sys
from PIL import Image
from PIL import ImageFont, ImageDraw, ImageTk

WIDTH_OF_PIXEL = 100
HEIGHT_OF_PIXEL = 100
TOP_LEFT_X = 0
TOP_LEFT_Y = 0

window=Tk()

selectImage = str(filedialog.askopenfilenames())[2:-3]
print(selectImage)
selectImage2 = PhotoImage(master=window, file=selectImage)
im = Image.open(selectImage)
width, height = im.size

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 24)
num = 0
coordList = "1"
def imageExport():
    global im
    num = 0
    coordList= str(coordfield.get()).split(",")
    TOP_LEFT_X = int(coordList[0])
    TOP_LEFT_Y = int(coordList[1])
    print(TOP_LEFT_X)
    print(TOP_LEFT_Y)
    for i in range(OFFSET_LEFT, width, WIDTH_OF_PIXEL):
        for j in range(OFFSET_TOP, height, HEIGHT_OF_PIXEL):
            num += 1
            draw.line(((i, j), (i + WIDTH_OF_PIXEL, j)), fill="black", width=1)
            draw.line(((i, j), (i, j + HEIGHT_OF_PIXEL)), fill="black", width=1)
            draw.text((i + 3, j + 3),
                      f"Nr.{num}\nx{TOP_LEFT_X + (i // WIDTH_OF_PIXEL)}\ny{(TOP_LEFT_Y + j // HEIGHT_OF_PIXEL)}",
                      font=font, fill=(46, 204, 113))

    im.save(selectImage[0:-4] + "output.png")
    im.show()
    sys.exit()

coord=Label(window, text="Coordinates x,y", fg='Black', font=("Helvetica", 9))
coord.place(x=15, y=40)

coordfield=Entry(window, text="x coord", bd=5)
coordfield.place(x=15, y=60)
coordfield.focus_force()


button2=Button(window, text="Export Image", fg='black',command=lambda: imageExport())
button2.place(x=40, y=140)
#window.overrideredirect(True)
window.title('Coordinator')
window.geometry("160x200+10+20")
window.mainloop()





