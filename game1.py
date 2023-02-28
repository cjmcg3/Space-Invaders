from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *


########## global variable
game_over=False

######### Functions

def stop_game():
    global game_over
    game_over=True

#initiate list for tuples to be collected
tuplelist=[]   

def shoot(canvas,aliens,booms,amunition,x,y,record):
    color = "white" #a miss is white 
    score=-3  #default score is -3 for a miss
    for a in aliens:
        if a.is_shot(x,y):
            a.deactivate() #if the alien is shot, deactivate it 
            color=a.color #and set the color of the explosion to the corrosponding alien color
            score=a.point #along with the corrosponding point increase value
            if a.color=='red':  ########################################################################################
                record['red']+=1
            elif a.color=='green':
                record['green']+=1                       
            elif a.color=='blue': #adds 1 to the dictionary value depending on the color of the alien hit based on the key 
                record['blue']+=1           
            elif a.color=='purple':
                record['mine']+=1######################################################################################
   #after checking for the alien hit, make an explosion of the color at the hit location, or white in miss location
    Explosion.add_explosion(canvas,booms,x,y,30,color)
    amunition.increment(score) #change score depending on hit or miss


################
    
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        amunition=Counter(canvas,10)
        ####### Dictionary initiazation
        record={'red':0,'green':0,'blue':0,'mine':0}
        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,amunition,e.x,e.y,record))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################

        t=0
        #To complete (time sleep is 0.01s)
        while True: 

            if t%100==0:
                #every 1 second append the aliens hit to the dictionary 
                tuplelist.append((record['red'],record['green'],record['blue'],record['mine']))

            if amunition.count <=0:
                stop_game() #if the score srops below 0 end the game 

            if game_over==True:
                f=open("game1.txt",'w') #create a new file 
                for i in range(len(tuplelist)):
                   f.write('%s %s %s %s\n'%(tuplelist[i][0],tuplelist[i][1],tuplelist[i][2],tuplelist[i][3])) #write the values of the tuple created in shoot
                f.close() 
                canvas.create_text(w/2,h/2,anchor=CENTER,text='GAME OVER',fill="red",font=("system",50)) #create GAME OVER message 
                print(record) #print dictionary results 
                for bye in root.bind(): #unbinds all of the keys so that once game is over, clicks dont chnage score anymore
                    root.unbind(bye)
                root.mainloop() #freeze the screen 


            if t%50==0:
                #every 0.5 seconds add an alien
                Alien.add_alien(canvas,aliens)
            
            for a in aliens:
                a.next() #keep the aliens moving

            for b in booms: #keep the explosions expanding 
                b.next()
         
            for e in aliens:
                if not e.is_active():# if the alien isnt active remove it from alien list so it isnt searched for anymore
                    aliens.remove(e)
        
                
            for b in booms:
                if b.is_active()==False: #remove explosions from list if false so it isnt searched for anymore
                    booms.remove(b)
            
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)
            t=t+1



          
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

