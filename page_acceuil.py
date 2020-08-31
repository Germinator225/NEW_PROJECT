from tkinter import *
Width= 1900
Height= 800
#--------------------------------------------------------------------------------------------------------------------

def video():
    fene2 = Tk()
    fene2.wm_state(newstate="zoomed")
    root.destroy()
    canvas = Canvas(fene2, bg='#006D80', width=Width, height=Height)
    canvas.pack()
#--------------------------------------------------------------------------------------------------------------------

root= Tk()
root.wm_state(newstate="zoomed")
root.title("PAGE D'ACCEUIL 2020")
canvas= Canvas(root, width= Width, height=Height, bg='#3D3D37' )
photo=PhotoImage(file='logoinp.gif')
canvas.create_image(38,38,image=photo)
canvas.pack()
label= Label(root, text='BIENVENUE AU BINOMAGE\n'+' ITA P-45 2020', fg='white', bg='#3D3D37', font=("arial", 60, "bold"))
label.place(x=190, y=250)

#--------------------------------------------------------------------------------------------------------------------

button1= Button(root, text='presentation', command=video, bg='white', fg='blue')
button1.place(x= 1250, y= 650)
root.mainloop()
