
#imports 
from sys import prefix
import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import *
from pygame import mixer
import time
mixer.init()

#Makes the windows
root = tk.Tk()
root.title("<< home >>")
root.geometry("340x360")

MUSIC = [
"Default",
"Where We Wanna Go",
"Wehrmut",
"Stranger Think",
"To Pass Time"
]

CLICK = [
"Default",
"Click2"
]

#Variables
index = 1
count = 0


#Style for buttons
style = ttk.Style(root)
style.map("TButton",
    foreground=[('pressed', '#07314d'), ('active', '#bed9e8'), ('!active', '#84bddb')], 
    background=[('pressed', '#4a4a4a'), ('active', '#a83250'), ('!active', '#4a4a4a')],
    borderwidth=[('pressed', '0'), ('active', '0'), ('!active', '0')]
    )


#Code for quit button
def kill_button():
    click_sound()
    time.sleep(0.12)
    print("Program is now exiting...")
    root.destroy()

def ok():
    click_sound()
    lobby_music()
    menu()


#Menu Buttons
title_label = ttk.Label(text = 'Revision',font=("Helvetica", 50),foreground="#84bddb")
settings_button = ttk.Button(root, text="Preferences!",style="TButton", command = lambda: reset('settings'))
computer_science = ttk.Button(root, text="Computer Science!",style="TButton", command = lambda: reset('cs_rev'))
biology = ttk.Button(root, text="Biology",style="TButton", command = lambda: reset('biology_rev'))
geography = ttk.Button(root, text="Geography",style="TButton", command = lambda: reset('geography_rev'))
quit_button = ttk.Button(root, text="Quit App",style="TButton", command=kill_button)


#Titles
pref_title = ttk.Label(text = 'Preferences',font=("Helvetica", 40))


#Other
back_button = ttk.Button(root, text = 'Back', style = 'TButton', command = lambda: reset('menu'))
coming_soon = tk.Label(root, text = 'COMING SOON!') #CAN REPURPOSE IN tHE FUTURE

musicvar = StringVar(root)
musicvar.set(MUSIC[0]) # default value
w = OptionMenu(root, musicvar, *MUSIC)
clickvar = StringVar(root)
clickvar.set(CLICK[0]) # default value
w1 = OptionMenu(root, clickvar, *CLICK)

ok_button = ttk.Button(root, text="Confirm Choices", style="TButton", command= lambda: reset('ok'))

#Packing all the buttons, titles, etc for code to run
widgets = [pref_title,w,w1,ok_button,settings_button,title_label,computer_science,biology,geography,quit_button,back_button,coming_soon]



#--Functions--# 
def reset(function): #allows commands to be reset
    for widget in widgets:
        widget.pack_forget()

    if function == 'biology_rev':
        for widget in widgets:
            widget.pack_forget()
        title_label.pack_forget()
        biology_rev()

    elif function == 'settings':
        title_label.pack_forget()
        settings()

    elif function == 'menu':
        for widget in widgets:
            widget.pack_forget()
            geography.pack_forget()
            biology.pack_forget()
            computer_science.pack_forget() 
            coming_soon.pack_forget()
        menu()
    
    elif function == 'ok':
        for widget in widgets:
            widget.pack_forget()
        ok()

    elif function == 'cs_rev':
        for widget in widgets:
            widget.pack_forget()
        title_label.pack_forget()
        cs_rev()

    elif function == 'geography_rev':
        for widget in widgets:
            widget.pack_forget()
        title_label.pack_forget()
        cs_rev()
    

def click_sound():
    if clickvar.get() == "Click2":
        click = mixer.Sound('click2.mp3')
        click.play()
    elif clickvar.get() == "Default":
        click = mixer.Sound('click.wav')
        click.play()

def lobby_music():
    if musicvar.get() == "Default":
        mixer.music.load("music.wav")
        mixer.music.play()
        mixer.music.play(-1)     
    elif musicvar.get() == "Where We Wanna Go":
        mixer.music.load("choice1.mp3")
        mixer.music.play()
        mixer.music.play(-1)
    elif musicvar.get() == "Wehrmut":
        mixer.music.load("choice2.mp3")
        mixer.music.play()
        mixer.music.play(-1)
    elif musicvar.get() == "Stranger Think":
        mixer.music.load("choice3.mp3")
        mixer.music.play()
        mixer.music.play(-1)
    elif musicvar.get() == "To Pass Time":
        mixer.music.load("choice4.mp3")
        mixer.music.play()
        mixer.music.play(-1)



def settings():
    root.title("<< preferences >>")
    pref_title.pack(pady = 20)
    click_sound()
    w.pack()
    w1.pack()
    ok_button.pack(pady=20)


def cs_rev(): #code for the computer science page
    click_sound()
    root.title("<< computer science >>")
    coming_soon.pack(pady=30)
    back_button.pack(pady=30)
    #I havent wrote it yet!


def biology_rev(): #code for the biology page
    click_sound()
    root.title("<< biology >>")
    coming_soon.pack(pady=30)
    back_button.pack(pady=30)
    #I havent wrote it yet!

def geography_rev(): #code for the geography page
    click_sound()
    root.title("<< geography >>")
    coming_soon.pack(pady=30)
    back_button.pack(pady=30)
    #I havent wrote it yet!


def menu(): #buttons displayed on the main menu
    click_sound()
    root.title("<< home >>")
    title_label.pack(pady = 30)
    settings_button.pack(pady = 5)
    computer_science.pack(pady = 10)
    geography.pack(pady=10)
    biology.pack(pady = 10)
    quit_button.pack(pady = 10)
    

myMenu=Menu(root)
root.config(menu=myMenu)

optionsMenu=Menu(myMenu,tearoff=False)
myMenu.add_cascade(label="Options",menu=optionsMenu)
optionsMenu.add_command(label="Home",command=lambda:reset("menu"))
optionsMenu.add_command(label="Quit",command=kill_button)

menu()
lobby_music()
root.mainloop()
