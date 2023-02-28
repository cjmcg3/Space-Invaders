from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        

        
        ############################################
        ####### start simulation
        ############################################
        t=0
        while True:
                x=random.randint(8,w-8)  #random x coordinate within the constraints of the screen with missile width in consideration
                y=h  #set position for the missiles to spawn 
                max=random.randint(h//4,3*h//4)   #random height for the fireworks to explode
                ecolors=["blue","red","yellow","green","orange","purple",'rainbow','rainbow']
                ecolor=random.choice(ecolors)   #random choice of colors for explosion               
                
                if t%50==0:  #adds a missile on screen every 0.5 seconds 
                        Missile.add_missile(canvas,missiles,x,y,max,random.randint(2,7),'orange') 
                
                for missy in missiles:
                        active=missy.is_active() #checks active state 
                        missy.next()
                        var=missy.is_active()   #checks active state 
                        if active==True and var==False:    #if the missile has just deactivated, add an explosion at that coordinate 
                                Explosion.add_explosion(canvas,booms,missy.x,missy.y,random.randint(100,300),ecolor)

                for boom in booms:
                        boom.next() #keep the explosions running


                root.update()   # update the graphic (redraw)
                time.sleep(0.01)  # wait 0.01 second  
                t=t+1

        root.mainloop()



        

if __name__=="__main__":
    main()

