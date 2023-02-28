from tkinter import *
import math,time,random
from Dot import Dot
import numpy as np 
#### to complete

class Explosion:
    def __init__(self,canvas,maxr=80,color='rainbow'):
        self.canvas=canvas
        self.maxr=maxr
        self.color=color
        self.num_dots=15 #num of dots per layer 
        self.list_dots=[] #controlls the dots created 
        self._active=True 

    def activate(self,x,y):  #activates at a point defined by add_explosion
        self._active=True
        self.x=x
        self.y=y
        self.radius=0    
      
    def is_active(self):   #returns bool of the state of the explosion
        return self._active
   
    def next(self):  #keeps the explosion expanding in a given direction
        self._active=True
        i=0
        self.radius+=1  #increment the radius 
        while i < (self.num_dots): #run the loop 15 times (or based on number set to variable)
            angle=random.randint(0,359)
            r=math.cos(angle)*self.radius  #dot expansion
            r2=math.sin(angle)*self.radius  #dot expansion
            dot=Dot(self.canvas,r+self.x,r2+self.y,self.color)
            self.list_dots.append(dot)  #add each dot created to a list for storage
            i=i+1
        if self.radius > self.maxr:   #explosion expanding until the given max size is reached 
            self.deactivate()

    def deactivate(self):   
        for i in self.list_dots:
            self.canvas.delete(i.oval)  #deletes the dots from the screen 
        self._active=False
                
    @staticmethod
    def add_explosion(canvas,booms,x,y,maxr=80,color='rainbow'):
        exps=[Explosion(canvas,maxr,color),Explosion_gravity(canvas,maxr,color)]#,Explosion(canvas,maxr,color)]  #random choice of explosion types 
        dotty=random.choice(exps)   #activates the randomly selected explosion 
        dotty.activate(x,y)    
        booms.append(dotty)   #adds the explosion to a tracking system 
        for boom in booms:
            if boom.is_active() == False:
                booms.remove(boom)   #removes ONLY ONE bool state of the explosion from the memory
'''i=0 
        while True:
            l=len(booms)
            if l=0 or l=1:
                break
            if booms[i].is_active() ==False:
                booms.pop[i]   #removes ONLY ONE bool state of the explosion from the memory
            else:
                i+=1'''

class Explosion_gravity(Explosion):
    def __init__(self,canvas,maxr=80,color='rainbow'):
        super().__init__(canvas,maxr=80,color='rainbow')
        self.maxr=maxr
        self.color=color
        for i in range(15):   #get the random integers 15 times
            self.speed=np.random.uniform(1,5,15)
            self.theta=np.radians(np.random.uniform(0,359,15))

    def next(self):
        self._active=True
        i=0
        self.radius+=1
        for i in range(15):
            dot=Dot(self.canvas,self.x+(-self.speed[i]*np.cos(self.theta[i])*self.radius),self.y+(-self.speed[i]*np.sin(self.theta[i])*self.radius)-((-0.06/2)*self.radius**2),self.color)
            #for the line above, I take the index of the arrays created in the constructor, and apply them to the given equation
            self.list_dots.append(dot)
            if self.radius > self.maxr:  #same concepts as regular explosion
                self.deactivate()
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y))
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms: #boom is object type Explosion
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

