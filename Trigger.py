import pyscreenshot
import tkinter as tk
from PIL import ImageTk, Image
import time
#screenshot=pyscreenshot.grab(bbox=(10,10,500,500))
#screenshot.show()

#pyscreenshot.grab_to_file('screen.png')
#print('ok')
t_end = time.time() + 2
number = 1

def change_image ():
    number += 1
    window.destroy() 

while(1):

        window = tk.Tk()
        window.title("Test_Data")
        window.geometry("300x300")
        window.configure(background='grey')
        
        path = "/Users/julien/Desktop/PY_PS4/test_data/glaz_scope/" + str(number) + ".jpeg"
        
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(window, image = img)
        
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        window.after(0, change_image )
        window.mainloop()
