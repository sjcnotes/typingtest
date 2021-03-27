words=['ability','year','desire','about','sum','nothing','factory','users','problem','elephant','location','act','connections',
       'current','customer','long','people','large','database','hindi','urdu','police','chickballapur','among','confidence','hero','bihar','further','summary','document',
       'game','print','command','invalid','library','keyword','awesome','information','year']
from tkinter import *
import random
from tkinter import messagebox

def labelSlider():
    global count,sliderwords
    text = 'Welcome to Typing Speed Increaser Game'
    if(count >= len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150,labelSlider)
    
def time():
    global timeleft,score,miss
    if(timeleft >=11):
        pass
    else:
        timeLabelCount.configure(fg='red')
    if(timeleft>0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} or miss = {} or Total score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel("Notification","For play again hit retry button")
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timeLabelCount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
    
def startGame(event):
    global score,miss
    if(timeleft==60):
     time()
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordlabel["text"]):
        score += 1
        scoreLabelCount.configure(text=score)
        #print("Score",score)
    else:
        miss += 1
       # print("miss",miss)
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordEntry.delete(0,END)


#root methods
root=Tk()
root.geometry('800x600+400+30')
root.configure(bg='powder blue')
root.title("Developed by Raushan Kumar")
root.iconbitmap("")


#variables
score = 0
timeleft=60
count=0
sliderwords=''
miss=0







#label methods
fontlabel = Label(root,text='',font=('airal',25,'italic bold'),bg='powder blue',fg='red',width=40)
fontlabel.place(x=10,y=10)

labelSlider()
random.shuffle(words)


#word label
wordlabel=Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordlabel.place(x=350,y=200)



#score label
scoreLabel=Label(root,text='Your Score:',font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount=Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=10,y=180)

timerLabel=Label(root,text='Time left:',font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timerLabel.place(x=600,y=100)

timeLabelCount=Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLabelCount.place(x=680,y=180)


gamePlayDetailLabel=Label(root,text='Type word and hit Enter Button',font=('arial',30,'italic bold'),bg='powder blue',fg='dark green')
gamePlayDetailLabel.place(x=120,y=450)
#entry box
wordEntry=Entry(root,font=('airal',25,'italic bold'),bd=10,justify="center")
wordEntry.place(x=250,y=300)
wordEntry.focus_set()




root.bind("<Return>",startGame)

root.mainloop()