from tkinter import *
import random
score=0
dinocoordx1=0
dinocoordx2=0
dinocoordy1=30
dinocoordy2=0
yVelocity=0
dinoscore=0
jump=-15
incactus=False
life=1

cactCoorX=1000

hs=open("highscore.txt",'r')
# if int(hs.read)>=0:
highscore=str(hs.read())
# else:
#     highscore=0
# hs.close()

root = Tk()    
frame = Frame(root)
frame.pack()
root.geometry("500x500")
multiplier=1
canjump=False
gravity=1
dinosprite=PhotoImage(file="dinosaur.png")
cactussprite=PhotoImage(file="cactus.png")


def jump(event):
    global yVelocity
    global jump
    if canjump==True:
        # yVelocity=-15
        jump=-10-5*((dinoscore)/100)
        
    
    


root.bind("<Key>",jump)


def spawnCactus(canv):
    cactus=Canvas(root)
    cactus.config(width=500,height=500)
    cactus.create_rectangle(50,50,100,100)
    cactus.pack()
    


def dino():
    
    clearscreen()
    global score
    global dinoscore
    global jump
    global canjump
    global gravity
    global cactCoorX
    global incactus
    cactCoorX-=10+(dinoscore/100)
    score+=1
    global yVelocity
    global dinocoordy1
    global dinocoordy2
    dinocoordy1+=yVelocity
    dinocoordy2+=yVelocity
    gameScore=Label(root,text="score: "+str(dinoscore))
    gameScore.pack()
    
    yVelocity+=gravity-0.5+(dinoscore/100)*gravity
    dinosaurgame=Canvas(root)
    
    dinosaurgame.config(width=500,height=500,bg="light blue")
    
    floor = dinosaurgame.create_rectangle(0,300,500,500,fill="#b8814d")
    dinosaurgame.create_rectangle(0,280,500,285,fill="#f1ff85",outline="#dfff87")
    dinosaurgame.create_rectangle(0,285,500,320,fill="#f5de82",outline="#f5de82")
    dinosaurgame.create_oval(10,310,30,300,fill="#b8814d",outline="#b8814d")
    dinosaur=dinosaurgame.create_image(20,dinocoordy2+20,image=dinosprite)
    
    
    cactus=dinosaurgame.create_image(cactCoorX,280,image=cactussprite)
    
    if random.randrange(1,20)==1 and cactCoorX<0:
        cactCoorX=500
        
        
    if (cactCoorX>=19-(dinoscore/2) and cactCoorX<=21+(dinoscore/2)) and dinocoordy2>=250:
        dinogameover()
    elif (cactCoorX>=19-(dinoscore/2) and cactCoorX<=21+(dinoscore/2)) and dinocoordy2<250:
        if(incactus==False):
            dinoscore+=1
        incactus=True
    else:
        incactus=False
    
    
    
    if dinocoordy1==300 or dinocoordy2==300:
        canjump=True
        yVelocity=jump
        gravity=0
    elif dinocoordy1>300 or dinocoordy2>300:
        canjump=True
        dinocoordy1=300
        dinocoordy2=270
        # yVelocity=-1+jump-int((dinoscore/1000))
        yVelocity=0
        gravity=0
    else:
        jump=0
        canjump=False
        gravity=1
    
    dinosaurgame.pack()

    root.after(10,dino)
    
def dinogameover():
    global dinoscore
    global hs
    global highscore
    clearscreen()
    score=Label(text="your score was "+str(dinoscore))
    score.pack()
    if dinoscore>int((highscore)):
        hs=open("highscore.txt",'w') 
        hs.write(str(dinoscore))
        hs.close()
        highscore=str(dinoscore)
    
    high=Label(root,text="the highscore was "+highscore)
    high.pack()
    
    dinoscore=0
    replay=Button(text="replay",command=dino)
    replay.pack()
    clicker=Button(text="return to clicker",command=Gamescreen)
    clicker.pack()


def clearscreen():
    for i in root.winfo_children():
        i.destroy()

def getmultip():
    global multiplier
    global score
    score-=50
    multiplier+=multiplier

def cookieClicked():
    global score
    score +=1*multiplier
    clearscreen()
    Gamescreen()


def Gamescreen():
    score 
    clearscreen()
    pointsFrame=LabelFrame(root,text="points:")
    pointsFrame.pack()
    points=Label(pointsFrame,text=score)
    points.pack()
    cookie=Button(root,text="imagine this is a cookie",command=cookieClicked)
    cookie.pack()
    gotoStore=Button(root,text="Store",command=StoreScreen)
    gotoDino=Button(root, text="Play dinosaur",command=dino)
    gotoDino.pack()
    gotoStore.pack()
    
    
def StoreScreen():
    clearscreen()
    heart=Button(root,text="heart")
    # powerup3=Button
    heart.pack()
    multip=Button(root,text="X2 multiplier: 50p",command=getmultip)
    multip.pack()
    game=Button(root,text="return to game",command=Gamescreen)
    game.pack()
    


Gamescreen()
root.mainloop()