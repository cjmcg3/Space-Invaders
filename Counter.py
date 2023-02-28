from tkinter import *

class Counter:
    # to complete
    def __init__(self,canvas,count=0):
        self.canvas=canvas
        self.count=count
        #creates count on screen depending on input 
        self.txt=canvas.create_text(580,20,text=self.count,fill="orange",font=("Courier",25))
        self.image=PhotoImage(file="ship.png")
        self.smallship=self.image.subsample(3,3)
        self.life3=self.canvas.create_image(0,0,anchor=NW,image=self.smallship)
        self.life2=self.canvas.create_image(25,0,anchor=NW,image=self.smallship)
        self.life1=self.canvas.create_image(50,0,anchor=NW,image=self.smallship)

    def increment(self,inc):  #i call counter in main starting at 10. When i press keys i need that dislay to be edited
        if inc:  #if given a value... 
            self.count+=inc 
            #...change the value based on the givan value
        self.canvas.itemconfig(self.txt, text=self.count)
    #########################

    def delete_ship(self,life):  #takes a life number as a condition
        if life==1:                       ##########################################
            self.canvas.delete(self.life1)
        elif life==2:
            self.canvas.delete(self.life2)   #deletes the corrosponding ship based off taking in the number 1 2 or 3
        elif life==3:
            self.canvas.delete(self.life3) ##########################################



def main():
    # to complete
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    my_image=PhotoImage(file="space2.png")
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image) #creates the background

    amunition = Counter(canvas,10) #create instance of Counter

    #binds the left and right arrow keys to the method that changes value of counter
    root.bind("<Left>",lambda e:Counter.increment(amunition,-1))
    root.bind("<Right>",lambda e:Counter.increment(amunition,1))
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)    
    ####### Tkinter binding mouse actions

    root.mainloop() 

if __name__=="__main__":
    main()



        
