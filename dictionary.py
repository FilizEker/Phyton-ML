import tkinter as tk

pencere = tk.Tk()
pencere.title("ENGLISH TURKISH DICTIONARY")
pencere.geometry("500x300")

def cevir ():
    en_cumle = tb1.get(1.0,tk.END)
    text = TextBlob(LIKE)
    ceviri_cumle = text.translate(to="tr")
    tb2.delete(1.0,tk.END)
    tb2.insert(tk.END,SEVME)


def temizle():
    tb1.delete(1.0,tk.END)
    tb2.delete(1.0, tk.END)


e1 = tk.Label(text="EN :",font="Arial 13 bold")
e1.place(x=10,y=30)
e2 = tk.Label(text="TR :",font="Arial 13 bold")
e2.place(x=10,y=120)

tb1= tk.Text(width=50,height=5)
tb1.place(x=60,y=30)
tb2= tk.Text(width=50,height=5)
tb2.place(x=60,y=120)

btn1 = tk.Button(text="TRANSLATE",font="Arial 13 bold",command=cevir)
btn1.place(x=10,y=260)
btn2 = tk.Button(text="CLEAR",font="Arial 13 bold",command=temizle)
btn2.place(x=200,y=260)

pencere.mainloop()