from tkinter import *
from PIL import Image, ImageTk

class Window(Frame): # It is the base frame and in programming we call the gui output as a frame and not as a window.


    def client_exit(self):
        exit()

    def client_undo(self):
        pass

    def showImg(self):
        load = Image.open('pic.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image = render)
        img.img = render
        img.place(x = 0, y = 0)
        pass

    def showTxt(self):

        text = Label(self, text = 'Hey there good looking!')
        text.pack()
        pass

    def __init__(self, master = None): # You can replace self with anything you want.

        Frame.__init__(self, master)
        self.master = master # This makes it our master(main) frame.
        self.init_window()
        input('Input to exit!')

    def init_window(self): # You can name this function anything, it is made by us.

        varString = StringVar()

        myInput = Entry(root, textvariable=varString).pack()

        varInput = varString.get()

        print(varInput)  # This doe'nt work.

        self.master.title("GUI")
        self.pack(fill = BOTH, expand = 1)
        quitButton = Button(self, text = "Quit!", command = self.client_exit) # You can write client_exit as anything you want, the button just starts a new function.
        quitButton.place(x = 349, y = 259)

        menu = Menu(self.master) # menu can be varMenu
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label = 'Exit', command = self.client_exit)
        menu.add_cascade(label = 'File', menu = file)

        edit = Menu(menu)
        edit.add_command(label = 'Undo', command = self.client_undo)
        edit.add_command(label = 'Show Image', command = self.showImg) # To show image directly use command = self.showImg()
        edit.add_command(label = 'Show Text', command = self.showTxt)
        menu.add_cascade(label = 'Edit', menu = edit)



root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()

