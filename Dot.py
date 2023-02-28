########################
## Team Members
## Name1: Connor McGarry        
## Name2: N/A
#########################

from tkinter import *
import random
class Dot:
    ##### TO COMPLETE
    def __init__(self,canvas,x,y,color,display=False):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.display=display
        self.color=color
        self.rand=['red','green','blue','yellow','white','orange','purple']  #sets up the list of colors for the rainbow effect
        self.random=random.choice(self.rand)  #sets a variable to the random color choice from the list
        if self.color=='rainbow':  #if the color is rainbow, make each dot a different random color 
            self.oval=canvas.create_oval(self.x+1,self.y+1,self.x-1,self.y-1,outline=self.random,fill=self.random) #sets oval at click coords and fills with a consistant random color
        else:   #else, make dots all the same color as the given color
            self.oval=canvas.create_oval(self.x+1,self.y+1,self.x-1,self.y-1,outline=self.color,fill=self.color)
        if self.display==True:  #as true is given in the bind 
            print("%s %s %s"%(self.x,self.y,self.random))   #prints on click

#################################################################
#################################################################
    
def main(): 

    ##### create a window, canvas
    root = Tk() # instantiate a tkinter window
    canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
    canvas.pack()
    root.update()   # update the graphic
            
    # Tkinter binding action (mouse click)
    root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
    
    root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

