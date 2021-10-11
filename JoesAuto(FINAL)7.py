#Joe's automotive
#By, Jeff Bratanov
# 7/23/2019
# Apparently Joe fixes the cars I have to refuse!
#IMPORT MODUALS
import tkinter
from tkinter import *
from tkinter import messagebox
#GLOBAL VARIABLES, CONSTANTS, ETC

def TotalUp ():
    try:
        SERVICES = []
        TOTAL = 0
        SUBTOTAL = 0.00
        GRANDTOTAL = 0.00
        TAX = 0.00
        TAXRATE = .05
        LABORRATE = 50
        global PARTCOST
        global LABORHOURS
        global LABORCOST
        PART = PARTS.get()
        PARTSCOST = float(PART)
        LABORHOURS = LABOR.get()
        LABORCOST = float(LABORHOURS) * float(LABORRATE)
         #Run through check list
        if OIL.get() == 1:
            TOTAL += 30
            SERVICES.append("Oil change")
        if LUBE.get() == 1:
            TOTAL += 20
            SERVICES.append("Lube Job")
        if  RADIATOR.get() == 1:
            TOTAL += 40
            SERVICES.append("Radiator flush")
        if TRANSMISSION.get() == 1:
            TOTAL += 100
            SERVICES.append("Transmission flush")
        if INSPECTION.get() == 1:
            TOTAL += 30
            SERVICES.append("Inspection")
        if MUFFLER.get() == 1:
            TOTAL += 200
            SERVICES.append("Muffler replacement")
        if TIRES.get() == 1:
            TOTAL += 20
            SERVICES.append("Tire rotation")
         #Get details of Customer.
    
        CUSTNAME = CustName.get()
        CUSTADDRESS = CustAddr.get()
        CUSTPHONE = CustPhone.get()
       

         #Get details on car
        CAR = ""
        CARNUM = CARMAKE.get()
        if CARNUM == 0:
            messagebox.showinfo ("Joe's Automotive", "Please select a car make.")
            window.mainloop()
        if CARNUM == 1:
            CAR = "Porche"
        if CARNUM == 2:
            CAR = "Mercedes"
        if CARNUM == 3:
            CAR = "BMW"
        YEAR = CARYEAR.get()    
        SUBTOTAL = float(TOTAL) + float(PARTSCOST) + float(LABORCOST)
        TAX = float(TAXRATE) * float(SUBTOTAL)
        GRANDTOTAL = float(TAX) + float(SUBTOTAL)
        #This is where the invoice would go into a database and or printer.
        #A autogenerated PK and datetime would most likely be used as those are the only reliable primary key in this situation.
        #Possibly a place for the mechanic to add notes about the repair too.
        invoice=Tk()
        invoice.title("Joe's Automotive Repair Invoice")
        Label (invoice, text="Joe's Automotive Repair Invoice", font="none 18 bold") .grid(row=0, column=0, sticky=W)
        Label (invoice, text="Customer : "+ CUSTNAME). grid(row=1, column=0, sticky=W)
        Label (invoice, text="Address : " + CUSTADDRESS). grid(row=2, column=0, sticky=W)
        Label (invoice, text="Phone :\n" + CUSTPHONE) . grid(row=2, column=1, sticky=W)
        Label (invoice, text="Car : " + YEAR + " " + CAR + "."). grid(row=3, column=0, sticky=W)
        Label (invoice, text="Services : ") . grid(row=4, column=0, sticky=W)
        Label (invoice, text=SERVICES). grid(row=5, column=0, sticky=W)
        Label (invoice, text="Parts : $") . grid(row=6, column=0, sticky=E)
        Label (invoice, text=("%.2f" %PARTSCOST)) .grid(row=6, column=1, sticky=W)
        Label (invoice, text="Labor :$") . grid(row=7, column=0, sticky=E)
        Label (invoice, text=("%.2f" %LABORCOST)) . grid(row=7, column=1, sticky=W)
        Label (invoice, text="Subtotal :$") . grid(row=8, column=0, sticky=E)
        Label (invoice, text=("%.2f" %SUBTOTAL)) . grid(row=8, column=1, sticky=W)
        Label (invoice, text="Tax :$") . grid(row=9, column=0, sticky=E)
        Label (invoice, text=("%.2f" %TAX)) . grid(row=9, column=1, sticky=W)
        Label (invoice, text="Grand Total:$", font="none 16 bold") . grid(row=10, column=0, sticky=E)
        Label (invoice, text=("%.2f" %GRANDTOTAL), font="none 16 bold") . grid(row=10, column=1, sticky=W)
        invoice.mainloop()
    except:
        #Error messagebox to make sure all fields are filled and error free. Runs main window again.
        #Program will not preceed until all crutial values are entered.
        messagebox.showinfo("Joe's Automotive", "Please check all fields.")
        window.mainloop()
       

#Main window for filling out invoice
window=Tk()
window.title("Joe's Automotive")
window.configure(background="darkturquoise")
#Title label
Label (window, text="Joe's Automotive", bg="blue", fg="cyan", font="none 18 bold") .grid(row=0,column=0, sticky=W)
Label (window, text="Where prices are low,\nDouble if you watch,\nand tripple if you help!", bg="blue", fg="cyan", font="none 10 italic") .grid(row=1,column=0, sticky=W)
#Customer name input
Label (window, text="   Customer's Name: ", bg="darkturquoise", fg="navy", font="none 12 bold") .grid(row=3,column=0, sticky=E)
CustName = Entry(window, width=20, bg="white")
CustName.grid(row=3, column=1, sticky=W)
#Customer address input
Label (window, text="   Customer's Address: ", bg="darkturquoise", fg="navy", font="none 12 bold") .grid(row=4,column=0, sticky=E)
CustAddr = Entry(window, width=20, bg="white")
CustAddr.grid(row=4, column=1, sticky=W)
#Customer phone input
Label (window, text="   Customer's Phone: ", bg="darkturquoise", fg="navy", font="none 12 bold") .grid(row=5,column=0, sticky=E)
CustPhone = Entry(window, width=20, bg="white")
CustPhone.grid(row=5, column=1, sticky=W)
#Car Make Radiobuttons
Label (window, text="    Select Car Make: ", bg="darkturquoise", fg="navy", font="none 10 bold") .grid(row=6,column=0, sticky=E)
CARMAKE = IntVar()
rd1 = Radiobutton(window, text="Porche",bg="darkturquoise", variable=CARMAKE, value=1) .grid(row=6,column=1, sticky=W)
rd2 = Radiobutton(window, text="Mercedes", bg="darkturquoise", variable=CARMAKE, value=2) .grid(row=6, column=1, sticky=E)
rd2 = Radiobutton(window, text="BMW", bg="darkturquoise", variable=CARMAKE, value=3) .grid(row=6, column=2, sticky=W)
#Car Year input
Label (window, text="   Vehicle Year: ", bg="darkturquoise", fg="navy", font="none 10 bold") .grid(row=7,column=0, sticky=E)
CARYEAR = Entry(window, width=20, bg="white")
CARYEAR.grid(row=7, column=1, sticky=W)
#Checkboxes for services rendered
Label (window, text=" Services Rendered: ", bg="darkturquoise", fg="navy", font="none 10 bold") .grid(row=8,column=0, sticky=W)
OIL = IntVar()
Checkbutton (window, text="Oil Change:           $30", bg="darkturquoise", variable=OIL) .grid(row=9,  sticky=W)
LUBE = IntVar()
Checkbutton (window, text="Lube Job:             $20", bg="darkturquoise", variable=LUBE). grid(row=10, column=0, sticky=W)
RADIATOR = IntVar()
Checkbutton (window, text="Radiator Flush:       $40",bg="darkturquoise", variable=RADIATOR). grid(row=11, column=0, sticky=W)
TRANSMISSION = IntVar()
Checkbutton (window, text="Transmission Flush:  $100",bg="darkturquoise", variable=TRANSMISSION). grid(row=12, column=0, sticky=W)
INSPECTION = IntVar()
Checkbutton (window, text="Inspection:           $35",bg="darkturquoise", variable=INSPECTION). grid(row=13, column=0, sticky=W)
MUFFLER = IntVar()
Checkbutton (window, text="Muffler Replacement: $200",bg="darkturquoise", variable=MUFFLER). grid(row=14, column=0, sticky=W)#Checkbutton (window, text="Tire Rotation\n$20", variable=TIRES). grid(row=7, column=6, sticky=W)
TIRES = IntVar()
Checkbutton (window, text="Tire Rotation:        $20",bg="darkturquoise", variable=TIRES). grid(row=15, column=0, sticky=W)
#Parts input
Label (window, text="   Parts Cost: ", bg="darkturquoise", fg="navy", font="none 10 bold") .grid(row=16,column=0, sticky=E)
PARTS = Entry(window, width=20, bg="white")
PARTS.grid(row=16, column=1, sticky=W)
#Labor input
Label (window, text=" Labor Hours : ", bg="darkturquoise", fg="navy", font="none 10 bold") .grid(row=17,column=0, sticky=E)
LABOR = Entry(window, width=20, bg="white")
LABOR.grid(row=17, column=1, sticky=W)
#Submit buttons and invoice creation
Button(window, text="SUBMIT", width=6, command=TotalUp) .grid(row=19, column=1, sticky=W)
Button(window, text="QUIT", width=6, command=window.destroy) .grid(row=19, column=0, sticky=E)
#Runs the GUI
window.mainloop()
