#import
from tkinter import *
from pygame import mixer
from tkinter import messagebox
import webbrowser
#creation de la page graphique
file = 'click.mp3'
page = Tk()
page.geometry('1269x718')
page.title("Un truc vreeeeeuuumuuent")
operator=""
text_Inpunt =StringVar()
page['bg'] = '#ff6666'
#page.resizable(height=False,width=False)
#creation du logiciel
C = Canvas(page, bg="blue", height=False, width=False)
filename = PhotoImage(file ='dream.png')
background_label = Label(page, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

#function    
def polo():
    print("selut")

def function():
    if mavariable.get() == "crakoze_":
        sub_label = Label(page, text="Bonjour clicker sur le bouton pour afficher la prochaine etape")
        sub_label.pack()
        bouton = Button(page, text="secret", command=polo)
        bouton.pack(expand=YES)
    else:
        print("poulet")

def discord():
    webbrowser.open('https://discord.gg/EN365HM')

def github():
    webbrowser.open('https://github.com/crakoze1119')
    
def sound():
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
#variable
#photo = PhotoImage(file='click.png')
githubpng = PhotoImage(file='github.png')
discordpng = PhotoImage(file='discord.png')
#mavariable = StringVar()
#label = Label(page, text="Mot de passe")
#label.pack()
#entree = Entry(page, textvariable=mavariable)
#entree.pack()
#bouton = Button(page, text="Valider", image=photo, command=function)
#bouton.pack()
           
#bouton
bouton2 = Button(page, text="My discord sever", image=discordpng, command=discord)
bouton2.place(x='230', y='630')

bouton3 = Button(page, text="My github", image=githubpng, command=github)
bouton3.place(x='45', y='630')
#texte
text_discord = Label(page, text="Discord", font=("Verdana", 20, "italic bold"), fg="black", bg="#99ff99")
text_discord.place(x='200', y='600')

text_github = Label(page, text="GitHub", font=("Verdana", 20, "italic bold"), fg="black", bg="#99ff99")
text_github.place(x='20', y='600')


name = Label(page, text="By crakoze_ 2020", font=("Verdana", 10, "italic bold"), fg="black", bg="#66b3ff")
name.place(x='1100', y='660')

info = Label(page, text='Salut cette calculatrice a été faite pour le plaisir.', font=("Verdana", 15, "italic bold"), fg="black", bg="#cc80ff")
info.place(x='10', y='')

info2 = Label(page, text="Alors viens pas me dire qu'elle pue la merde je le sait déjà", font=("Verdana", 15, "italic bold"), fg="black", bg="#cc80ff")
info2.place(x='10', y='50')

info3 = Label(page, text='vue que c’est moi qui l’a créé.', font=("Verdana", 15, "italic bold"), fg="black", bg="#cc80ff")
info3.place(x='10', y='100')

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Inpunt.set(operator)

def btnEqualsInputn():
    global operator
    sumup=str(eval(operator))
    text_Inpunt.set(sumup)

def btnClearDisplay():
    global operator
    operator=""
    text_Inpunt.set("")

boite = Frame(page, bg=('#ff6666'))

txtDisplay = Entry(boite,font=('arial', 20,'bold'), textvariable=text_Inpunt, bd=30, insertwidth=4,
                   bg="#ff6666", justify='right').grid(columnspan=4)


btn7=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="7", bg="#ff6666", command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="8",bg="#ff6666", command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="9",bg="#ff6666", command=lambda:btnClick(9)).grid(row=1,column=2)

addition=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="+",bg="#ff6666", command=lambda:btnClick("+")).grid(row=1,column=3)

btn4=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="4",bg="#ff6666", command=lambda:btnClick(4)).grid(row=2,column=0)

btn5=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="5",bg="#ff6666", command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="6",bg="#ff6666", command=lambda:btnClick(6)).grid(row=2,column=2)

soustraction=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="-",bg="#ff6666", command=lambda:btnClick("-")).grid(row=2,column=3)

btn1=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="1",bg="#ff6666", command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="2",bg="#ff6666", command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="3",bg="#ff6666", command=lambda:btnClick(3)).grid(row=3,column=2)

multiplication=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="x",bg="#ff6666", command=lambda:btnClick("*")).grid(row=3,column=3)


btn0=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="0",bg="#ff6666", command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="C",bg="#ff6666", command=btnClearDisplay).grid(row=4,column=1)

btnEgale=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="=",bg="#ff6666", command=btnEqualsInputn).grid(row=4,column=2)

btnDivision=Button(boite,padx=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="/",bg="#ff6666", command=lambda:btnClick("/")).grid(row=4,column=3)

boite.place(x='500', y='200')






page.mainloop()
