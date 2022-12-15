"""
Program: OnlinePhones.py
Name: Alejandro Munoz Garcia
Course: SDEV-140
About: Fake app that lets you order a phone online, but its a scam and causes pop ups
"""
# imports tkinter and random
from tkinter import *
from random import randint

# Program class
class Program:
    def __init__(self, master):
        self.master = master

        # color vars
        self.bgColor = "#14213d"
        self.fontColor = "#e5e5e5"

        # vars for colors, and phone, name, price, color, storage, tax for phone picked
        # count var for colors
        self.pickPrice = 0
        self.pickName = ""
        self.pickColor = ""
        self.pickStorage = "128"
        self.count = 0
        self.tax = 0.07

        # Window
        self.master.geometry("+0+0")
        self.master.title("Online Phones")
        self.master["bg"] = self.bgColor

        # Log in Widgets
        # log in title
        self.logInTitleLabel = Label(master, text="Online Phones", bg=self.bgColor, font=("Times", 40, "bold"))
        self.logInTitleLabel.config(foreground=self.fontColor)
        self.logInTitleLabel.grid(row=0, column=0)
        # log in label
        self.entryLabel = Label(master,text="Enter Name:",foreground=self.fontColor,bg=self.bgColor, font=("Times", 12))
        self.entryLabel.grid(column=0,row=1,padx=50)
        # log in entry
        self.name = StringVar()
        self.nameEntry = Entry(master,textvariable=self.name,foreground="#000000",bg=self.fontColor, font=("Times", 18))
        self.nameEntry.grid(column=0,row=2)
        # Log in buttons
        self.logInBtn = Button(master, text="Enter", bg=self.fontColor, font=("Times", 18), command=self.mainPage)
        self.logInBtn.config(foreground=self.bgColor)
        self.logInBtn.grid(row=3, column=0,pady=10)


        # Main Page Widgets
        # Welcome Label
        self.mainWelcomeLabel = Label(master, text="Welcome, what are buying?", bg=self.bgColor, font=("Times", 20))
        self.mainWelcomeLabel.config(foreground=self.fontColor)
        self.mainWelcomeLabel.grid_forget()
        # exit btn
        self.ExitBtn = Button(master,text="EXIT",bg=self.fontColor,foreground=self.bgColor,font=("Times",13),command=self.master.quit)
        self.ExitBtn.grid_forget()
        # s22 Ultra
        self.mainS22Ultra = Label(master, text="Samsung 22 Ultra", bg=self.bgColor, font=("Times", 13))
        self.mainS22Ultra.config(foreground=self.fontColor)
        self.mainS22Ultra.grid_forget()
        # img
        # picture source: https://www.samsung.com/us/
        self.s22U_img = PhotoImage(file="s22ultra.png")
        self.s22ULabel_img = Label(master, image=self.s22U_img)
        self.s22ULabel_img.config(bg=self.bgColor)
        self.s22ULabel_img.grid_forget()
        # btn & price
        self.s22UPrice_Label = Label(master, text="$1199.99", bg=self.bgColor, font=("Times", 13))
        self.s22UPrice_Label.config(foreground=self.fontColor)
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn = Button(master, text="See More", bg=self.fontColor, font=("Times", 13), command=self.s22UMore)
        self.s22U_btn.config(foreground=self.bgColor)
        self.s22U_btn.grid_forget()

        # s22 plus
        self.mainS22Plus = Label(master, text="Samsung 22 Plus", bg=self.bgColor, font=("Times", 13))
        self.mainS22Plus.config(foreground=self.fontColor)
        self.mainS22Plus.grid_forget()
        # img
        # picture source: https://www.samsung.com/us/
        self.s22P_img = PhotoImage(file="s22plus.png")
        self.s22PLabel_img = Label(master, image=self.s22P_img)
        self.s22PLabel_img.config(bg=self.bgColor)
        self.s22PLabel_img.grid_forget()
        # btn & price
        self.s22Price_Label = Label(master, text="$999.99", bg=self.bgColor, font=("Times", 13))
        self.s22Price_Label.config(foreground=self.fontColor)
        self.s22Price_Label.grid_forget()
        self.s22_btn = Button(master, text="See More", bg=self.fontColor, font=("Times", 13),command=self.s22PMore)
        self.s22_btn.config(foreground=self.bgColor)
        self.s22_btn.grid_forget()

        # pixel 7 pro
        self.mainPixel7Pro = Label(master, text="Pixel 7 Pro", bg=self.bgColor, font=("Times", 13))
        self.mainPixel7Pro.config(foreground=self.fontColor)
        self.mainPixel7Pro.grid_forget()
        # img
        # picture source: https://store.google.com/?hl=en-US
        self.pixel7P_img = PhotoImage(file="pixel7pro.png")
        self.pixel7PLabel_img = Label(master, image=self.pixel7P_img)
        self.pixel7PLabel_img.config(bg=self.bgColor)
        self.pixel7PLabel_img.grid_forget()
        # btn & price
        self.pixel7ProPrice_Label = Label(master, text="$899.99", bg=self.bgColor, font=("Times", 13))
        self.pixel7ProPrice_Label.config(foreground=self.fontColor)
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn = Button(master, text="See more", bg=self.fontColor, font=("Times", 13),command=self.Pixel7ProMore)
        self.pixel7Pro_btn.config(foreground=self.bgColor)
        self.pixel7Pro_btn.grid_forget()

        # pixel 7
        self.mainPixel7 = Label(master, text="Pixel 7", bg=self.bgColor, font=("Times", 13))
        self.mainPixel7.config(foreground=self.fontColor)
        self.mainPixel7.grid_forget()
        # img
        # picture source: https://store.google.com/?hl=en-US
        self.pixel7_img = PhotoImage(file="pixel7.png")
        self.pixel7Label_img = Label(master, image=self.pixel7_img)
        self.pixel7Label_img.config(bg=self.bgColor)
        self.pixel7Label_img.grid_forget()
        # btn & price
        self.pixel7Price_Label = Label(master, text="$599.99", bg=self.bgColor, font=("Times", 13))
        self.pixel7Price_Label.config(foreground=self.fontColor)
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn = Button(master, text="See more", bg=self.fontColor, font=("Times", 13),command=self.Pixel7More)
        self.pixel7_btn.config(foreground=self.bgColor)
        self.pixel7_btn.grid_forget()

        # iphone 14 pro max
        self.mainI14ProMax = Label(master, text="iPhone 14 Pro Max", bg=self.bgColor, font=("Times", 13))
        self.mainI14ProMax.config(foreground=self.fontColor)
        self.mainI14ProMax.grid_forget()
        # img
        # picture source: https://www.verizon.com/
        self.i14PM_img = PhotoImage(file="iphone14promax.png")
        self.i14PMLabel_img = Label(master, image=self.i14PM_img)
        self.i14PMLabel_img.config(bg=self.bgColor)
        self.i14PMLabel_img.grid_forget()
        # btn & price
        self.i14PMprice_Label = Label(master, text="$1099.99", bg=self.bgColor, font=("Times", 13))
        self.i14PMprice_Label.config(foreground=self.fontColor)
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn = Button(master, text="See more", bg=self.fontColor, font=("Times", 13),command=self.i14ProMaxMore)
        self.i14PM_btn.config(foreground=self.bgColor)
        self.i14PM_btn.grid_forget()

        # iphone 14 pro
        self.mainI14Pro = Label(master, text="iPhone 14 Pro", bg=self.bgColor, font=("Times", 13))
        self.mainI14Pro.config(foreground=self.fontColor)
        self.mainI14Pro.grid_forget()
        # img
        # picture source: https://www.t-mobile.com/
        self.i14P_img = PhotoImage(file="iphone14pro.png")
        self.i14PLabel_img = Label(master, image=self.i14P_img)
        self.i14PLabel_img.config(bg=self.bgColor)
        self.i14PLabel_img.grid_forget()
        # btn & price
        self.i14Price_Label = Label(master, text="$999.99", bg=self.bgColor, font=("Times", 13))
        self.i14Price_Label.config(foreground=self.fontColor)
        self.i14Price_Label.grid_forget()
        self.i14P_btn = Button(master, text="See more", bg=self.fontColor, font=("Times", 13),command=self.i14ProMore)
        self.i14P_btn.config(foreground=self.bgColor)
        self.i14P_btn.grid_forget()

        # See more page
        # back btn
        self.backbtn = Button(master, text="Back", command=self.mainPage)
        self.backbtn.grid_forget()
        # name label
        self.phoneName = Label(master,text="phone")
        self.phoneName.grid_forget()
        # specs: screen size, storage, camera, os
        self.screen = Label(master,text="Screen Size: ")
        self.screen.grid_forget()
        self.storage = Label(master,text="Storage Size: ")
        self.storage.grid_forget()
        self.camera = Label(master,text="Main Camera: ")
        self.camera.grid_forget()
        self.os = Label(master,text="Operating System: ")
        self.os.grid_forget()
        # radio color buttons
        self.var = StringVar()
        self.colorBlack = Radiobutton(master,text="Color: Black",variable=self.var,value="Black",command=self.BLCK)
        self.colorBlack.grid_forget()
        self.colorBlue = Radiobutton(master,text="Color: Blue",variable=self.var,value="Blue",command=self.BLUE)
        self.colorBlue.grid_forget()
        self.colorPurple = Radiobutton(master,text="Color: Purple",variable=self.var,value="Purple",command=self.PRPLE)
        self.colorPurple.grid_forget()
        self.colorRed = Radiobutton(master,text="Color: Red",variable=self.var,value="Red",command=self.RED)
        self.colorRed.grid_forget()
        # buy btn
        self.buyBtn = Button(master,text="Buy",command=self.BuyPage)
        self.buyBtn.grid_forget()
    # sets count into color num
    def BLCK(self):
        self.pickColor = "BLCK"
        return self.pickColor
    def BLUE(self):
        self.pickColor = "BLUE"
        return self.pickColor
    def PRPLE(self):
        self.pickColor = "PRPLE"
        return self.pickColor
    def RED(self):
        self.pickColor = "RED"
        return self.pickColor
    # pages
    # main
    def mainPage(self):
        """Changes the login page to the main page"""
        # destroys login widgets and resizes window
        self.name_Input = self.name.get()

        # log in window
        self.logInBtn.grid_forget()
        self.logInTitleLabel.grid_forget()
        self.entryLabel.grid_forget()
        self.nameEntry.grid_forget()
        # about btn
        self.backbtn.grid_forget()
        # phone name
        self.phoneName.grid_forget()
        # pic
        self.s22ULabel_img.grid_forget()
        # spec
        self.screen.grid_forget()
        self.storage.grid_forget()
        self.camera.grid_forget()
        self.os.grid_forget()
        # radio btns
        self.colorBlack.grid_forget()
        self.colorBlue.grid_forget()
        self.colorPurple.grid_forget()
        self.colorRed.grid_forget()
        # but btn
        self.buyBtn.grid_forget()

        # makes main widgets appear
        self.mainWelcomeLabel.config(text="Welcome "+self.name_Input+",\nwhat are you buying?")
        self.mainWelcomeLabel.grid(column=0,row=4)
        # s22 ultra
        self.mainS22Ultra.grid(column=1, row=1, columnspan=1, rowspan=1, padx=0, sticky=W)
        self.s22ULabel_img.grid(column=1, row=2, columnspan=1, rowspan=1, padx=0, sticky=W)
        self.s22UPrice_Label.grid(column=1, row=3, columnspan=1, rowspan=1, padx=0, sticky=W)
        self.s22U_btn.grid(column=1, row=4, columnspan=1, rowspan=1, padx=0, sticky=W)
        # s22 plus
        self.mainS22Plus.grid(column=2, row=1, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.s22PLabel_img.grid(column=2, row=2, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.s22Price_Label.grid(column=2, row=3, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.s22_btn.grid(column=2, row=4, columnspan=1, rowspan=1, padx=25, sticky=W)
        # pixel 7 pro
        self.mainPixel7Pro.grid(column=3, row=1, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.pixel7PLabel_img.grid(column=3, row=2, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.pixel7ProPrice_Label.grid(column=3, row=3, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.pixel7Pro_btn.grid(column=3, row=4, columnspan=1, rowspan=1, padx=25, sticky=W)
        # pixel 7
        self.mainPixel7.grid(column=1, row=5, columnspan=1, rowspan=1, padx=0, sticky=W)
        self.pixel7Label_img.grid(column=1, row=6, columnspan=1, rowspan=1, padx=0, sticky=W)
        self.pixel7Price_Label.grid(column=1, row=7, columnspan=1, rowspan=1, padx=0, sticky=W)
        self.pixel7_btn.grid(column=1,row=8, columnspan=1, rowspan=1, padx=0, sticky=W)
        # iphone 14 pro max
        self.mainI14ProMax.grid(column=2, row=5, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.i14PMLabel_img.grid(column=2, row=6, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.i14PMprice_Label.grid(column=2, row=7, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.i14PM_btn.grid(column=2, row=8, columnspan=1, rowspan=1, padx=25, sticky=W)
        # iphone 14 pro
        self.mainI14Pro.grid(column=3, row=5, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.i14PLabel_img.grid(column=3, row=6, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.i14Price_Label.grid(column=3, row=7, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.i14P_btn.grid(column=3, row=8, columnspan=1, rowspan=1, padx=25, sticky=W)
        self.ExitBtn.grid(column=0,row=9,sticky=W)
    # "more" pages
    def s22UMore(self):
        """Samsung 22 Ultra More Info"""
        self.pickPrice = 1199.99
        self.pickName = "S22Ultra"
        # destroys main widgets
        self.mainWelcomeLabel.grid_forget()
        # s22 ultra
        self.mainS22Ultra.grid_forget()
        self.s22ULabel_img.grid_forget()
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn.grid_forget()
        # s22 plus
        self.mainS22Plus.grid_forget()
        self.s22PLabel_img.grid_forget()
        self.s22Price_Label.grid_forget()
        self.s22_btn.grid_forget()
        # pixel 7 pro
        self.mainPixel7Pro.grid_forget()
        self.pixel7PLabel_img.grid_forget()
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn.grid_forget()
        # pixel 7
        self.mainPixel7.grid_forget()
        self.pixel7Label_img.grid_forget()
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn.grid_forget()
        # iphone 14 pro max
        self.mainI14ProMax.grid_forget()
        self.i14PMLabel_img.grid_forget()
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn.grid_forget()
        # iphone 14 pro
        self.mainI14Pro.grid_forget()
        self.i14PLabel_img.grid_forget()
        self.i14Price_Label.grid_forget()
        self.i14P_btn.grid_forget()

        # widgets
        # back btn
        self.backbtn.grid(column=0,row=8)
        self.backbtn.config(bg="#e5e5e5",foreground="#14213d",font=("Times",13))
        # phone name
        self.phoneName.config(text="Samsung S22 Ultra",bg="#14213d",foreground="#e5e5e5",font=("Times",13))
        self.phoneName.grid(column=0,row=0)
        # phone pic
        self.s22ULabel_img.grid(column=0,row=1)
        # specs
        self.screen.config(text="Screen Size: 3080 x 1440 pixels",bg="#14213d",foreground="#e5e5e5",font=("Times",13))
        self.screen.grid(column=0,row=2)
        self.storage.config(text="Storage Size: 128 GB",bg="#14213d",foreground="#e5e5e5",font=("Times",13))
        self.storage.grid(column=0,row=3)
        self.camera.config(text="Main Camera: 108 MP",bg="#14213d",foreground="#e5e5e5",font=("Times",13))
        self.camera.grid(column=0,row=4)
        self.os.config(text="Operating System: Android",bg="#14213d",foreground="#e5e5e5",font=("Times",13))
        self.os.grid(column=0,row=5)
        # radio btns
        self.colorBlack.config(bg="#14213d",foreground="#a1a1a1",font=("Times",13))
        self.colorBlack.grid(column=0,row=6)
        self.colorBlue.config(bg="#14213d",foreground="#a1a1a1",font=("Times",13))
        self.colorBlue.grid(column=0,row=7)
        self.colorPurple.config(bg="#14213d",foreground="#a1a1a1",font=("Times",13))
        self.colorPurple.grid(column=1,row=6)
        self.colorRed.config(bg="#14213d",foreground="#a1a1a1",font=("Times",13))
        self.colorRed.grid(column=1,row=7)
        # buy
        self.buyBtn.config(bg="#e5e5e5",foreground="#14213d",font=("Times",13))
        self.buyBtn.grid(column=1,row=8)
    def s22PMore(self):
        """Samsung S22 Plus More Info"""
        self.pickPrice = 999.99
        self.pickName = "S22Plus"
        # destroys main widgets
        self.mainWelcomeLabel.grid_forget()
        # s22 ultra
        self.mainS22Ultra.grid_forget()
        self.s22ULabel_img.grid_forget()
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn.grid_forget()
        # s22 plus
        self.mainS22Plus.grid_forget()
        self.s22PLabel_img.grid_forget()
        self.s22Price_Label.grid_forget()
        self.s22_btn.grid_forget()
        # pixel 7 pro
        self.mainPixel7Pro.grid_forget()
        self.pixel7PLabel_img.grid_forget()
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn.grid_forget()
        # pixel 7
        self.mainPixel7.grid_forget()
        self.pixel7Label_img.grid_forget()
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn.grid_forget()
        # iphone 14 pro max
        self.mainI14ProMax.grid_forget()
        self.i14PMLabel_img.grid_forget()
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn.grid_forget()
        # iphone 14 pro
        self.mainI14Pro.grid_forget()
        self.i14PLabel_img.grid_forget()
        self.i14Price_Label.grid_forget()
        self.i14P_btn.grid_forget()

        # widgets
        # back btn
        self.backbtn.grid(column=0, row=8)
        self.backbtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        # phone name
        self.phoneName.config(text="Samsung 22 Plus", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.phoneName.grid(column=0, row=0)
        # phone pic
        self.s22PLabel_img.grid(column=0, row=1)
        # specs
        self.screen.config(text="Screen Size: 2340 x 1080 pixels", bg="#14213d", foreground="#e5e5e5",
                           font=("Times", 13))
        self.screen.grid(column=0, row=2)
        self.storage.config(text="Storage Size: 128 GB", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.storage.grid(column=0, row=3)
        self.camera.config(text="Main Camera: 50 MP", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.camera.grid(column=0, row=4)
        self.os.config(text="Operating System: Android", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.os.grid(column=0, row=5)
        # radio btns
        self.colorBlack.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlack.grid(column=0, row=6)
        self.colorBlue.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlue.grid(column=0, row=7)
        self.colorPurple.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorPurple.grid(column=1, row=6)
        self.colorRed.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorRed.grid(column=1, row=7)
        # buy
        self.buyBtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        self.buyBtn.grid(column=1, row=8)
    def Pixel7ProMore(self):
        """Pixel 7 Pro More Info"""
        self.pickPrice = 899.99
        self.pickName = "P7Pro"
        # destroys main widgets
        self.mainWelcomeLabel.grid_forget()
        # s22 ultra
        self.mainS22Ultra.grid_forget()
        self.s22ULabel_img.grid_forget()
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn.grid_forget()
        # s22 plus
        self.mainS22Plus.grid_forget()
        self.s22PLabel_img.grid_forget()
        self.s22Price_Label.grid_forget()
        self.s22_btn.grid_forget()
        # pixel 7 pro
        self.mainPixel7Pro.grid_forget()
        self.pixel7PLabel_img.grid_forget()
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn.grid_forget()
        # pixel 7
        self.mainPixel7.grid_forget()
        self.pixel7Label_img.grid_forget()
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn.grid_forget()
        # iphone 14 pro max
        self.mainI14ProMax.grid_forget()
        self.i14PMLabel_img.grid_forget()
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn.grid_forget()
        # iphone 14 pro
        self.mainI14Pro.grid_forget()
        self.i14PLabel_img.grid_forget()
        self.i14Price_Label.grid_forget()
        self.i14P_btn.grid_forget()

        # widgets
        # back btn
        self.backbtn.grid(column=0, row=8)
        self.backbtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        # phone name
        self.phoneName.config(text="Pixel 7 Pro", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.phoneName.grid(column=0, row=0)
        # phone pic
        self.pixel7PLabel_img.grid(column=0, row=1)
        # specs
        self.screen.config(text="Screen Size: 3120 x 1440 pixels", bg="#14213d", foreground="#e5e5e5",
                           font=("Times", 13))
        self.screen.grid(column=0, row=2)
        self.storage.config(text="Storage Size: 128 GB", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.storage.grid(column=0, row=3)
        self.camera.config(text="Main Camera: 50 MP", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.camera.grid(column=0, row=4)
        self.os.config(text="Operating System: Android", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.os.grid(column=0, row=5)
        # radio btns
        self.colorBlack.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlack.grid(column=0, row=6)
        self.colorBlue.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlue.grid(column=0, row=7)
        self.colorPurple.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorPurple.grid(column=1, row=6)
        self.colorRed.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorRed.grid(column=1, row=7)
        # buy
        self.buyBtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        self.buyBtn.grid(column=1, row=8)
    def Pixel7More(self):
        """Pixel 7 More Info"""
        self.pickPrice = 599.99
        self.pickName = "P7"
        # destroys main widgets
        self.mainWelcomeLabel.grid_forget()
        # s22 ultra
        self.mainS22Ultra.grid_forget()
        self.s22ULabel_img.grid_forget()
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn.grid_forget()
        # s22 plus
        self.mainS22Plus.grid_forget()
        self.s22PLabel_img.grid_forget()
        self.s22Price_Label.grid_forget()
        self.s22_btn.grid_forget()
        # pixel 7 pro
        self.mainPixel7Pro.grid_forget()
        self.pixel7PLabel_img.grid_forget()
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn.grid_forget()
        # pixel 7
        self.mainPixel7.grid_forget()
        self.pixel7Label_img.grid_forget()
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn.grid_forget()
        # iphone 14 pro max
        self.mainI14ProMax.grid_forget()
        self.i14PMLabel_img.grid_forget()
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn.grid_forget()
        # iphone 14 pro
        self.mainI14Pro.grid_forget()
        self.i14PLabel_img.grid_forget()
        self.i14Price_Label.grid_forget()
        self.i14P_btn.grid_forget()

        # widgets
        # back btn
        self.backbtn.grid(column=0, row=8)
        self.backbtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        # phone name
        self.phoneName.config(text="Pixel 7", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.phoneName.grid(column=0, row=0)
        # phone pic
        self.pixel7Label_img.grid(column=0, row=1)
        # specs
        self.screen.config(text="Screen Size: 2400 x 1080 pixels", bg="#14213d", foreground="#e5e5e5",
                           font=("Times", 13))
        self.screen.grid(column=0, row=2)
        self.storage.config(text="Storage Size: 128 GB", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.storage.grid(column=0, row=3)
        self.camera.config(text="Main Camera: 50 MP", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.camera.grid(column=0, row=4)
        self.os.config(text="Operating System: Android", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.os.grid(column=0, row=5)
        # radio btns
        self.colorBlack.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlack.grid(column=0, row=6)
        self.colorBlue.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlue.grid(column=0, row=7)
        self.colorPurple.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorPurple.grid(column=1, row=6)
        self.colorRed.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorRed.grid(column=1, row=7)
        # buy
        self.buyBtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        self.buyBtn.grid(column=1, row=8)
    def i14ProMaxMore(self):
        """iPhone 14 Pro Max More Info"""
        self.pickPrice = 1099.99
        self.pickName = "i14PM"
        # destroys main widgets
        self.mainWelcomeLabel.grid_forget()
        # s22 ultra
        self.mainS22Ultra.grid_forget()
        self.s22ULabel_img.grid_forget()
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn.grid_forget()
        # s22 plus
        self.mainS22Plus.grid_forget()
        self.s22PLabel_img.grid_forget()
        self.s22Price_Label.grid_forget()
        self.s22_btn.grid_forget()
        # pixel 7 pro
        self.mainPixel7Pro.grid_forget()
        self.pixel7PLabel_img.grid_forget()
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn.grid_forget()
        # pixel 7
        self.mainPixel7.grid_forget()
        self.pixel7Label_img.grid_forget()
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn.grid_forget()
        # iphone 14 pro max
        self.mainI14ProMax.grid_forget()
        self.i14PMLabel_img.grid_forget()
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn.grid_forget()
        # iphone 14 pro
        self.mainI14Pro.grid_forget()
        self.i14PLabel_img.grid_forget()
        self.i14Price_Label.grid_forget()
        self.i14P_btn.grid_forget()

        # widgets
        # back btn
        self.backbtn.grid(column=0, row=8)
        self.backbtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        # phone name
        self.phoneName.config(text="iPhone 14 Pro Max", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.phoneName.grid(column=0, row=0)
        # phone pic
        self.i14PMLabel_img.grid(column=0, row=1)
        # specs
        self.screen.config(text="Screen Size: 2796 x 1290 pixels", bg="#14213d", foreground="#e5e5e5",
                           font=("Times", 13))
        self.screen.grid(column=0, row=2)
        self.storage.config(text="Storage Size: 128 GB", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.storage.grid(column=0, row=3)
        self.camera.config(text="Main Camera: 48 MP", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.camera.grid(column=0, row=4)
        self.os.config(text="Operating System: IOS", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.os.grid(column=0, row=5)
        # radio btns
        self.colorBlack.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlack.grid(column=0, row=6)
        self.colorBlue.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlue.grid(column=0, row=7)
        self.colorPurple.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorPurple.grid(column=1, row=6)
        self.colorRed.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorRed.grid(column=1, row=7)
        # buy
        self.buyBtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        self.buyBtn.grid(column=1, row=8)
    def i14ProMore(self):
        """iPhone 14 Pro More Info"""
        self.pickPrice = 999.99
        self.pickName = "i14P"
        # destroys main widgets
        self.mainWelcomeLabel.grid_forget()
        # s22 ultra
        self.mainS22Ultra.grid_forget()
        self.s22ULabel_img.grid_forget()
        self.s22UPrice_Label.grid_forget()
        self.s22U_btn.grid_forget()
        # s22 plus
        self.mainS22Plus.grid_forget()
        self.s22PLabel_img.grid_forget()
        self.s22Price_Label.grid_forget()
        self.s22_btn.grid_forget()
        # pixel 7 pro
        self.mainPixel7Pro.grid_forget()
        self.pixel7PLabel_img.grid_forget()
        self.pixel7ProPrice_Label.grid_forget()
        self.pixel7Pro_btn.grid_forget()
        # pixel 7
        self.mainPixel7.grid_forget()
        self.pixel7Label_img.grid_forget()
        self.pixel7Price_Label.grid_forget()
        self.pixel7_btn.grid_forget()
        # iphone 14 pro max
        self.mainI14ProMax.grid_forget()
        self.i14PMLabel_img.grid_forget()
        self.i14PMprice_Label.grid_forget()
        self.i14PM_btn.grid_forget()
        # iphone 14 pro
        self.mainI14Pro.grid_forget()
        self.i14PLabel_img.grid_forget()
        self.i14Price_Label.grid_forget()
        self.i14P_btn.grid_forget()

        # widgets
        # back btn
        self.backbtn.grid(column=0, row=8)
        self.backbtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        # phone name
        self.phoneName.config(text="iPhone 14 Pro", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.phoneName.grid(column=0, row=0)
        # phone pic
        self.i14PLabel_img.grid(column=0, row=1)
        # specs
        self.screen.config(text="Screen Size: 2556 x 1179 pixels", bg="#14213d", foreground="#e5e5e5",
                           font=("Times", 13))
        self.screen.grid(column=0, row=2)
        self.storage.config(text="Storage Size: 128 GB", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.storage.grid(column=0, row=3)
        self.camera.config(text="Main Camera: 48 MP", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.camera.grid(column=0, row=4)
        self.os.config(text="Operating System: IOS", bg="#14213d", foreground="#e5e5e5", font=("Times", 13))
        self.os.grid(column=0, row=5)
        # radio btns
        self.colorBlack.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlack.grid(column=0, row=6)
        self.colorBlue.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorBlue.grid(column=0, row=7)
        self.colorPurple.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorPurple.grid(column=1, row=6)
        self.colorRed.config(bg="#14213d", foreground="#a1a1a1", font=("Times", 13))
        self.colorRed.grid(column=1, row=7)
        # buy
        self.buyBtn.config(bg="#e5e5e5", foreground="#14213d", font=("Times", 13))
        self.buyBtn.grid(column=1, row=8)
    # buy page
    def BuyPage(self):
        """Buying Page Where Users get to add credit card stuff, email, and address"""
        # set up window
        self.buy = Tk()
        self.buy.geometry("+200+50")
        self.buy["bg"] = self.bgColor
        self.buy.title("Shopping Cart")

        # calculations
        TaxCal = (self.pickPrice*self.tax)
        TaxAmt = format(TaxCal,".2f")
        TotalAmt = float(TaxAmt)+self.pickPrice+50

        # reciepts
        # order details
        OrderDetails = Label(self.buy,text="Order Details",bg=self.bgColor,foreground=self.fontColor,font=("Times",20))
        OrderDetails.grid(column=0,row=0,sticky=W)
        # order name
        OrderName = Label(self.buy, text=self.pickName+self.pickColor+self.pickStorage, bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderName.grid(column=0, row=1,sticky=W)
        # order price
        OrderPrice = Label(self.buy,text="$"+str(self.pickPrice),bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderPrice.grid(column=1,row=1,sticky=E)
        # order fee
        OrderFee = Label(self.buy,text="Online Fee",bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderFee.grid(column=0,row=2,sticky=W)
        # order fee amt
        OrderFeeAmt = Label(self.buy,text="$50.00",bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderFeeAmt.grid(column=1,row=2,sticky=E)
        # order tax
        OrderTax = Label(self.buy,text="Tax",bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderTax.grid(column=0,row=3,sticky=W)
        # order tax amt
        OrderTaxAmt = Label(self.buy,text="$"+TaxAmt,bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderTaxAmt.grid(column=1,row=3,sticky=E)
        # order total
        OrderTotal = Label(self.buy,text="TOTAL",bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderTotal.grid(column=0,row=4,sticky=W)
        # order amt
        OrderAmt = Label(self.buy,text="$"+str(TotalAmt),bg=self.bgColor, foreground=self.fontColor,font=("Times", 13))
        OrderAmt.grid(column=1,row=4,sticky=E)

        # shipping info
        # name
        ShipName = Entry(self.buy,bg=self.fontColor, foreground=self.bgColor,font=("Times", 10))
        ShipName.insert(0,"Name")
        ShipName.grid(column=0,row=5,pady=10,sticky=W)
        # last name
        ShipLastName = Entry(self.buy, bg=self.fontColor, foreground=self.bgColor, font=("Times", 10))
        ShipLastName.insert(0, "Last Name")
        ShipLastName.grid(column=0, row=6, pady=10,sticky=W)
        # address
        ShipAddress = Entry(self.buy,bg=self.fontColor, foreground=self.bgColor,font=("Times", 10))
        ShipAddress.insert(0,"Address")
        ShipAddress.grid(column=0,row=7,pady=10,sticky=W)
        # email
        ShipEmail = Entry(self.buy, bg=self.fontColor, foreground=self.bgColor, font=("Times", 10))
        ShipEmail.insert(0, "Email")
        ShipEmail.grid(column=0, row=8, pady=10,sticky=W)
        # credit card name
        ShipCreditName = Entry(self.buy, bg=self.fontColor, foreground=self.bgColor, font=("Times", 10))
        ShipCreditName.insert(0, "Name On Credit Card")
        ShipCreditName.grid(column=1, row=5, pady=10, sticky=E)
        # credit card num
        ShipCreditNum = Entry(self.buy, bg=self.fontColor, foreground=self.bgColor, font=("Times", 10))
        ShipCreditNum.insert(0, "Credit Card Number")
        ShipCreditNum.grid(column=1, row=6, pady=10, sticky=E)
        # credit card exp
        ShipCreditExp = Entry(self.buy, bg=self.fontColor, foreground=self.bgColor, font=("Times", 10))
        ShipCreditExp.insert(0, "Expiration month/year")
        ShipCreditExp.grid(column=1, row=7, pady=10, sticky=E)
        # credit cvv
        ShipCreditCVV = Entry(self.buy, bg=self.fontColor, foreground=self.bgColor, font=("Times", 10))
        ShipCreditCVV.insert(0, "CVV")
        ShipCreditCVV.grid(column=1, row=8, pady=10, sticky=E)

        # btns
        BuyBack = Button(self.buy,text="Back", bg=self.fontColor, foreground=self.bgColor, font=("Times", 10),command=lambda :self.buy.destroy())
        BuyBack.grid(column=0,row=9,pady=10)

        NextBtn = Button(self.buy,text="Next",bg=self.fontColor, foreground=self.bgColor, font=("Times", 10),command=self.HACKED)
        NextBtn.grid(column=1,row=9,pady=10)
    def HACKED(self):
        """Hacked function that enables the pop ups"""
        self.buy.destroy()
        for i in range(7):
            win = Tk()
            win["bg"] = self.bgColor
            btn1 = Button(win, text="CLICK HERE", font=("Times", 10),bg=self.fontColor, foreground=self.bgColor ,command=win.destroy).pack(anchor="center")
            label1 = Label(win, text="^ FREE MONEY ^",bg=self.bgColor,foreground=self.fontColor,font=("Times", 10)).pack(anchor="center")
            win.geometry("+{}+{}".format(
                randint(0, 1000),  # x position
                randint(0, 500)  # y position
            ))

        for i in range(7):
            win2 = Tk()
            win2["bg"] = self.bgColor
            btn2 = Button(win2, text="CLICK HERE", font=("Times", 10), bg=self.fontColor, foreground=self.bgColor,command=win2.destroy).pack(anchor="center")
            label2 = Label(win2, text="^FIND FREE PHONES NEAR YOU ;)^",bg=self.bgColor,foreground=self.fontColor,font=("Times", 10)).pack(anchor="center")
            win2.geometry("+{}+{}".format(
                randint(0, 1000),  # x position
                randint(0, 500)  # y position
            ))

        for i in range(7):
            win3 = Tk()
            win3["bg"] = self.bgColor
            btn3 = Button(win3, text="CLICK HERE TO DELETE", font=("Times", 10),bg=self.fontColor, foreground=self.bgColor,command=win3.destroy).pack(anchor="center")
            label3 = Label(win3, text="^YOU HAVE A VIRUS^",bg=self.bgColor,foreground=self.fontColor,font=("Times", 10)).pack(anchor="center")
            win3.geometry("+{}+{}".format(
                randint(0, 1000),  # x position
                randint(0, 500)  # y position
            ))

        for i in range(7):
            win4 = Tk()
            win4["bg"] = self.bgColor
            btn4 = Button(win4, text="CLICK HERE TO DELETE", font=("Times", 10),bg=self.fontColor, foreground=self.bgColor,command=win4.destroy).pack(anchor="center")
            label4 = Label(win4, text="^YOU GOT HACKED HAHA^",bg=self.bgColor,foreground=self.fontColor,font=("Times", 10)).pack(anchor="center")
            win4.geometry("+{}+{}".format(
                randint(0, 1000),  # x position
                randint(0, 500)  # y position
            ))
def main():
    root = Tk()
    my_gui = Program(root)
    root.mainloop()
if __name__ == "__main__":
    main()