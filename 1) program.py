'''VACUUM CLEANER - AN INTELLIGENT AGENT'''
import tkinter as tk
from functools import partial
import time

global room,button,l_room,b_room,vc

#creating a room
def create_room():
    global room,button
    room = [ ['' for j in range(b_room)] for i in range(l_room)]
    button = [['' for j in range(b_room)]for i in range(l_room)]

#creating a vacuum cleaner
def create_vacuum():
    global vc
    vc = [0,0]

#function to dirty the room via user's mouse clicks on the respective tiles
def dirty_the_room(m,n):
    global room,button
    room[m][n] = 'dirty'
    button[m][n].config(text=room[m][n],fg='white',bg='tan4')

#sucking the dirt when a dirty tile is encountered
def suck_dirt(m,n):
    room[m][n] = 'cleaned'
    button[m][n].config(text=room[m][n],fg='black',bg='light steel blue')

#function to clean the room
def clean():
    global vc
    vc=[0,0]
    while(vc[0]!=l_room):
        if(room[vc[0]][vc[1]]=='dirty'):
            suck_dirt(vc[0],vc[1])
        if(vc[1]==b_room-1 and vc[0]!=l_room):
            vc[0] += 1
            vc[1]=0
        else:
            vc[1] += 1

#displaying the room  
def print_room():
    for i in range(l_room):
        for j in range(b_room):
            dirty=partial(dirty_the_room,i,j)
            button[i][j] = tk.Button(frm,text=room[i][j],command=dirty,bg='light steel blue',height=5,width=10)
            button[i][j].grid(row=i,column=j)
   
if __name__=='__main__':
    main = tk.Tk()
    lbl = tk.Label(main,text='VACUUM CLEANER - AN INTELLIGENT AGENT',fg='black',bg='plum1',height=3,width=40)
    lbl.pack()
    frm = tk.Frame(main)
    frm.pack()
    clean_btn = tk.Button(main,text='clean the room',bg='khaki3',command=clean,height=2,width=20) #button to enable the cleaning process
    clean_btn.pack(anchor='se')
    l_room = 4 #lenght of the room in metres
    b_room = 10 #breadth of the room in metres
    create_room()
    create_vacuum()
    print_room()
    main.mainloop()

