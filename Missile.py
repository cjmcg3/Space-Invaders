from tkinter import *
import time,random

class Missile:
#### to complete

    #basic constructor stuff
    def __init__(self,canvas,max_height=0,increment=5,color='orange',missile_width=8,missile_height=25):
        self.canvas=canvas
        self.max=max_height
        self.inc=increment
        self.color=color
        self.w=missile_width
        self.h=missile_height
        self.__active=False

    def activate(self,x,y):
        self.__active=True
        self.x=x  #sets activation coords
        self.y=y
        self.rect=self.canvas.create_rectangle(0+self.x,self.y,self.w+self.x,self.h+self.y,fill=self.color,outline=self.color)
        #the above creates a missile at the coordinates that are supplied in main

    def deactivate(self):
        self.__active=False
        self.canvas.delete(self.rect) #removes missile 

    def is_active(self):
        return self.__active #retuns bool of active state

    def next(self):
        if self.__active == True:
            self.canvas.move(self.rect,0,-self.inc) #moves missile upwards
            self.y=-self.inc+self.y  #updates y coordinate 
            self.xcoord=self.canvas.coords(self.rect)[0]
            self.ycoord=self.canvas.coords(self.rect)[1]
            #if the coordinates of the missile are past the given ceiling, deactivate
            if self.canvas.coords(self.rect)[1] < self.max:
                self.deactivate()
                

    @staticmethod
    def add_missile(canvas,missiles,x,y,max_height,increment,color):
        #sets a missile to a variable and puts it into a list for storage 
        missy=Missile(canvas,max_height,increment,color)
        missy.activate(x,y)
        missiles.append(missy)

###################################################
###################################################

        
def main(): 
       
        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        ####### start simulation
    
        ############################################
        #           # initialize time clock   
        t=0    
        while True:
            
############################################################################MINE
           ##### To complete
#############################################################################TO MINE           
            if t%50==0:
                #every 0.5 seconds, add a missile at given papameters
                x=random.randint(8,canvas.winfo_width()-8)
                y=canvas.winfo_height()
                increment=random.randint(2,7)
                max_height=random.randint(0,500)
                Missile.add_missile(canvas,missiles,x,y,max_height,increment,'orange')               
            
            
            for shoot in missiles:
                shoot.next()  #keep the missile moving   
       

            for m in missiles:
                print(m.is_active(),end='')
            print()
            
            for m in missiles:  #deletes the bool state from memory 
                if not m.is_active():
                    missiles.remove(m)


            # update the graphic and wait time        
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second  
            t=t+1  #how many loops it goes through

########################################################## Every 0.01 seconds, t is adding 1 to itself When 0.01 has looped to 0.5,
        root.mainloop() # wait until the window is closed
        
if __name__=="__main__":
    main()

