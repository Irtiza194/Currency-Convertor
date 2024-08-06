#from here we will import the window and GUI, including the functionality to make the program
from tkinter import Tk,ttk
from tkinter import *
from tkinter import messagebox
from tkinter import Label

from PIL import Image, ImageTk
from click import command

import requests
import json

#Colour palette
cor0 = "#F5F5F5" #White
cor1 = "#36454F" #Black
cor2 = "#3d5c71" #Blue

#Size of the window
window = Tk()
window.geometry('300x320')
window.title('Currency Converter')
window.configure(bg=cor0)

#Here we will declare that we will not resize the window, for ease of access
window.resizable(height= FALSE, width=FALSE)

#title frame "Currency Converter"
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)
#again, title frame
main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)

#API function
def convert():
    #website that will give us the converted amount
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    #when the user has selected the currencies, this will ask the API for the conversion
    Currency_1 = combo1.get()
    Currency_2 = combo2.get()
    Amount = value.get()
    #basically, telling the API that we want these currencies to convert
    querystring = {"from": Currency_1,"to":Currency_2,"amount":Amount}
    # Check if the input is valid
    if not Currency_1 or not Currency_2 or not Amount:
        messagebox.showerror("Invalid Input", "Please select currencies and enter a valid amount.")
        return
    try:
        float(Amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")
        return
    # if else statement. Here we will put the currency symbol with the converted amount
    if Currency_2 == 'USD':
        symbol = '$'
    elif Currency_2 == 'INR':
        symbol = '7'
    elif Currency_2 =='EUR':
        symbol = '€'
    elif Currency_2 == 'BRL':
        symbol = 'R$'
    elif Currency_2 == 'CAD':
        symbol = 'CA $'
    #authentication so that the API recognizes the user and allows it to convert accurately
    headers = {
        "X-RapidAPI-Key": "332df1d7ffmshdc495be2d06b4f9p1f6a33jsnb9541a237b5b",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }
    #what should the API do? It should get the converted amount, in other words, order the API
    response = requests.request("GET", url, headers=headers, params=querystring)
    #here we will get the response and load in the program so that later we can adjust it
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    #format the amount, in other words, add comas, points...
    formatted = symbol + "{:,.2f}".format(converted_amount)
    #show the formatted amount
    result['text'] = formatted
    #simply show the amount
    print(converted_amount, formatted)   

#title frame editing, here we will put an image and a title
icon = Image.open('image\icon.png')
#size of the image
icon = icon.resize((50,50))
#allowing the image to be in the GUI
icon = ImageTk.PhotoImage(icon)
#editing the text, fonts, size...
app_name = Label(top, image = icon, compound=LEFT,  text="Currency Converter", height=9, pady=20,padx=20, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg='#F5F5F5')
#place for the text
app_name.place(x=0, y=0)

#the white frame where on top of it, will be everything such as dropdown menus
result = Label(main, text=" ", width=16, height=2, pady=7, relief=SOLID, anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

#Currencies
currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD',]

#from currency frame
from_label = Label(main, text="From", width=8, height=1, pady=0, padx=0, relief=FLAT, anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
#place for the menu
from_label.place(x=48, y=90)
#size of the menu
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'),)
#values or identities for user to choose
combo1['values'] = (currency)
#place for the to currency to be shown
combo1.place(x=50, y=115)

#to currency dropdown menu
to_label = Label(main, text="To", width=8, height=1, pady=0, padx=0, relief=FLAT, anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)
#size of the dropdown menu
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
#values or identities for user to choose
combo2['values'] = (currency)
#place for the to currency to be shown
combo2.place(x=160, y=115)

#frame where the result will be shown
value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=155)

#Button that when pressed it should convert
button = Button(main, text="Convert",  width=19, padx=5, height=1, bg=cor2, fg=cor0, font=("Ivy 12 bold"), command=convert)
#place of the button
button.place(x=50,  y=210)
#a loop, just so that the user can do it again and again
window.mainloop()