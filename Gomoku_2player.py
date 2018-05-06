'''By Xiangxin Kong
May 6th
Gomoku, also called Gobang or Five in a Row, is an abstract strategy board game.
It's traditionally played with Go pieces (black and white stones) on a Go board, using 19×19 grid intersections.
Players alternate turns placing the 'stone' of their color on the empty intersection.
The winner is the first player to form an unbroken chain of five stones horizontally, vertically, or diagonally.
The program will terminate once the winner occur.
'''
from tkinter import *
import tkinter.messagebox
board=[[0 for i in range(20)] for i in range(20)]#initialize the board. 0 for empty
turn=0#use odd-even to show which player is playing this turn

def play(click):
#This function convert the coordinate of the click to the coordinate on the board, save it in board,
#then pass it to draw function
    global turn
    x,y=click.x+17,click.y+17
    x,y=x//35,y//35
    if x>19:x=19
    if x<1:x=1
    if y>19:y=19
    if x<1:x=1
    if board[x][y]==0:
        turn=turn+1
        if turn % 2 == 0:
            board[x][y]=1
            draw(x,y,'#F5F5F5')
            check(x,y,1)
        else:
            board[x][y] = 2
            draw(x, y, 'black')
            check(x,y,2)

def draw(x,y,color):
#this function draw the oval
    interface.create_oval(35*x-15,35*y-15,35*x+15,35*y+15,fill=color,outline=color)

def check(x,y,turn):
#this function check if player win the game
    global win
    won=False

    countH,countV=0,0
    for i in range(20):
        #this loop check if the 'stone' form a horizontal or vertical chain
        if board[x][i]==turn:
            countV+=1
        else:
            countV=0
        if board[i][y]==turn:
            countH+=1
        else:
            countH=0
        if countH==5 or countV==5:
            won=True
            break

    count = 0
#the following if-loop structure check if the 'stone' form a diagnal chain
    if x + y > 19:
        for i in range(39 - x - y):
            if board[x + y - 19 + i][19 - i] == turn:
                count += 1
                if count == 5:
                    won = True
                    break
            else:
                count = 0
    else:
        for i in range(x + y - 1):
            if board[1 + i][x + y - 1 - i] == turn:
                count += 1
                if count == 5:
                    won = True
                    break
            else:
                count = 0
    if x - y > 0:
        for i in range(19 + y - x):
            if board[19 - i][19 + y - x - i] == turn:
                count += 1
                if count == 5:
                    won = True
                    break
            else:
                count = 0
    else:
        for i in range(19 - y + x):
            if board[19 - y + x - i][19 - i] == turn:
                count += 1
                if count == 5:
                    won = True
                    break
            else:
                count = 0

    if won:
        #pop the winning information and terminate the program
        tkinter.messagebox.showinfo('','You won!')
        win.destroy()

#create a window
win=Tk()
win.title("BetaGO")
win.geometry("700x700")
win.configure(background='black')
# draw the grid on canvas with clicking event
interface=Canvas(win,height=700,width=700)
interface.pack(expand=TRUE,fill=BOTH)
interval=35
for i in range(1,20):
    interface.create_line(i*interval,interval,i*interval,19*interval,width=2)
    interface.create_line(interval,i*interval,19*interval,i*interval,width=2)
interface.configure(background='#F5DEB3')
interface.bind("<Button-1>",play)
#running the program
win.mainloop()