from tkinter import *
import math
import time, random
### to complete

class Alien:
    def __init__(self,canvas,px=2,color='yellow',width=50,height=50,point=1):
        #constructor requiremtnts 
        self.canvas=canvas
        self.px=px
        self.color=color
        self.w=width
        self.h=height
        self.point=point
        self._active=False

    def activate(self,x=None,y=None): #placeholder for x and y
        self._active=True
        self.x=random.randint(0,self.canvas.winfo_width()-self.w) #random x coord across given canvas
        self.y=random.randint(0,0) #starts at 0 y 
        #create the primary alien square at the top of the canvas at a random x coord and a y coord of 0 (top)
        self.man=self.canvas.create_rectangle(0+self.x,0+self.y,self.w+self.x,self.h+self.y,fill=self.color,outline=self.color)

    def is_active(self):
        return self._active #returns the true or false of the state that _active is in 

    def deactivate(self):
        self._active=False
        self.canvas.delete(self.man)  #deletes the current alien on the screen  

    def next(self):
        if self._active == True:
            self.canvas.move(self.man,0,self.px) #move down screen
            self.xcoord=self.canvas.coords(self.man)[0] #set x coord
            self.ycoord=self.canvas.coords(self.man)[1] #set y coord
            if self.canvas.coords(self.man)[1] > self.canvas.winfo_height(): #if goes off bottom of screen deactivate
                self.deactivate()

    def is_shot(self,x0,y0):
        if (self.canvas.coords(self.man)[0])//1-self.w//2 <= x0 <= (self.canvas.coords(self.man)[0])//1+self.w//2 and (self.canvas.coords(self.man)[1])//1-self.h//2 <= y0 <= (self.canvas.coords(self.man)[1]//1+self.h//2):
            #if clicked within the size of the square
            return True
        else:
            return False
    
    @staticmethod
    def add_alien(canvas,aliens):
        #list of possible aliens to add
        alien_list=[Alien_red(canvas),Alien_blue(canvas),Alien_green(canvas),Alien_mine(canvas)]
        go=random.choice(alien_list) #choose a random alien
        go.activate()
        for go in alien_list:
            if go.is_active():
                aliens.append(go) #add it to the list that is given when method called
################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,canvas,px=4,color='red',point=2):
        super().__init__(self) #parent
        #inherit methods, but use new paramaters for the new alien
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        self.w=self.image.width()
        self.h=self.image.height()
        self.canvas=canvas
        self.px=px
        self.color=color
        self.point=point
        self._active=False

    #OVERRRIDE  ACTIVATE
    def activate(self,x=None,y=None):
        self._active=True
        self.x=random.randint(24,585)
        self.y=random.randint(0,0)
        #create the red alien at the top of the canvas at a random x coord and a y coord of 0 (top)
        self.man=self.canvas.create_image(self.x,self.y,anchor=CENTER,image=self.image)
    


###############################################################
###############################################################

class Alien_green(Alien_red):
    def __init__(self,canvas,point=4):
        self.point=point
        self.image=PhotoImage(file="alien_green.png")  # keep a reference (avoid garbage collector)
        self.w=self.image.width()
        self.h=self.image.height()#parent 
        Alien.__init__(self,canvas,px=4,color='green',point=4) #parent

    def next(self):
        if self._active == True:
            #alien shifts left and right while moving down at a consistant speed 
            self.canvas.move(self.man,random.randint(-5,5),self.px)
            self.xcoord=self.canvas.coords(self.man)[0]
            self.ycoord=self.canvas.coords(self.man)[1]
            #deactivate if go off canvas
            if self.canvas.coords(self.man)[1] > self.canvas.winfo_height():
                self.deactivate()
    
        

    # to complete


###############################################################
###############################################################
                


class Alien_blue(Alien_red):
    def __init__(self,canvas,point=3,angle=(math.radians(random.randint(-160,-60)))):
        self.angle=angle
        self.point=point
        self.image=PhotoImage(file="alien_blue.png")  # keep a reference (avoid garbage collector)
        self.w=self.image.width()
        self.h=self.image.height()
        #parent
        Alien.__init__(self,canvas,px=4,color='blue',point=3)

    def next(self):
        if self._active == True:
            self.canvas.move(self.man,self.angle,self.px) #starts moving at a set angle based off random integer
            if self.canvas.coords(self.man)[0] > self.canvas.winfo_width()-37.5:
                self.angle=(math.radians(-math.pi)-(self.angle-(math.radians(math.pi)))) 
                #^Changes the angle if hits left wall and stops the speed of the alien from increasing post bounce
            if self.canvas.coords(self.man)[0] < 37.5:
                self.angle=(math.radians(math.pi)-(self.angle+(math.radians(math.pi)))) 
                #^Changes the angle if it hits the right wass and stops the speed of the alien from increasing post bounce
            self.xcoord=(int((self.canvas.coords(self.man)[0])))
            self.ycoord=(int((self.canvas.coords(self.man)[1])))
            #deativtes off bottom
            if self.canvas.coords(self.man)[1] > self.canvas.winfo_height():
                self.deactivate()

###############################################################
class Alien_mine(Alien_red):
    def __init__(self,canvas,px=3,color='purple',point=5):
        self.image=PhotoImage(file="anya.png")  # keep a reference (avoid garbage collector)
        self.w=self.image.width()
        self.h=self.image.height()
        self.canvas=canvas
        self.px=px
        self.color=color
        self.point=point
        #parent
        Alien.__init__(self,canvas,px=4,color='purple',point=4)

    def next(self):
        if self._active == True:
            #randomly shakes left right up down, but gradually goes down the screen
            self.canvas.move(self.man,random.randint(-10,10),random.randint(-14,18))
            self.xcoord=self.canvas.coords(self.man)[0]
            self.ycoord=self.canvas.coords(self.man)[1]
            #deactivate off bottom
            if ((self.canvas.coords(self.man)[1]) > self.canvas.winfo_height()):
                self.deactivate()

#################################################################

            
#################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"
    print(x,y,result)


    
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)  

        #Initialize alien
        #alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)
        alien=Alien_mine(canvas)    


        alien.activate()    

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        t=0               # time clock
        while True:
            if t%50==0:

                if not alien.is_active():
                    alien.activate()
                
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
            t=t+1
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

