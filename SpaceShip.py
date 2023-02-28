from tkinter import *

class SpaceShip:
    def __init__(self,canvas):
        self.canvas=canvas
        self.__active=False


    '''Chose to place ship at a NW anchor point, so any placement adjustments are to account for that'''
    
    def activate(self):
        self.__active=True
        self.xpos=(Canvas.winfo_width(self.canvas)/2)-37  #Sets x position taking the size of the spaceship and size of any canvas into consideration
        self.ypos=Canvas.winfo_height(self.canvas)-122   #Sets y position taking the size of the spaceship and size of any canvas into consideration
        self.image=PhotoImage(file="ship.png")
        self.w=self.image.width()//2
        self.h=self.image.height()//2
        self.ship=self.canvas.create_image(self.xpos,self.ypos,anchor=NW,image=self.image)  #makes the ship appear
        self.x=self.canvas.coords(self.ship)[0]+33  #for use in game2 (snapshots xcoord)
        self.y=self.canvas.coords(self.ship)[1] #for use in game2 (snapshots ycoord)
        

    def is_active(self):
        return self.__active #returns the true or false of the state that _active is in 

    def deactivate(self):
        self.canvas.delete(self.ship)  #deletes ship from screen
        self.__active=False 

    def shift_left(self):
        if int(self.canvas.coords(self.ship)[0]) >= 15: #last visible full ship on left
            self.canvas.move(self.ship,-15,0)       #move in 15 pixel increments to the left
            self.x=(self.canvas.coords(self.ship)[0]+33)#snapshot for game 2
            self.y=self.canvas.coords(self.ship)[1]#snapshot for game 2
        else:
            self.canvas.move(self.ship,int(-self.canvas.coords(self.ship)[0]),0) #snaps to the left wall 
            self.x=(self.canvas.coords(self.ship)[0]+33) #snapshot for game 2
            self.y=self.canvas.coords(self.ship)[1] #snapshot for game 2


    def shift_right(self):
        if int(self.canvas.coords(self.ship)[0]) <= (Canvas.winfo_width(self.canvas)-90):#(last visible full ship on left)
            self.canvas.move(self.ship,15,0)   #move the ship 15px to the right on a right arrow key press
            self.x=(self.canvas.coords(self.ship)[0]+33) 
            self.xcoord=self.canvas.coords(self.ship)[0]#snapshot for game 2
            self.ycoord=self.canvas.coords(self.ship)[1] #snapshot for game 2
        else:
            self.canvas.move(self.ship,(Canvas.winfo_width(self.canvas)-80)-(self.canvas.coords(self.ship)[0]),0)
            self.x=(self.canvas.coords(self.ship)[0]+33)  #snaps to the right wall
            self.xcoord=self.canvas.coords(self.ship)[0]#snapshot for game 2
            self.ycoord=self.canvas.coords(self.ship)[1]#snapshot for game 2
       



   
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left()) #bind left to moving left
    root.bind("<Right>",lambda e:ship.shift_right()) #bind right to moving right

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

