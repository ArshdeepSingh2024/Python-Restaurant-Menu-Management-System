from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib


# functionality Part

def clear():
    vegetablespringrollEntry.delete(0, END)
    paneertikkaEntry.delete(0, END)
    momosEntry.delete(0, END)
    chillipotatoEntry.delete(0, END)
    chickenwingsEntry.delete(0, END)
    chesseballsEntry.delete(0, END)

    daalfryEntry.delete(0, END)
    daalmakhaniEntry.delete(0, END)
    riceEntry.delete(0, END)
    butterpaneerEntry.delete(0, END)
    naanEntry.delete(0, END)
    rotiEntry.delete(0, END)

    kheerEntry.delete(0, END)
    rasgullaEntry.delete(0, END)
    gulabjamunEntry.delete(0, END)
    icecreamEntry.delete(0, END)
    rasmalaiEntry.delete(0, END)
    chocolavacakeEntry.delete(0, END)

    vegetablespringrollEntry.insert(0, 0)
    momosEntry.insert(0, 0)
    chesseballsEntry.insert(0, 0)
    chickenwingsEntry.insert(0, 0)
    chillipotatoEntry.insert(0, 0)
    paneertikkaEntry.insert(0, 0)

    daalfryEntry.insert(0, 0)
    daalmakhaniEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    butterpaneerEntry.insert(0, 0)
    naanEntry.insert(0, 0)
    rotiEntry.insert(0, 0)

    rasgullaEntry.insert(0, 0)
    kheerEntry.insert(0, 0)
    icecreamEntry.insert(0, 0)
    gulabjamunEntry.insert(0, 0)
    chocolavacakeEntry.insert(0, 0)
    rasmalaiEntry.insert(0, 0)

    STARTERStaxEntry.delete(0, END)
    MAINCOURSEtaxEntry.delete(0, END)
    DESSERTStaxEntry.delete(0, END)

    STARTERSpriceEntry.delete(0, END)
    MAINCOURSEpriceEntry.delete(0, END)
    DESSERTSpriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again', parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='black')
        root1.resizable(0, 0)

        senderFrame = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='black', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'), bg='black', fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry =Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='black', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='black', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='black', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='black', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,
                              width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t\t'))

        sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)

        root1.mainloop()


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'bill number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif STARTERSpriceEntry.get() == '' and MAINCOURSEpriceEntry.get() == '' and DESSERTSpriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products are selected')
    elif MAINCOURSEpriceEntry.get() == '0 Rs' and MAINCOURSEpriceEntry.get() == '0 Rs' and DESSERTSpriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No Products are selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n=======================================================')
        textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')
        if vegetablespringrollEntry.get() != '0':
            textarea.insert(END, f'\nVegetable Spring Roll\t\t\t{vegetablespringrollEntry.get()}\t\t\t{vegetablespringrollprice} Rs')
        if chesseballsEntry.get() != '0':
            textarea.insert(END, f'\nCheese Balls\t\t\t{chesseballsEntry.get()}\t\t\t{chesseballsprice} Rs')
        if chickenwingsEntry.get() != '0':
            textarea.insert(END, f'\nChicken Wings\t\t\t{chickenwingsEntry.get()}\t\t\t{chickenwingsprice} Rs')
        if momosEntry.get() != '0':
            textarea.insert(END, f'\nMomos\t\t\t{momosEntry.get()}\t\t\t{momosprice} Rs')
        if paneertikkaEntry.get() != '0':
            textarea.insert(END, f'\nPaneer Tikka\t\t\t{paneertikkaEntry.get()}\t\t\t{paneertikkaprice} Rs')
        if chillipotatoEntry.get() != '0':
            textarea.insert(END, f'\nChilli Potato\t\t\t{chillipotatoEntry.get()}\t\t\t{chillipotatoprice} Rs')

        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if butterpaneerEntry.get() != '0':
            textarea.insert(END, f'\nButter Paneer\t\t\t{butterpaneerEntry.get()}\t\t\t{butterpaneerprice} Rs')
        if naanEntry.get() != '0':
            textarea.insert(END, f'\nNaan\t\t\t{naanEntry.get()}\t\t\t{naanprice} Rs')
        if daalmakhaniEntry.get() != '0':
            textarea.insert(END, f'\nDaal Makhani\t\t\t{daalmakhaniEntry.get()}\t\t\t{daalmakhaniprice} Rs')
        if daalfryEntry.get() != '0':
            textarea.insert(END, f'\nDaal Fry\t\t\t{daalfryEntry.get()}\t\t\t{daalfryprice} Rs')
        if rotiEntry.get() != '0':
            textarea.insert(END, f'\nRoti\t\t\t{rotiEntry.get()}\t\t\t{rotiprice} Rs')

        if icecreamEntry.get() != '0':
            textarea.insert(END, f'\nIce Cream\t\t\t{icecreamEntry.get()}\t\t\t{icecreamprice} Rs')
        if rasmalaiEntry.get() != '0':
            textarea.insert(END, f'\nRas Malai\t\t\t{rasmalaiEntry.get()}\t\t\t{rasmalaiprice} Rs')
        if rasgullaEntry.get() != '0':
            textarea.insert(END, f'\nRasgulla\t\t\t{rasgullaEntry.get()}\t\t\t{rasgullaprice} Rs')
        if kheerEntry.get() != '0':
            textarea.insert(END, f'\nKheer\t\t\t{kheerEntry.get()}\t\t\t{kheerprice} Rs')
        if gulabjamunEntry.get() != '0':
            textarea.insert(END, f'\nGulab Jamun\t\t\t{gulabjamunEntry.get()}\t\t\t{gulabjamunprice} Rs')
        if chocolavacakeEntry.get() != '0':
            textarea.insert(END, f'\nChoco Lava Cake\t\t\t{chocolavacakeEntry.get()}\t\t\t{chocolavacakeprice} Rs')
        textarea.insert(END, '\n-------------------------------------------------------')

        if STARTERStaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nSTARTERS Tax\t\t\t\t{STARTERStaxEntry.get()}')
        if MAINCOURSEtaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nMAINCOURSE Tax\t\t\t\t{MAINCOURSEtaxEntry.get()}')
        if DESSERTStaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nDESSERTS Tax\t\t\t\t{DESSERTStaxEntry.get()}')
        textarea.insert(END, f'\n\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END, '\n-------------------------------------------------------')
        save_bill()


def total():
    global vegetablespringrollprice, chesseballsprice, chickenwingsprice, momosprice, paneertikkaprice, chillipotatoprice
    global riceprice, daalfryprice, butterpaneerprice, naanprice, daalmakhaniprice, rotiprice
    global rasmalaiprice, gulabjamunprice, rasgullaprice, chocolavacakeprice, kheerprice, icecreamprice
    global totalbill
    # STARTERS price calculation
    vegetablespringrollprice = int(vegetablespringrollEntry.get()) * 120
    momosprice = int(momosEntry.get()) * 80
    paneertikkaprice = int(paneertikkaEntry.get()) * 250
    chesseballsprice = int(chesseballsEntry.get()) * 150
    chickenwingsprice = int(chickenwingsEntry.get()) * 199
    chillipotatoprice = int(chillipotatoEntry.get()) * 130

    totalSTARTERSprice = vegetablespringrollprice + paneertikkaprice + momosprice + chickenwingsprice + chesseballsprice + chillipotatoprice
    STARTERSpriceEntry.delete(0, END)
    STARTERSpriceEntry.insert(0, f'{totalSTARTERSprice} Rs')
    STARTERStax = totalSTARTERSprice * 0.12
    STARTERStaxEntry.delete(0, END)
    STARTERStaxEntry.insert(0, str(STARTERStax) + ' Rs')

    # MAINCOURSE price calculation
    riceprice = int(riceEntry.get()) * 30
    daalfryprice = int(daalfryEntry.get()) * 125
    butterpaneerprice = int(butterpaneerEntry.get()) * 225
    naanprice = int(naanEntry.get()) * 50
    rotiprice = int(rotiEntry.get()) * 20
    daalmakhaniprice = int(daalmakhaniEntry.get()) * 175

    totalMAINCOURSEprice = riceprice + daalfryprice + butterpaneerprice + naanprice + rotiprice + daalmakhaniprice
    MAINCOURSEpriceEntry.delete(0, END)
    MAINCOURSEpriceEntry.insert(0, str(totalMAINCOURSEprice) + ' Rs')
    MAINCOURSEtax = totalMAINCOURSEprice * 0.05
    MAINCOURSEtaxEntry.delete(0, END)
    MAINCOURSEtaxEntry.insert(0, str(MAINCOURSEtax) + ' Rs')

    icecreamprice = int(icecreamEntry.get()) * 50
    rasmalaiprice = int(rasmalaiEntry.get()) * 30
    gulabjamunprice = int(gulabjamunEntry.get()) * 20
    rasgullaprice = int(rasgullaEntry.get()) * 25
    chocolavacakeprice = int(chocolavacakeEntry.get()) * 79
    kheerprice = int(kheerEntry.get()) * 150

    totalDESSERTSprice = icecreamprice + rasmalaiprice + gulabjamunprice + rasgullaprice + chocolavacakeprice + kheerprice
    DESSERTSpriceEntry.delete(0, END)
    DESSERTSpriceEntry.insert(0, str(totalDESSERTSprice) + ' Rs')
    DESSERTStax = totalDESSERTSprice * 0.08
    DESSERTStaxEntry.delete(0, END)
    DESSERTStaxEntry.insert(0, str(DESSERTStax) + ' Rs')

    totalbill = totalSTARTERSprice + totalMAINCOURSEprice + totalDESSERTSprice + STARTERStax + MAINCOURSEtax + DESSERTStax 

def logout():
    root.destroy()
    os.system('python login.py')
# GUI Part
root = Tk()
root.title('Restaurant Billing System')
root.geometry('1270x685')
headingLabel = Label(root, text='Restaurant Billing System', font=('times new roman', 30, 'bold')
                     , bg='black', fg='gold', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

logoutButton = Button(headingLabel, text='Logout', font=('arial', 14, 'bold')
                     , bd=3, width=8, pady=5, command=logout)
logoutButton.pack(side=RIGHT)

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'),
                                    fg='gold', bd=8, relief=GROOVE, bg='black')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='black',
                  fg='white')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='black',
                   fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='black',
                        fg='white')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='SEARCH',
                      font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

STARTERSFrame = LabelFrame(productsFrame, text='STARTERS', font=('times new roman', 15, 'bold'),
                            fg='gold', bd=8, relief=GROOVE, bg='black')
STARTERSFrame.grid(row=0, column=0)

vegetablespringrollLabel = Label(STARTERSFrame, text='Vegetable Spring Roll', font=('times new roman', 15, 'bold'), bg='black',
                      fg='white')
vegetablespringrollLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

vegetablespringrollEntry = Entry(STARTERSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
vegetablespringrollEntry.grid(row=0, column=1, pady=9, padx=10)
vegetablespringrollEntry.insert(0, 0)

momosLabel = Label(STARTERSFrame, text='Momos', font=('times new roman', 15, 'bold'), bg='black',
                       fg='white')
momosLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

momosEntry = Entry(STARTERSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
momosEntry.grid(row=1, column=1, pady=9, padx=10)
momosEntry.insert(0, 0)

paneertikkaLabel = Label(STARTERSFrame, text='Paneer Tikka', font=('times new roman', 15, 'bold'), bg='black',
                      fg='white')
paneertikkaLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

paneertikkaEntry = Entry(STARTERSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
paneertikkaEntry.grid(row=2, column=1, pady=9, padx=10)
paneertikkaEntry.insert(0, 0)

chesseballsLabel = Label(STARTERSFrame, text='Cheese Balls', font=('times new roman', 15, 'bold'), bg='black',
                       fg='white')
chesseballsLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

chesseballsEntry = Entry(STARTERSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
chesseballsEntry.grid(row=3, column=1, pady=9, padx=10)
chesseballsEntry.insert(0, 0)

chickenwingsLabel = Label(STARTERSFrame, text='Chicken Wings', font=('times new roman', 15, 'bold'), bg='black',
                     fg='white')
chickenwingsLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

chickenwingsEntry = Entry(STARTERSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
chickenwingsEntry.grid(row=4, column=1, pady=9, padx=10)
chickenwingsEntry.insert(0, 0)

chillipotatoLabel = Label(STARTERSFrame, text='Chilli Potato', font=('times new roman', 15, 'bold'), bg='black',
                        fg='white')
chillipotatoLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

chillipotatoEntry = Entry(STARTERSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
chillipotatoEntry.grid(row=5, column=1, pady=9, padx=10)
chillipotatoEntry.insert(0, 0)

MAINCOURSEFrame = LabelFrame(productsFrame, text='MAINCOURSE', font=('times new roman', 15, 'bold'),
                          fg='gold', bd=8, relief=GROOVE, bg='black')
MAINCOURSEFrame.grid(row=0, column=1)

riceLabel = Label(MAINCOURSEFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='black',
                  fg='white')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

riceEntry = Entry(MAINCOURSEFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0, 0)

butterpaneerLabel = Label(MAINCOURSEFrame, text='Butter Paneer', font=('times new roman', 15, 'bold'), bg='black',
                 fg='white')
butterpaneerLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

butterpaneerEntry = Entry(MAINCOURSEFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
butterpaneerEntry.grid(row=1, column=1, pady=9, padx=10)
butterpaneerEntry.insert(0, 0)

daalfryLabel = Label(MAINCOURSEFrame, text='Daal Fry', font=('times new roman', 15, 'bold'), bg='black',
                  fg='white')
daalfryLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

daalfryEntry = Entry(MAINCOURSEFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
daalfryEntry.grid(row=2, column=1, pady=9, padx=10)
daalfryEntry.insert(0, 0)

daalmakhaniLabel = Label(MAINCOURSEFrame, text='Daal Makhani', font=('times new roman', 15, 'bold'), bg='black',
                   fg='white')
daalmakhaniLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

daalmakhaniEntry = Entry(MAINCOURSEFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
daalmakhaniEntry.grid(row=3, column=1, pady=9, padx=10)
daalmakhaniEntry.insert(0, 0)

naanLabel = Label(MAINCOURSEFrame, text='Naan', font=('times new roman', 15, 'bold'), bg='black',
                   fg='white')
naanLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

naanEntry = Entry(MAINCOURSEFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
naanEntry.grid(row=4, column=1, pady=9, padx=10)
naanEntry.insert(0, 0)

rotiLabel = Label(MAINCOURSEFrame, text='Roti', font=('times new roman', 15, 'bold'), bg='black',
                 fg='white')
rotiLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

rotiEntry = Entry(MAINCOURSEFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
rotiEntry.grid(row=5, column=1, pady=9, padx=10)
rotiEntry.insert(0, 0)

DESSERTSFrame = LabelFrame(productsFrame, text='DESSERTS', font=('times new roman', 15, 'bold'),
                         fg='gold', bd=8, relief=GROOVE, bg='black')
DESSERTSFrame.grid(row=0, column=2)

icecreamLabel = Label(DESSERTSFrame, text='Ice Cream', font=('times new roman', 15, 'bold'), bg='black',
                   fg='white')
icecreamLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

icecreamEntry = Entry(DESSERTSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
icecreamEntry.grid(row=0, column=1, pady=9, padx=10)
icecreamEntry.insert(0, 0)

rasgullaLabel = Label(DESSERTSFrame, text='Rasgulla', font=('times new roman', 15, 'bold'), bg='black',
                   fg='white')
rasgullaLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

rasgullaEntry = Entry(DESSERTSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
rasgullaEntry.grid(row=1, column=1, pady=9, padx=10)
rasgullaEntry.insert(0, 0)

chocolavacakeLabel = Label(DESSERTSFrame, text='Choco Lava Cake', font=('times new roman', 15, 'bold'), bg='black',
                    fg='white')
chocolavacakeLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

chocolavacakeEntry = Entry(DESSERTSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
chocolavacakeEntry.grid(row=2, column=1, pady=9, padx=10)
chocolavacakeEntry.insert(0, 0)

gulabjamunLabel = Label(DESSERTSFrame, text='Gulab Jamun', font=('times new roman', 15, 'bold'), bg='black',
                 fg='white')
gulabjamunLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

gulabjamunEntry = Entry(DESSERTSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
gulabjamunEntry.grid(row=3, column=1, pady=9, padx=10)
gulabjamunEntry.insert(0, 0)

rasmalaiLabel = Label(DESSERTSFrame, text='Ras Malai', font=('times new roman', 15, 'bold'), bg='black',
                    fg='white')
rasmalaiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

rasmalaiEntry = Entry(DESSERTSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
rasmalaiEntry.grid(row=4, column=1, pady=9, padx=10)
rasmalaiEntry.insert(0, 0)

kheerLabel = Label(DESSERTSFrame, text='Kheer', font=('times new roman', 15, 'bold'), bg='black',
                      fg='white')
kheerLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

kheerEntry = Entry(DESSERTSFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
kheerEntry.grid(row=5, column=1, pady=9, padx=10)
kheerEntry.insert(0, 0)

billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'),
                           fg='gold', bd=8, relief=GROOVE, bg='black')
billmenuFrame.pack()

STARTERSpriceLabel = Label(billmenuFrame, text='STARTERS Price', font=('times new roman', 14, 'bold'), bg='black',
                           fg='white')
STARTERSpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

STARTERSpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
STARTERSpriceEntry.grid(row=0, column=1, pady=6, padx=10)

MAINCOURSEpriceLabel = Label(billmenuFrame, text='MAINCOURSE Price', font=('times new roman', 14, 'bold'), bg='black',
                          fg='white')
MAINCOURSEpriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

MAINCOURSEpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
MAINCOURSEpriceEntry.grid(row=1, column=1, pady=6, padx=10)

DESSERTSpriceLabel = Label(billmenuFrame, text='DESSERTS Price', font=('times new roman', 14, 'bold'), bg='black',
                         fg='white')
DESSERTSpriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

DESSERTSpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
DESSERTSpriceEntry.grid(row=2, column=1, pady=6, padx=10)

STARTERStaxLabel = Label(billmenuFrame, text='STARTERS Tax', font=('times new roman', 14, 'bold'), bg='black',
                         fg='white')
STARTERStaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

STARTERStaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
STARTERStaxEntry.grid(row=0, column=3, pady=6, padx=10)

MAINCOURSEtaxLabel = Label(billmenuFrame, text='MAINCOURSE Tax', font=('times new roman', 14, 'bold'), bg='black',
                        fg='white')
MAINCOURSEtaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

MAINCOURSEtaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
MAINCOURSEtaxEntry.grid(row=1, column=3, pady=6, padx=10)

DESSERTStaxLabel = Label(billmenuFrame, text='DESSERTS Tax', font=('times new roman', 14, 'bold'), bg='black',
                       fg='white')
DESSERTStaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

DESSERTStaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
DESSERTStaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='black', fg='white'
                     , bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='black', fg='white'
                    , bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='black', fg='white'
                     , bd=5, width=8, pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='black', fg='white'
                     , bd=5, width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='black', fg='white'
                     , bd=5, width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
