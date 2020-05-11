import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title('GUI')
win.configure(bg='#f3c3fa')


#widgets --> label , buttons , radio buttons - tk , ttk (submodule of tkinter)
#create labels
name_label = ttk.Label(win , text ='Enter your name:')
# pack , grid to set where to place the label inside the win
name_label.grid(row = 0,column=0 , sticky=tk.W)

email_label = ttk.Label(win, text = 'Enter your email :')
email_label.grid(row = 1,column=0 , sticky=tk.W)

age_label = ttk.Label(win , text = 'Enter your age : ')
age_label.grid(row=2,column=0 , sticky=tk.W)

gender_label = ttk.Label(win , text='Enter your gender:')
gender_label.grid(row=3,column=0 , sticky=tk.W)

#create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win , width=16 , textvariable = name_var)
name_entrybox.grid(row = 0 , column = 1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=16,textvariable = email_var)
email_entrybox.grid(row=1,column = 1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)


#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win , width=13 , textvariable=gender_var , state='readonly')
gender_combobox['values'] = ('Male' , 'Female' , 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)


#radio button
user_type = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text='Student',value='Student', variable=user_type)
radiobtn1.grid(row=4 , column =0)
radiobtn2 = ttk.Radiobutton(win, text='Teacher' , value='Teacher' , variable=user_type)
radiobtn2.grid(row=4 , column=1)


#check button
checkbtn_var = tk.IntVar()
checkbtn=ttk.Checkbutton(win , text='check if you want to subscribe to our newsletter' , variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=3)


#create button

# def action():
#    username = name_var.get()
#    userage = age_var.get()
#    useremail = email_var.get()
#    print(f'{username} is {userage} , {useremail}')
#    usergender = gender_var.get()
#    usertype = user_type.get()
#    if checkbtn_var.get() == 0:
#        subscribed = 'No'
#    else:
#        subscribed = 'Yes'
#    print(usergender , usertype , subscribed)

#    with open('1st_GUI.txt','a') as f:
#        f.write(f'{username} , {userage} , {useremail} , {usergender} , {usertype} , {subscribed} \n')

#    name_entrybox.delete(0,tk.END)
#    age_entrybox.delete(0,tk.END)
#    email_entrybox.delete(0,tk.END)
 #   name_label.configure(foreground = 'Blue')
    #submit_button.configure(foreground = 'Cyan')

#write to csv file
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    usergender = gender_var.get()
    usertype = user_type.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'


    with open('1st_GUI.csv', 'a') as f:
        dict_writer = DictWriter(f,fieldnames=['User Name','User Email Address','User Age','User Gender','User Type' , 'Subscribed'])
        if os.stat('1st_GUI.csv').st_size==0:
                dict_writer.writeheader()


        dict_writer.writerow({
            'User Name' : username ,
            'User Email Address' : useremail ,
            'User Age' : userage ,
            'User Gender' : usergender ,
            'User Type' : usertype ,
            'Subscribed' : subscribed
        })


    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground = 'Blue')


submit_button=tk.Button(win,text = 'Submit' , command=action)
submit_button.grid(row=10 , column=0)



win.mainloop()

