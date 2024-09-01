from tkinter import *


my_screen=Tk()
my_screen.configure(background="green")
my_screen.title("BMİ CALCULATİON")
my_screen.minsize(width=400,height=400)
Font=("Arial",10,"bold")
#label1
my_label=Label(text="Enter Your Weight (kg)",font=Font)
my_label.place(x=90,y=30)
#label2
my_label2=Label(text="Enter Your Height (cm)",font=Font)
my_label2.place(x=90,y=80)


#entry1
def validate_number_input(P):
    # P, girilen değeri temsil eder
    if P == "" or P.isdigit():
        return True
    return False

validate_cmd = my_screen.register(validate_number_input)
my_entry=Entry(my_screen, validate="key", validatecommand=(validate_cmd, "%P"))
my_entry.place(x=130,y=60)
my_entry.config(border=0)
my_entry.focus()
#entry2
def validate_number_input(P):
    # P, girilen değeri temsil eder
    if P == "" or P.isdigit():
        return True
    return False

validate_cmd = my_screen.register(validate_number_input)
my_entry2=Entry(my_screen, validate="key", validatecommand=(validate_cmd, "%P"))
my_entry2.place(x=130,y=120)


#button
def mybutton_clicked():
    weight= float(my_entry.get())
    height = float(my_entry2.get()) / 100

    bmi = float(weight/height ** 2)
    bmi = round(bmi, 2)

    metin = ""
    if bmi<18:
        metin= "Cok zayıfsın kilo al lan zargana!!!"
    elif bmi>18 and bmi<25:
        metin="Formundasın HAA "
    elif bmi>25 and bmi<40:
        metin="Dikkat et  Dombili"
    else :
        metin=" ZAYIFLA LA ÖLECEN"



    my_label3.config(text=f"Vücut Kitle İndeksiniz : {bmi}, {metin}")



my_button=Button(text="Calculate",font=Font,command=mybutton_clicked)
my_button.place(x=130,y=150)

#label3

my_label3=Label()
my_label3.place(x=100,y=200)
my_screen.mainloop()

