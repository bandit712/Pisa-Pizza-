"""
Final Program SDEV 140 - Spring 2023
Pisa Pizza Ordering System
Kevin Cox 03/06/2023

JCT tinker with image sizes.
"""
from tkinter import *


window = Tk()
window.title("Pisa Pizza")
window.minsize(width=500, height=700)
window.configure(bg="tomato")


def button_clicked():
    cheese_total = int(cheese_sb.get()) * 8
    margherita_total = int(margherita_sb.get()) * 10
    caponata_total = int(caponata_sb.get()) * 12
    rib_total = int(rib_sb.get()) * 14
    meatball_total = int(meatball_sb.get()) * 14
    soppressata_total = int(soppressata_sb.get()) * 15
    total_bills = cheese_total + margherita_total + caponata_total + rib_total + meatball_total + soppressata_total
    bills = Label(text=f"Your Total Order: ${total_bills}", font=("Times New Roman", 18, "bold"), bg="tomato")
    bills.place(x=150, y=600)

def quit_clicked():
    window.destroy()

# Restaurant Name Label 1
resto_name = Label(text='WELCOME TO\nPISA PIZZA', font=("Times New Roman", 20, "bold"), bg="tomato")
resto_name.grid(column=1, row=0)

#Restaurant Quote Label 2
quote = Label(text="Artisan Pies, No Passport Needed!", font=("Times New Roman", 18 ,"italic"), bg="tomato")
quote.grid(column=1, row=2)

# Food Label
#food_label = Label(text="Choose Your Pizza", font=("Times New Roan", 12 , "normal"), bg="tomato")
#food_labe.grid(column=0, row=3)
# cheese (Food) Image = Info + Spinbox
#cheese = PhotoImage(file="..\pizza images gif\cheese.gif") #JCT was commented
#cheese = PhotoImage(file="pizza images gif\cheese.gif") #JCT access child folder
cheese = PhotoImage(file="pizza images gif\cheeseR.gif",
                    height=133,width=100)
               # original gif      810 X 1080 pixels)
                                      #JCT2 size
               # use the image viewer to resize (save as "R" file)
cheese_label = Label(image=cheese, borderwidth=0)
cheese_label.place(x=50, y=130)
cheese_info = Label(text="Four Cheese\n$8", font=("Times New Roman", 10 , "normal"), bg="tomato")
cheese_info.place(x=40, y=230)
cheese_sb = Spinbox(from_=0, to=10, width=5)
cheese_sb.place(x=80, y=270)
               
# Margherita (Food) Image = Info + Spinbox
margherita = PhotoImage(file="pizza images gif\margheritaR.gif",
                        height=133,width=100)       #JCT2
margherita_label = Label(image=margherita, borderwidth=0) #JCT2 uncomment
margherita_label.place(x=200, y=130)                      #JCT2 uncomment 
margherita_info = Label(text="Margherita\n$10", font=("Times New Roman", 10 , "normal"), bg="tomato")
margherita_info.place(x=210, y=230)
margherita_sb = Spinbox(from_=0, to=10, width=5)
margherita_sb.place(x=225, y=270)

# Caponata (Food) Image = Info + Spinbox
caponata = PhotoImage(file="pizza images gif\caponataR.gif",
                      height=133,width=100)
               # original gif      810 X 1080 pixels)
                                      #JCT2 size

caponata_label = Label(image=caponata, borderwidth=0)
caponata_label.place(x=350, y=130)
caponata_info = Label(text="Caponata\n$12", font=("Times New Roman", 10 , "normal"), bg="tomato")
caponata_info.place(x=350, y=230)
caponata_sb = Spinbox(from_=0, to=10, width=5)
caponata_sb.place(x=380, y=270)


# Rib (Food) Image = Info + Spinbox
rib = PhotoImage(file="pizza images gif\\ribR.gif",
                       height=133,width=100)  #JCT2 size

rib_label = Label(image=rib, borderwidth=0)
rib_label.place(x=50, y=380)
rib_info = Label(text="Shot Rib\n$14", font=("Times New Roman", 10 , "normal"), bg="tomato")
rib_info.place(x=40, y=480)
rib_sb = Spinbox(from_=0, to=10, width=5)
rib_sb.place(x=80, y=520)

# Meatball (Food) Image = Info + Spinbox
meatball = PhotoImage(file="pizza images gif\meatballR.gif")
meatball_label = Label(image=meatball, borderwidth=0)
meatball_label.place(x=200, y=380)
meatball_info = Label(text="Meatball\n$14", font=("Times New Roman", 10 , "normal"), bg="tomato")
meatball_info.place(x=225, y=480)
meatball_sb = Spinbox(from_=0, to=10, width=5)
meatball_sb.place(x=230, y=520)

# Soppressata (Food) Image = Info + Spinbox
soppressata = PhotoImage(file="pizza images gif\soppressataR.gif")
soppressata_label = Label(image=soppressata, borderwidth=0)
soppressata_label.place(x=350, y=380)
soppressata_info = Label(text="Soppressata\n$15", font=("Times New Roman", 10 , "normal"), bg="tomato")
soppressata_info.place(x=360, y=480)
soppressata_sb = Spinbox(from_=0, to=10, width=5)
soppressata_sb.place(x=375, y=520)

# Finish Button
finish = Button(text="Place Order", fg="green", command=button_clicked)
finish.place(x=210, y=560)

# Quit Buttton
quit= Button(text="Quit", fg="red", command=quit_clicked)
#quit_button = Button(root, text="Quit",  command=root.destroy)
quit.place(x=300, y=560)







                   

window.mainloop()
                                                
                                                


                                                
                  
