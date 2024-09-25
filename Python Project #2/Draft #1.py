# What's My Load? Python Emulator

from tkinter import *
from tkinter.ttk import *

Kbar = 20
Lbar = 45


def openKGWindow():
    # KG Window
    gui = Tk()
    gui.title("Whats My Load? (Kilo Edition)")
    gui.configure(bg='#8b8d91')
    gui.resizable(width=False, height=False)

    # Load Entry
    unit = 'KG'
    label = Label(gui, text=f'Current Load: {Kbar} {unit}')
    label.grid(row=0, column=0, columnspan=5, pady=10, padx=30)

    # All The Different Buttons

    # 25
    def redplate():
        global Kbar
        Kbar += 50
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image1 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Red_plate.png')
    button_red = Button(gui, image=button_image1, command=redplate)
    button_red.grid(row=1, column=0, padx=10, pady=10)

    # 20
    def blueplate():
        global Kbar
        Kbar += 40
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image2 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Blue_plate.png')
    button_blue = Button(gui, image=button_image2, command=blueplate)
    button_blue.grid(row=1, column=1, padx=10, pady=10)

    # 15
    def yellowplate():
        global Kbar
        Kbar += 30
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image3 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Yellow_plate.png')
    button_yellow = Button(gui, image=button_image3, command=yellowplate)
    button_yellow.grid(row=1, column=2, padx=10, pady=10)

    # 10
    def greenplate():
        global Kbar
        Kbar += 20
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image4 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Green_plate.png')
    button_green = Button(gui, image=button_image4, command=greenplate)
    button_green.grid(row=2, column=0, padx=10, pady=10)

    # 5
    def whiteplate():
        global Kbar
        Kbar += 10
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image5 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/White_plate.png')
    button_white = Button(gui, image=button_image5, command=whiteplate)
    button_white.grid(row=2, column=1, padx=10, pady=10)

    # 2.5
    def blackplate():
        global Kbar
        Kbar += 5
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image6 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Black_plate.png')
    button_black = Button(gui, image=button_image6, command=blackplate)
    button_black.grid(row=2, column=2, padx=10, pady=10)

    # 1.25
    def silverplate():
        global Kbar
        Kbar += 2.5
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image7 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Silver_plate.png')
    button_silver = Button(gui, image=button_image7, command=silverplate)
    button_silver.grid(row=3, column=0, padx=10, pady=10)

    # 0.5
    def toddlerplate():
        global Kbar
        Kbar += 1
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image8 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Toddler_plate.png')
    button_toddler = Button(gui, image=button_image8, command=toddlerplate)
    button_toddler.grid(row=3, column=1, padx=10, pady=10)

    # 0.25
    def babyplate():
        global Kbar
        Kbar += 0.5
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image9 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Baby_plate.png')
    button_baby = Button(gui, image=button_image9, command=babyplate)
    button_baby.grid(row=3, column=2, padx=10, pady=10)

    # Clear Bar
    def Kclear():
        global Kbar
        Kbar = 20
        label.config(text=f'Current Load: {Kbar} {unit}')

    button_image10 = PhotoImage(master=gui, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Clear.png')
    button_clear = Button(gui, image=button_image10, command=Kclear)
    button_clear.grid(row=4, column=1, padx=10, pady=10)

    gui.mainloop()


def openLBWindow():
    # KG Window
    hub = Tk()
    hub.title("Whats My Load? (Pound Edition)")
    #bg_image = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Back_Ground.png')
    #bg_label = Label(hub, image=bg_image)
    blue = "#8b8d91"
    hub.configure(bg = blue)
    hub.resizable(width=False, height=False)

    # Load Entry
    unit = 'Lbs'
    label = Label(hub, text=f'Current Load: {Lbar} {unit}')
    label.grid(row=0, column=0, columnspan=5, pady=10, padx=30)

    # All The Different Buttons

    # 45
    def FourFiveplate():
        global Lbar
        Lbar += 90
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image11 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/45_plate.png')
    button_fourfive = Button(hub, image=button_image11, command=FourFiveplate)
    button_fourfive.grid(row=1, column=0, padx=10, pady=10)

    # 35
    def ThreeFiveplate():
        global Lbar
        Lbar += 70
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image12 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/35_plate.png')
    button_threefive = Button(hub, image=button_image12, command=ThreeFiveplate)
    button_threefive.grid(row=1, column=1, padx=10, pady=10)

    # 25
    def TwoFiveplate():
        global Lbar
        Lbar += 50
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image13 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/25_plate.png')
    button_twofive = Button(hub, image=button_image13, command=TwoFiveplate)
    button_twofive.grid(row=1, column=2, padx=10, pady=10)

    # 10
    def Tenplate():
        global Lbar
        Lbar += 20
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image14 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/10_plate.png')
    button_ten = Button(hub, image=button_image14, command=Tenplate)
    button_ten.grid(row=2, column=0, padx=10, pady=10)

    # 5
    def Fiveplate():
        global Lbar
        Lbar += 10
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image15 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/5_plate.png')
    button_five = Button(hub, image=button_image15, command=Fiveplate)
    button_five.grid(row=2, column=1, padx=10, pady=10)

    # 2.5
    def Twoplate():
        global Lbar
        Lbar += 5
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image16 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/2_plate.png')
    button_two = Button(hub, image=button_image16, command=Twoplate)
    button_two.grid(row=2, column=2, padx=10, pady=10)

    # Clear Bar
    def Lclear():
        global Lbar
        Lbar = 45
        label.config(text=f'Current Load: {Lbar} {unit}')

    button_image17 = PhotoImage(master=hub, file='C:/Users/Bruno/OneDrive/Pictures/Screenshots/Clear.png')
    button_clear = Button(hub, image=button_image17, command=Lclear)
    button_clear.grid(row=4, column=1, padx=10, pady=10)

    hub.mainloop()

#Front Screen
master = Tk()

master.geometry('400x550')
master.title("What's My Load?")
master.configure(background='#CAD4DF')

label = Label(master, text= "  Welcome To \"What's My Load?\"  ")
label.pack(pady=30, expand=True)

kgbtn = Button(master, text='Kilo Plates', command=openKGWindow)
kgbtn.pack(ipadx=50, ipady=50, padx=30, pady=40)

poundbtn = Button(master, text='Pound Plates', command=openLBWindow)
poundbtn.pack(ipadx=50, ipady=50, padx=30, pady=40)

#Button Cosmetics
style = Style(master)
style.theme_use('clam')
style.theme_use('alt')
style.configure('TButton',
                background='#DDDBDE', foreground='#3B373B', font=('Comic Sans MS', 16, 'bold'),
                width=75, height=50, borderwidth=3, relief='solid', bordercolor = '#656E77')
style.configure('TLabel',
                background='#DDDBDE', foreground='#3B373B', font=('Comic Sans MS', 16, 'bold'),
                borderwidth=1, relief='solid', bordercolor = '#656E77')


mainloop()

