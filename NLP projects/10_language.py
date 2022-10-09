from tkinter import *
from tkinter import ttk
import googletrans
from googletrans import Translator
root = Tk() #here the window is created
root.title("Language Translator from group number 10")#giving the title of the project
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="green")

def label_change():
    c=combo1.get()
    c2=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c2)
    root.after(1000,label_change)

def translate_now():
    text_=text1.get(1.0, END)
    t1=Translator()
    trans_text=t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)
# icon
image_icon = PhotoImage(file="direction.PNG")
root.iconphoto(False, image_icon)

# for arrow
arrow_image = PhotoImage(file="direction.PNG")
arrow_image_label = Label(root, image=arrow_image, width=150)
arrow_image_label.place(x=460, y=50)

# making the constructor for the googlr translatore
language = googletrans.LANGUAGES #to check how many languages are present
languageV = list(language.values())
lang1 = language.keys()

# firsst combo box
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English") #by default i select it
label1 = Label(root,text="bydefault",font="segoe 30 bold",width=18, bd=5, relief=GROOVE,bg="blue")
label1.place(x=10,y=50)


# second combo box
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("English") #by default i select it

label2 = Label(root, text="bydefault",font="segoe 30 bold",width=18, bd=5, relief=GROOVE,bg="blue")
label2.place(x=620 , y=50)

# first frame
f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

# text1=Text()
text1=Text(f, font="Robote 20", bg="purple", width=18, bd=5, relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill='y')
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# creating the seccond frame
f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

# text1=Text()
text2=Text(f1, font="Robote 20", bg="white", width=18, bd=5, relief=GROOVE, wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)
scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill='y')
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# translate button
translat=Button(root,text="Translate", font=("Roboto",15),activebackground="white",cursor="hand2",bd=1,width=10,height=2,bg="black",
                fg="white",command=translate_now)
translat.place(x=476,y=250)

label_change()
root.mainloop()