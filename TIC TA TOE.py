from tkinter import *
import tkinter.messagebox

#creating the window
tk = Tk()
tk.title("Tic Tac Toe By Fun With Python(Gaurang)")

a=[[0,0,0],
   [0,0,0],
   [0,0,0]]

playera = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
#Take PLayer Name
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

buttonclick = True
total_button_clicked = 0
#Function To disable Clicked Buttons
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)



def btnClick(buttons):
    global buttonclick, total_button_clicked, player2_name, player1_name, playerb, playera
    if buttons["text"] == " " and buttonclick == True:
        buttons["text"] = "X"
        buttonclick = False
        
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkForWin()
        total_button_clicked += 1


    elif buttons["text"] == " " and buttonclick == False:
        buttons["text"] = "O"
        buttonclick = True
        checkForWin()
        total_button_clicked += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
#fuction to check the winner
def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playera)

    elif(total_button_clicked == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

#all the Buttons
buttons = StringVar()

label = Label( tk, text="Player 1:", font='Arial 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Arial 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Arial 20 bold', bg='light blue', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
