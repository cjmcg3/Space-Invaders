from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile
        
########## global variable
game_over=False

######### Function
def stop_game():
    global game_over
    game_over=True
    

def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)



    '''CHOSE THE BONUS METHOD FOR GAME OVER REGARDING SHIP LOSING LIVES '''
#########################################
    #Initialize list of Explosions
    booms=[]
    #Initialize list of Aliens
    aliens=[]
    #Initialize ammunition
    missiles=[]
    #counter
    score=Counter(canvas,0)
    #list of explosions for the spaceship death 
    spacebooms=[] 
    #sets up lives
    lives=[1,2,3]

    ####### Tkinter binding mouse actions
    root.bind("<Up>",lambda e:Missile.add_missile(canvas,missiles,spaceship.x,canvas.winfo_height()-150,0,4,'yellow')) #add missile at top of spaceship
    root.bind("<Escape>",lambda e:stop_game())
    root.bind("<Left>",lambda e:spaceship.shift_left())
    root.bind("<Right>",lambda e:spaceship.shift_right())

    #initiate the spaceship
    spaceship=SpaceShip(canvas)
    spaceship.activate()

    ############################################
    ####### start simulation
    ############################################

    tuplelist=[] #list for tracking tuples of game data ty
    record={'red':0,'green':0,'blue':0,'mine':0}  #create dictionary for data 
    t=0
    #To complete (time sleep is 0.01s)

    while True:
        #every 1 second add an alien and append a tuple of dictionary contents to list
        if t%100==0:
            Alien.add_alien(canvas,aliens)
            tuplelist.append((record['red'],record['green'],record['blue'],record['mine']))

        if len(lives)==0:
            #if all the mini ships get deleted
            stop_game()

        if game_over==True:
            #if game over, open a new file 
            f=open("game2.txt",'w')
            for i in range(len(tuplelist)):
                #write the values of the tuple created in shoot
                f.write('%s %s %s %s\n'%(tuplelist[i][0],tuplelist[i][1],tuplelist[i][2],tuplelist[i][3]))
            f.close() 
            canvas.create_text(w/2,h/2,anchor=CENTER,text='GAME OVER',fill="red",font=("system",50)) #create GAME OVER message 
            print(record)#print dictionary results
            for bye in root.bind():
                root.unbind(bye) #unbinds all of the keys so that once game is over, clicks dont chnage score anymore
            root.mainloop() #freezes the screen


        for i in missiles:  #auto deletes for program speed 
            if not i.is_active():
                missiles.remove(i)   #removes inactive missiles from memory

########################## KILL THE SPACESHIP ######################################
        for a in aliens:
            a.next()  #keeps the aliens moving
            if (spaceship.x//1-spaceship.w <= (a.xcoord)//1 <= spaceship.x//1+spaceship.w) and (spaceship.y//1-spaceship.h <= (a.ycoord)//1 <= spaceship.y//1+spaceship.h):
                #if the coordinates of the missile hit within the range of the size of the spaceship
                Explosion.add_explosion(canvas,spacebooms,spaceship.x,spaceship.y+33,50) 
                a.deactivate()  #delete the alien
                spaceship.deactivate() #delete the ship
                score.delete_ship(lives[0])  #delete the corrosponding life depending on the contents of lives
                lives.pop(0) #pops the first index so that it will delete life 1 then 2 then 3 
        
        for a in aliens:  #auto deletes for program speed 
            if not a.is_active():
                aliens.remove(a)
    
        for b in spacebooms:
            b.next()  #keeps explosions from hitting ship moving and removing from memory
            if not spaceship.is_active() and not b.is_active():
                spaceship.activate()
                spacebooms.remove(b)  #auto deletes past explosions for program speed 


        for b in booms:
            b.next()   #keeps explosions from hitting aliens moving and removing from memory
            if not b.is_active():
                booms.remove(b)  #auto deletes for program speed 
      

######################### KILL THE ALIENS AND ADD TO DICTIONARY ##################################
        for missy in missiles:
            for a in aliens:
                missy.next() #keep the missile moving  
                xmiss=missy.xcoord//1 #sets x coords to an int
                ymiss=missy.ycoord//1 #sets y coords to an int
                if ((a.xcoord)//1-a.w//2 <= xmiss <= (a.xcoord)//1+a.w//2) and ((a.ycoord)//1-a.h//2 <= ymiss <= (a.ycoord)//1+a.h//2): #if the missile hits the alien
                    missy.deactivate() #deactivate the missile
                    a.deactivate()  #deactivate the alien
                    Explosion.add_explosion(canvas,booms,missy.x,missy.y,30,a.color) #add an explosion on hit 
                    score.increment(inc=a.point) #add the corrosponding score to the score
                    ######################################################################
                    if a.color=='red':
                        record['red']+=1
                    elif a.color=='green':
                        record['green']+=1                       
                    elif a.color=='blue':  #adds hit aliens to dictionary 
                        record['blue']+=1           
                    elif a.color=='purple':
                        record['mine']+=1
                    #######################################################################3

        root.update()   # update the graphic (redraw)
        time.sleep(0.01)
        t=t+1
   
           
    root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

