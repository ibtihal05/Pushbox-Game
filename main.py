from ast import main
import pygame
from game import Game
import search
from tkinter import *
if __name__=='__main__':
    pygame.init()
    game = Game("carte1_deadlock.tmx",3, 336,336) #second argument is the number of boxes we have
    t=game.simulation(search.deadbord1)
    
    window=Tk()
    window.geometry("400x30")
    window.title("Le nombre d'itération")
    text="Le nombre d'itération est:"+str(t)
    lable=Label(window,text=text,font=('Arial',10,'bold'),fg='#000000',bg='#FFDAB9')
    lable.pack()
    window.mainloop()
    
    