#importing necessary libraries
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import sqlite3 as sq
import pandas as pd
import numpy as np
from math import ceil
import re #regular expressions for quick search
import random



#pre functions
#existing user
def exuserpre(widget):
    '''This pre function is for accessing exuser() function.'''
    widget.destroy()
    exuser()
#new user
def newuserpre(widget):
    '''This pre function is for accessing newusers() function.'''
    widget.destroy()
    newusers()
#admin login
def adminpre(widget):
    '''This pre function is for accessing adminlogin() function.'''
    widget.destroy()
    adminlogin()
#track package
def trackpre(widget):
    '''This pre function is for accessing track() function.'''
    widget.destroy()
    track()
#cost estimator
def costpre(widget):
    '''This pre function is for accessing costestm() function.'''
    widget.destroy()
    costestm()
#feedback
def feedbackpre(widget):
    '''This pre function is for accessing feedback() function.'''
    widget.destroy()
    feedback()
    
def locationpre(widget):
    '''This pre function is for accessing location() function.'''
    widget.destroy()
    location()    
    
#back
def back(widget):
    '''This is function for going back to previous window.'''
    widget.destroy()
    mainscreen()
#side icons
def sideback(w):
    '''This function is for top right back icon.'''
    #rhs buttons & icons
    backimg = Image.open("Back.png")
    backrender = ImageTk.PhotoImage(backimg)
    bimg = Button(w, image = backrender, command = lambda: back(w), bd = 0)
    bimg.image = backrender
    bimg.place(relx = .02, rely = .04)
def sideexit(w):
    '''This function is for top right exit icon.'''
    #exit image
    exitimg = Image.open("Exit.png")
    exitrender = ImageTk.PhotoImage(exitimg)
    eimg = Button(w, image = exitrender, command = w.destroy, bd = 0)
    eimg.image = exitrender
    eimg.place(relx = .95, rely = .03)
def sideicons(w):
    '''This function is for top right icons.'''
    sideback(w)
    sideexit(w)


def mainscreen():
    '''This function is for creation of mainscreen, placing all elements on it and for creation of required databases.'''
    ms = Tk()
    ms.title("Home Screen")
    ms.attributes('-fullscreen',True)
    ms.configure(bg='palevioletred')
    
    #img= PhotoImage(file='front.png', master= ms)
    #creating the database
    #cmsuser
    conn = sq.connect('cmsuser.db') #creates file (if not exists)
    conn.execute('''Create table if not exists cmsuser
        (username varchar(20) not null unique,
        regno number(8) not null,
        gender char(6) not null,
        mobile number(10) not null,
        email char(25) not null,
        password varchar(25) not null);''')
    conn.close()
    #cmsfeed
    conn = sq.connect('cmsfeed.db') #creates file (if not exists)
    conn.execute('''Create table if not exists cmsfeed
        (email varchar(25) not null,
        feedback varchar(500) not null);''')
    conn.close()
    #cmsreq
    conn = sq.connect('cmsreq.db')
    conn.execute('''create table if not exists cmsreq
        (username varchar(20) not null,
        regno number(8) not null, 
        mobile number(10) not null,
        courierto char(50) not null,
        weight number(7) not null,
        distance number(6) not null,
        deltype char(15) not null,
        consnum number(7) not null unique,
        status char(10) not null);''')
    conn.close()
    #heading
    #mswelcome1 = Label(ms,text='Welcome to')
    mswelcome2 = Label(ms,text='Digital Santa',fg='purple', bg='pink')
    #mswelcome1.config(font=('Sans-serif',32,'bold'))
    mswelcome2.config(font=('Times',50,'bold italic'))
    #mswelcome1.pack()
    mswelcome2.pack()
    sideexit(ms)
    #new user, register, track, feedback buttons
    userbtn = Button(ms, text = "New User", command = lambda: newuserpre(ms), font = ('arial', 13), bd = 3)
    exuserbtn = Button(ms, text = "Existing User", command = lambda: exuserpre(ms), font = ('arial', 13), bd = 3)
    adminbtn = Button(ms, text = "Admin Login", command = lambda: adminpre(ms), font = ('arial', 13), bd = 3)
    trackbtn = Button(ms, text="Article Tracking", command = lambda: trackpre(ms), font = ('arial', 13), bd = 3)
    feedbtn = Button(ms, text = "Feedback", command = lambda: feedbackpre(ms), font = ('arial', 13), bd = 3)
    costbtn = Button(ms, text = "Postage Calculator", command = lambda: costpre(ms), font = ('arial', 13), bd = 3)
    locbtn = Button(ms, text = "Search Post Office", command = lambda: locationpre(ms), font = ('arial', 13), bd = 3)

    #homepage icons
    #new user    
    userimg = Image.open("newuser.png")
    userrender = ImageTk.PhotoImage(userimg)
    #existing user (register)
    exuserimg = Image.open("exuser.png")
    exuserrend = ImageTk.PhotoImage(exuserimg)
    #admin
    adminimg = Image.open("admin.png")
    adminrend = ImageTk.PhotoImage(adminimg)
    #track
    trackimg = Image.open("track.jpg")
    trackrend = ImageTk.PhotoImage(trackimg)
    #feedback
    feedimg = Image.open("feed.png")
    feedrend = ImageTk.PhotoImage(feedimg)
    #cost estimator
    costimg = Image.open("cost.png")
    costrend = ImageTk.PhotoImage(costimg)
    
    locimg = Image.open("loc.jpg")
    locrend = ImageTk.PhotoImage(locimg)
    #alignment of images on screen
    #new user
    nuimg = Label(image = userrender)
    nuimg.image = userrender
    #existing user
    euimg = Label(image = exuserrend)
    euimg.image = exuserrend
    #admin
    adimg = Label(image = adminrend)
    adimg.image = adminrend
    #track
    trimg = Label(image = trackrend)
    trimg.image = trackrend
    #feedback
    fdimg = Label(image = feedrend)
    fdimg.image = feedrend
    #cost estimator
    cstimg = Label(image = costrend)
    cstimg.image = costrend
    
    loimg = Label(image = locrend)
    loimg.image = locrend
    #alignment of icons
    nuimg.place(relx = .25, rely = .34, anchor = CENTER)
    euimg.place(relx = .50, rely = .34, anchor = CENTER)
    adimg.place(relx = .75, rely = .34, anchor = CENTER)
    trimg.place(relx = .25, rely = .63, anchor = CENTER)
    fdimg.place(relx = .75, rely = .63, anchor = CENTER)
    cstimg.place(relx = .50, rely = .63, anchor = CENTER)
    loimg.place(relx = .100, rely = .45, anchor = CENTER)
    #corresponding buttons
    userbtn.place(relx = .25, rely = .44, anchor = CENTER)
    exuserbtn.place(relx = .50, rely = .44, anchor = CENTER)
    adminbtn.place(relx = .75, rely = .44, anchor = CENTER)
    trackbtn.place(relx = .25, rely = .75, anchor = CENTER)
    costbtn.place(relx = .50, rely = .75, anchor = CENTER)
    feedbtn.place(relx = .75, rely = .73, anchor = CENTER)
    locbtn.place(relx = .100, rely = .60, anchor = CENTER)
    #keep the ms window open
    ms.mainloop()
    
def location():
#-------------------------------------------
    
    locationw = Tk()
    locationw.title("Login to Digital santa")
    locationw.attributes('-fullscreen', True)
    locationw.configure(bg='skyblue')
    
    loimg = Image.open("loc1.jpg")
    locrend = ImageTk.PhotoImage(loimg)
    uimg = Label(image = locrend)
    uimg.image = locrend
    uimg.place(relx = .200, rely = .20, anchor = N)
    
    log = Label(locationw, text = 'Location', font = ('Script-typeface', 25, 'bold'))
    log.place(relx = .600, rely = .30, anchor = S)
    sideicons(locationw)
    
#    log = Label(locationw, text = 'Search location', font = ('Script-typeface', 25, 'bold'))
#    log.place(relx = .5, rely = .20, anchor = N)
#    sideicons(locationw)
    
    
    l = Label(text = "Your Location").place(x = 760, y = 320)
#    l.place(relx = .5, rely = .30, anchor = N)
    inputtxt = Text(locationw, height = 10,
                    width = 25,
                    bg = "light yellow")
    inputtxt.place(relx = .600, rely = .50, anchor=CENTER)
        
#    Output = Text(locationw, height = 10,
#                    width = 25,
#                    bg = "light cyan")
    Output = Entry(locationw, width = 40, bd = 2, font = ('arial', 14))
    Output.place(relx = .600, rely = .70, anchor=CENTER)
    
    Display = Button(locationw, height = 2,
                     width = 20,
                     text ="Search",bg = 'darkblue',fg = 'white',
                     command = lambda:Take_input())
    Display.place(relx = .600, rely = .80, anchor = CENTER)
#    scrolW = 80
#    scrolH = 13
##    inputtxt = scrolledtext.ScrolledText(locationw, width = scrolW, height = scrolH, font = ('arial', 14), wrap = WORD)  
##    inputtxt.place(relx = .5, rely = .47, anchor = N)
#    
#    Output = scrolledtext.ScrolledText(locationw, width = scrolW, height = scrolH, font = ('arial', 14), wrap = WORD)  
#    Output.place(relx = .5, rely = .47, anchor = N)
#    
#    v = StringVar()
#    v.set(1)
##    

    def Take_input():
    #def Take_input():
        INPUT = inputtxt.get("1.0", "end-1c")
        print(INPUT)
            
            
            
        #l = Label(text = "Search Near by Location")    
        if(INPUT == "Avaniyapuram"):
            Output.insert(END, 'Near by Periyar Nagar Road')
        elif(INPUT == "Theppakulam"):
            Output.insert(END, 'Near by suguna store')
        elif(INPUT == "Mahal"):
            Output.insert(END, 'Near by keela vasal')
        else:
            Output.insert(END, "Enter your Location....")
     
 
     

     

    
    l.pack()
    inputtxt.pack()
    Display.pack()
    Output.pack()
    locationw.mainloop()
    
    
    
    
#---------------------------------------------    
#    varr = StringVar()
#    gender = Label(locationw, text = 'Gender:', font = ('arial', 14))
#    gender.place(relx = .34, rely = .46, anchor = W)
#    M = Radiobutton(locationw, text = 'Male', variable = varr, value = 'Male', font = ('verdana pro', 13))
#    M.focus_set()
#    F = Radiobutton(locationw, text = 'Female', variable = varr, value = 'Female', font = ('verdana pro', 13))
#    M.place(relx = .53, rely = .46, anchor = CENTER)
#    F.place(relx = .60, rely = .46, anchor = CENTER)
#    submit = Button(locationw, text = 'Submit',  command = loccheck, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white')
#    submit.place(relx = .57, rely = .60, anchor = CENTER)
# ------------------------------------------------   
#    ty = Label(locationw, text = 'search Near by Location:', font = ('arial', 14))
#    ty.place(relx = .33, rely = .34, anchor = W)
#    deltype = Combobox(locationw, font=('Arial', 14))
#    deltype['values'] = ['Avaniyapuram', 'Theppakulam','Mahal']
#    deltype.current(0)
#    print(deltype['values'])
#    print(deltype.current(0))
#   
#    deltype.place(relx = .55, rely = .54, anchor = W)
#   # print(deltype['values'])
#    deltype.place(relx = .55, rely = .34, anchor = W)
#    
#    def ShowChoice():
#        print(v.get())
#---------------------------------------------------  
#    def ShowChoice():
#        print(v.get())
    
#    aw = Label(locationw, text = 'Please Give Your Feedback:', font = ('arial', 14))
#    aw.place(relx = .10, rely = .23, anchor = W)
#    scrolW = 80
#    scrolH = 10
#    feed = scrolledtext.ScrolledText(locationw, width = scrolW, height = scrolH, font = ('arial', 14), wrap = WORD)  
#    feed.place(relx = .5, rely = .47, anchor = N)
#    
#    def checkloc():
#        str1 = ty.get()
#        print(str1)
#    def loccheck():
#        strr = varr.get()
#        print(strr)
##    uname = Label(locationw, text = 'Search Distrist:', font = ('arial', 14))
#    uname.place(relx = .37, rely = .4, anchor = W)
#    username = Entry(locationw, width = 20, bd = 2, font = ('arial', 14))
#    username.place(relx = .65, rely = .4, anchor = CENTER)
#    username.focus_set()
    
#    submit = Button(locationw, text = 'Submit',  command = locationpre, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white')
##    submit.place(relx = .57, rely = .60, anchor = CENTER)
#    list = Listbox(locationw, selectmode = "multiple")
#    list.pack(expand = YES, fill = "both")
#    x = ["C", "C++", "Java", "Python", "R",
#     "Go", "Ruby", "JavaScript", "Swift"]
#  
#import tkinter as tk
#
#root = tk.Tk()
#
#v = tk.IntVar()
#v.set(1)  # initializing the choice, i.e. Python
#
#languages = [("Python", 101),
#   	     ("Perl", 102),
#    	     ("Java", 103),
#             ("C++", 104),
#             ("C", 105)]
#
#def ShowChoice():
#    print(v.get())
#
#tk.Label(root, 
#         text="""Choose your favourite 
#programming language:""",
#         justify = tk.LEFT,
#         padx = 20).pack()
#
#for language, val in languages:
#    tk.Radiobutton(root, 
#                   text=language,
#                   padx = 20, 
#                   variable=v, 
#                   command=ShowChoice,
#                   value=val).pack(anchor=tk.W)   
      
      
    # coloring alternative lines of listbox
#    list.itemconfig(each_item,
#             bg = "yellow" if each_item % 2 == 0 else "cyan")
      
   
#    def checklocation():
#        Madurai=["TMB","INDIAN"]
    
#Existing User (Login) window
    



def exuser():
    '''This is function for login for existing user of CMS.'''
    loginw = Tk()
    loginw.title("Login")
    loginw.attributes('-fullscreen', True)
    loginw.configure(bg='mediumaquamarine')
    #headings
    log = Label(loginw, text = 'Login', font = ('Script-typeface', 25, 'bold'))
    log.place(relx = .5, rely = .20, anchor = N)
    sideicons(loginw)    
    #login icon
    userimg = Image.open("exuser.png")
    userrender = ImageTk.PhotoImage(userimg)
    uimg = Label(image = userrender)
    uimg.image = userrender
    uimg.place(relx = .5, rely = .05, anchor = N)
    #entries
    #login entry
    uname = Label(loginw, text = 'Username:', font = ('arial', 14))
    uname.place(relx = .37, rely = .4, anchor = W)
    username = Entry(loginw, width = 20, bd = 2, font = ('arial', 14))
    username.place(relx = .55, rely = .4, anchor = CENTER)
    username.focus_set()
    #password entry
    pswrd = Label(loginw, text = 'Password:', font = ('arial', 14))
    pswrd.place(relx = .37, rely = .47, anchor = W)
    password = Entry(show = "*", width = 20, bd = 2, font = ('arial', 14))
    password.place(relx = .55, rely = .47, anchor = CENTER)
    #login validator
    def checklogin():
        str1 = username.get()
        str2 = password.get()
        conn = sq.connect("cmsuser.db")
        c = conn.cursor()
        c.execute("select * from cmsuser where username = '%s' and password = '%s'" % (str1, str2))
        if c.fetchone() is not None:
            loginw.destroy()
            homepage()
        else:
            messagebox.showerror('Failure','Please enter valid Username and Password')
        conn.close()
    #submit button
    submit = Button(loginw, text = "Submit", command = checklogin, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white')
    submit.place(relx = .55, rely = .55, anchor = CENTER)
    #extra button for redirecting to register
    Label(loginw, text = "Don't have Digital santa account! Create a new account: ", font = ('Roboto', 12)).place(relx = .34, rely = .65, anchor = W)
    newuser = Button(loginw, text = "Register", command = lambda: newuserpre(loginw), font = ('Roboto', 13))
    newuser.place(relx = .60, rely = .65, anchor = W)
    #keep login window opened
    loginw.mainloop()

#New User (register) window
def newusers():
    '''This is function for creation of new users and adding their data to database.'''
    new = Tk()
    new.title("Register")
    new.attributes('-fullscreen', True)
    new.configure(bg='cyan')
    #headings
    log = Label(new, text = 'Register', font = ('Script-typeface', 23, 'bold'))
    log.place(relx = .5, rely = .19, anchor = N)
    sideicons(new)
    #register icon
    userimg = Image.open("newuser.png")
    userrender = ImageTk.PhotoImage(userimg)
    uimg = Label(image = userrender)
    uimg.image = userrender
    uimg.place(relx = .5, rely = .04, anchor = N)
    #entries
    #username entry
    username1 = StringVar() #for getting username
    uname = Label(new, text = 'Username:', font = ('arial', 14))
    uname.place(relx = .34, rely = .32, anchor = W)
    username = Entry(new, width = 20, bd = 2, font = ('roboto', 16))
    username.place(relx = .57, rely = .32, anchor = CENTER)
    username.focus_set()
    
    #registration no. entry
    reg = Label(new, text = 'Registration No:', font = ('arial', 14))
    reg.place(relx = .34, rely = .39, anchor = W)
    regno1 = IntVar()
    regno = Entry(new, width = 20, bd = 2, font = ('roboto', 16))
    regno.place(relx = .57, rely = .39, anchor = CENTER)
    #gender
    var = StringVar()
    gender = Label(new, text = 'Gender:', font = ('arial', 14))
    gender.place(relx = .34, rely = .46, anchor = W)
    M = Radiobutton(new, text = 'Male', variable = var, value = 'Male', font = ('verdana pro', 16))
    M.focus_set()
    F = Radiobutton(new, text = 'Female', variable = var, value = 'Female', font = ('verdana pro', 16))
    M.place(relx = .53, rely = .46, anchor = CENTER)
    F.place(relx = .60, rely = .46, anchor = CENTER)
    #mobile number
    ph = Label(new, text = 'Mobile No:', font = ('arial', 14))
    ph.place(relx = .34, rely = .53, anchor = W)
    phone = Entry(new, width = 20, bd = 2, font = ('roboto', 16))
    phone.place(relx = .57, rely = .53, anchor = CENTER)
    #email
    eml = Label(new, text = 'E-mail:', font = ('arial', 14))
    eml.place(relx = .34, rely = .60, anchor = W)
    #phone1 = IntVar()
    email = Entry(new, width = 20, bd = 2, font = ('roboto', 16))
    email.place(relx = .57, rely = .60, anchor = CENTER)
    #password entry
    pass1 = StringVar()
    pswrd1 = Label(new, text = 'Password:', font = ('arial', 14))
    pswrd1.place(relx = .34, rely = .67, anchor = W)
    password1 = Entry(show = "*", width = 20, bd = 2, font = ('roboto', 16))
    password1.place(relx = .57, rely = .67, anchor = CENTER)
    #re-enter password
    pass2 = StringVar()
    pswrd2 = Label(new, text = 'Re-enter Password:', font = ('arial', 14))
    pswrd2.place(relx = .34, rely = .74, anchor = W)
    password2 = Entry(show = "*", width = 20, bd = 2, font = ('roboto', 16))
    password2.place(relx = .57, rely = .74, anchor = CENTER)
    
    #submit checker
    def checknew():
        str1 = username.get()
        str2 = regno.get()
        str3 = var.get()
        print(str3)
        str4 = phone.get()
        str5 = email.get()
        str6 = password1.get()
        str7 = password2.get()
        dk1, dk2, dk4, dk5, dk6, dk7 = 0,0,0,0,0,0
        if str1 and str2 and str3 and str4 and str5 and str6 and str7:
            if len(str1) < 6 or len(str1) > 15:
                messagebox.showerror('Failure', 'Username must contain characters between 6 and 20')
                dk1 = 1
            elif re.search('[a-zA-Z]', str2) or len(str2) != 8: # or re.search('[A-Z]', str2):
                messagebox.showerror('Failure', 'Registration number must only contain 8 digits!')
                dk2 = 1
            elif len(str4) != 10 or re.search('[a-zA-Z]', str4):
                messagebox.showerror('Failure', 'Phone number should contain only 10 digits!')
                dk4 = 1
            elif re.search('[@]', str5) is None:
                messagebox.showerror('Failure', 'Please enter valid Email')
                dk5 = 1
            elif len(str6) < 8:
                messagebox.showerror('Failure', 'Password must contain at least 8 characters!')
                dk6 = 1
            elif str6 != str7:
                messagebox.showerror('Failure', "Password doesn't match!")
                dk7 = 1
            if dk1 == 0 and dk2 == 0 and dk4 == 0 and dk5 == 0 and dk6 == 0 and dk7 == 0:
                #changing data types
                #str1 = str(str1)
                str2 = int(str2)
                str3 = str(str3)
                str4 = int(str4)
                str5 = str(str5)
                str6 = str(str6)
                #saving to database
                #establish the connection to database
                conn = sq.connect('cmsuser.db')
                #check for username
                c = conn.cursor()
                c.execute("select * from cmsuser where username = '%s'" %(str1))
                if c.fetchone() is not None:
                    messagebox.showerror('User already exists', 'Username already exists in the system! Please use different Username')
                else:   
                    #enter user data to database
                    conn.execute("insert into cmsuser values (?,?,?,?,?,?)",(str1, str2, str3, str4, str5, str6,))
                    #commit the changes and close the connection to database
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('Registration Successful', 'User Registration Successful. Please Login')
                    exuserpre(new)
        else:
            messagebox.showerror('Failure', 'Please enter details correctly!')
    #submit button
    submit = Button(new, text = 'Submit',  command = checknew, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white')
    submit.place(relx = .57, rely = .80, anchor = CENTER)
    #redirect to existing user
    Label(new, text = 'Already have account! Login from here: ', font = ('roboto', 13)).place(relx = .37, rely = .89, anchor = W)
    Button(new, text = 'Login', font = ('roboto', 13), command = lambda: exuserpre(new)).place(relx = .60, rely = .89, anchor = W)

#Homepage after login
def homepagepre(win):
    '''This pre function is for accessing homepage() function. '''
    win.destroy()
    homepage()
def homepage():
    '''This is function for Home screen of Digital Santa.'''
    home = Tk()
    home.title("Digital Santa")
    home.attributes('-fullscreen', True)
    home.configure(bg='lightpink')
    #headings
    wel1 = Label(home, text = 'Digital Santa', font = ('Sans-serif', 50, 'bold'))
    wel2 = Label(home, text = 'User Page', font = ('Script-typeface', 30, 'bold'))
    wel1.pack()
    wel2.pack()
    #rhs buttons & icons
    backimg = Image.open("Back.png")
    backrender = ImageTk.PhotoImage(backimg)
    def logoutuser():
        messagebox.showinfo('User successfully Logged Out', 'User Logged Out. Redirecting to Home Screen...')
        back(home)
    bimg = Button(home, image = backrender, command = logoutuser, bd = 0)
    bimg.image = backrender
    bimg.place(relx = .02, rely = .04)
    sideexit(home)
    #Buttons
    trackbtn = Button(home, text="Article Tracking", command = lambda: trackpre(home), font = ('arial', 13), bd = 3)
    reqbtn = Button(home, text = "Service Request", command = lambda: courierpre(home), font = ('arial', 13), bd = 3)
    costbtn = Button(home, text = "Postage Calculator", command = lambda: costpre(home), font = ('arial', 13), bd = 3)
    #homepage icons
    #courier request
    reqimg = Image.open("request.png")
    reqrend = ImageTk.PhotoImage(reqimg)
    #track
    trackimg = Image.open("track.jpg")
    trackrend = ImageTk.PhotoImage(trackimg)
    #cost estimator
    costimg = Image.open("cost.png")
    costrend = ImageTk.PhotoImage(costimg)
    #alignment of images on screen
    #track
    trimg = Label(image = trackrend)
    trimg.image = trackrend
    #courier request
    rqimg = Label(image = reqrend)
    rqimg.image = reqimg
    #cost estimator
    cstimg = Label(image = costrend)
    cstimg.image = costrend
    #alignment of icons
    rqimg.place(relx = .25, rely = .45, anchor = CENTER)
    trimg.place(relx = .50, rely = .43, anchor = CENTER)
    cstimg.place(relx = .75, rely = .43, anchor = CENTER)
    #corresponding buttons
    reqbtn.place(relx = .25, rely = .55, anchor = CENTER)
    trackbtn.place(relx = .50, rely = .55, anchor = CENTER)
    costbtn.place(relx = .75, rely = .55, anchor = CENTER)
    #keep window opened
    home.mainloop()

#Request Courier 
#pre functions
def courierpre(win):
    win.destroy()
    reqcourier()
def homeback(win):
    win.destroy()
    homepage()
#courier request
def reqcourierpre(win):
    win.destroy()
    reqcourier()
def reqcourier():
    home = Tk()
    home.title("Service Request")
    home.attributes('-fullscreen', True)
    home.configure(bg='tomato')
    #heading and icon
    reqimg = Image.open("request.png")
    reqrender = ImageTk.PhotoImage(reqimg)
    aimg = Label(image = reqrender)
    aimg.image = reqrender
    aimg.place(relx=.5, rely=.05, anchor = N)
    #admin label
    log = Label(home, text = 'Service Request', font = ('Script-typeface', 23, 'bold'))
    log.place(relx = .5, rely = .20, anchor = N)
    #rhs buttons & icons
    backimg = Image.open("Back.png")
    backrender = ImageTk.PhotoImage(backimg)
    bimg = Button(home, image = backrender, command = lambda: homeback(home), bd = 0)
    bimg.image = backrender
    bimg.place(relx = .02, rely = .04)
    sideexit(home)
    #inputs
    Label(home, text = 'User details:', font = ('arial', 13)).place(relx = .10, rely = .35, anchor = W)
    #username entry
    username1 = StringVar() #for getting username
    uname = Label(home, text = 'Username:', font = ('arial', 14))
    uname.place(relx = .20, rely = .40, anchor = W)
    username = Entry(home, width = 20, bd = 2, font = ('roboto', 13))
    username.place(relx = .35, rely = .40, anchor = CENTER)
    username.focus_set()
    #registration number
    Label(home, text = 'Registration No:', font = ('arial', 14)).place(relx = .45, rely = .40, anchor = W)
    regno = Entry(home, width = 15, bd = 2, font = ('roboto', 13))
    regno.place(relx = .55, rely = .40, anchor = W)
    #mobile number
    ph = Label(home, text = 'Mobile No:', font = ('arial', 14))
    ph.place(relx = .70, rely = .40, anchor = W)
    phone = Entry(home, width = 20, bd = 2, font = ('roboto', 13))
    phone.place(relx = .84, rely = .40, anchor = CENTER)
    #courier details
    Label(home, text = 'Courier details:', font = ('arial', 13)).place(relx = .10, rely = .50, anchor = W)
    #travel from and to
    Label(home, text = 'From:', font = ('arial', 14)).place(relx = .20, rely = .55, anchor = W)
    Label(home, text = 'Lovely Professional University, Phagwara, 144411', font = ('arial', 13)).place(relx = .25, rely = .55, anchor = W)
    Label(home, text = 'To:', font = ('arial', 14)).place(relx = .55, rely = .55, anchor = W)
    to = Entry(home, width = 50, font = ('roboto', 13), bd = 2)
    to.place(relx = .58, rely = .55, anchor = W)
    #weight
    wgh = Label(home, text = 'Weight (in gms):', font = ('arial', 14))
    wgh.place(relx = .20, rely = .65, anchor = W)
    weight = Entry(home, width = 8, font = ('roboto', 13), bd = 2)
    weight.place(relx = .30, rely = .65, anchor = W)
    #Travel Distance
    dist = Label(home, text = 'Travel Distance (in kms):', font = ('arial', 14))
    dist.place(relx = .40, rely = .65, anchor = W)
    distance = Entry(home, width = 8, font = ('roboto', 13), bd = 2)
    distance.place(relx = .55, rely = .65, anchor = W)
    #Delivery Type
    ty = Label(home, text = 'Delivery Type:', font = ('arial', 14))
    ty.place(relx = .65, rely = .65, anchor = W)
    deltype = Combobox(home, font=('Arial', 14))
    deltype['values'] = ('Parcel', 'Express Parcel', 'Speed Post')
    deltype.current(0)
    deltype.place(relx = .75, rely = .65, anchor = W)
    #cost label
    Label(home, text = 'Estimated Cost:', font = ('arial', 14)).place(relx = .20, rely = .75, anchor = W)
    costlabel = Label(home, text = "", font = ('arial', 14), fg = 'darkblue')
    costlabel.place(relx = .47, rely = .75, anchor = CENTER)
    #consignment number
    cons = Label(home, text = '', font = ('arial', 14), fg = 'darkblue')
    cons.place(relx = .20, rely = .80, anchor = W)
    #cost checker
    #check cost button
    Button(home, text = 'Check cost', bd = 0, font = ('roboto', 12), command = lambda: costcheck(weight, distance, deltype, costlabel)).place(relx = .32, rely = .75, anchor = CENTER)
    #submit chekcer
    def checkreq():
        str1 = username.get()
        str2 = regno.get()
        str3 = phone.get()
        str4 = to.get()
        str5 = weight.get()
        #str5 = float(str5)
        str6 = distance.get()
        #str6 = float(str6)
        str7 = deltype.get()
        dk1, dk2, dk3, dk5, dk6, dk4 = 0,0,0,0,0,0
        if str1 and str2 and str3 and str4 and str5 and str6:
            if len(str1) < 6 or len(str1) > 15:
                messagebox.showerror('Failure', 'Username must contain characters between 6 and 20')
                dk1 = 1
            elif re.search('[a-zA-Z]', str2) or len(str2) != 8: # or re.search('[A-Z]', str2):
                messagebox.showerror('Failure', 'Registration number should only contain 8 digits!')
                dk2 = 1
            elif len(str3) != 10 or re.search('[a-zA-Z]', str3):
                messagebox.showerror('Failure', 'Phone number should contain only 10 digits!')
                dk3 = 1
            elif len(str4) < 8:
                messagebox.showerror('Failure', 'To address is too short!')
                dk4 = 1
            elif str5 == '0' or str5 == '':
                messagebox.showerror('Failure', 'Weight cannot be zero!')
                dk5 = 1
            elif str6 == '3' or str6 == '2' or str6 == '1' or str6 == '' or str6 == '0':
                messagebox.showerror('Failure', 'Distance should be at least 4 Kms')
                dk6 = 1
            if dk1 == 0 and dk2 == 0 and dk4 == 0 and dk5 == 0 and dk6 == 0 and dk3 == 0:
                #changing data types
                str1 = str(str1)
                str2 = int(str2)
                str3 = int(str3)
                str4 = str(str4)
                str5 = float(str5)
                str6 = float(str6)
                str7 = str(str7)
                status = 'On the Way'
                costcheck(weight, distance, deltype, costlabel)
                #consignment number generator
                consign = random.randint(1000000, 9999999)
                rnd = 'Consignment number for the courier request: {}'.format(consign)
                cons.configure(text = rnd)
                #saving to database
                #establish the connection to database
                conn = sq.connect('cmsreq.db')
                #enter user data to database
                conn.execute("insert into cmsreq values (?,?,?,?,?,?,?,?,?)",(str1, str2, str3, str4, str5, str6, str7,consign,status,))
                #commit the changes and close the connection to database
                conn.commit()
                conn.close()
                messagebox.showinfo('Request Updated Successfully', 'Request Updated Successfully with consignment no: {}'.format(consign))
                homepagepre(home)
        else:
            messagebox.showerror('Failure', 'Enter valid values!')
    
    #submit button
    Button(home, text = 'Submit Request', bd = 3, font = ('roboto', 13, 'bold'), bg = 'darkblue', fg = 'white', command = checkreq, width = 15).place(relx = .55, rely = .87, anchor = CENTER)
    Button(home, text = 'Reset', bd = 3, font = ('roboto', 13, 'bold'), bg = 'darkred', fg = 'white', command = lambda: reqcourierpre(home), width = 10).place(relx = .45, rely = .87, anchor = CENTER)
    home.mainloop()

#Admin login window
def adminlogin():
    ad = Tk()
    ad.title("Admin Screen")
    ad.attributes('-fullscreen',True)
    ad.configure(bg='turquoise')
    #images
    sideicons(ad)
    #admin image
    adminimg = Image.open("Admin.png")
    adminrender = ImageTk.PhotoImage(adminimg)
    aimg = Label(image = adminrender)
    aimg.image = adminrender
    aimg.place(relx=.5, rely=.05, anchor = N)
    #admin label
    log = Label(ad, text = 'Admin Login', font = ('Script-typeface', 23, 'bold'))
    log.place(relx = .5, rely = .20, anchor = N)
    #inputs
    aname = Label(ad, text = 'AdminID:', font = ('arial', 14))
    aname.place(relx = .38, rely = .37, anchor = W)
    adminname = Entry(ad, width = 20, font = ('roboto', 13), bd = 2)
    adminname.place(relx = .55, rely = .37, anchor = CENTER)
    adminname.focus_set()
    pswrd = Label(ad, text = 'Password', font = ('arial', 14))
    pswrd.place(relx = .38, rely = .44,anchor = W)
    password = Entry(ad, width = 20, show = '*', font = ('roboto', 13), bd = 2)
    password.place(relx = .55, rely = .44, anchor = CENTER)
    #submit checker
    def admincheck():
        str1 = adminname.get()
        str2 = password.get()
        str1 = str(str1)
        str2 = str(str2)
        if str1 and str2:
            #create admin without using any database
            if str1 == 'admin' and str2 == 'admin':    # Change it if necessary.
                ad.destroy()
                adminpage()
            else:
                messagebox.showerror('Failure', 'Wrong Admin details!')
    #submit button
    Button(ad, text = 'Submit', command = admincheck, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white').place(relx = .55, rely = .52, anchor = CENTER)
    #keep window opened
    ad.mainloop()
#admin page
def adminpage():
    x = Tk()
    x.title("AdminPage")
    x.attributes('-fullscreen', True)
    x.configure(bg='lightgrey')
    #headings
    wel1 = Label(x, text = 'Digital Santa', font = ('Helvetica', 50, 'bold italic'))
    wel2 = Label(x, text = 'Admin Page', font = ('Script-typeface', 32, 'bold'))
    wel1.pack()
    wel2.pack()
    #rhs buttons & icons
    backimg = Image.open("Back.png")
    backrender = ImageTk.PhotoImage(backimg)
    def logoutadmin():
        messagebox.showinfo('Admin successfully Logged Out', 'Admin Logged Out. Redirecting to Home Screen...')
        back(x)
    bimg = Button(x, image = backrender, command = logoutadmin, bd = 0)
    bimg.image = backrender
    bimg.place(relx = .02, rely = .04)
    sideexit(x)
    #Admin icons
    adimg = Image.open("admin1.png")
    adrend = ImageTk.PhotoImage(adimg)
    uimg = Label(image = adrend)
    uimg.image = adrend
    uimg.place(relx = .250, rely = .20, anchor = N)
    
    #feedback
    feedimg = Image.open("feed.png")
    feedrend = ImageTk.PhotoImage(feedimg)
    #courier requests
    reqimg = Image.open("request.png")
    reqrend = ImageTk.PhotoImage(reqimg)
    #users
    userimg = Image.open("user.png")
    userend = ImageTk.PhotoImage(userimg)
    #alignment of images on screen
    #courier requests
    rqimg = Label(image = reqrend)
    rqimg.image = reqrend
    #feedbacks
    fdimg = Label(image = feedrend)
    fdimg.image = feedrend
    #users
    usimg = Label(image = userend)
    usimg.image = userend
    #alignment of icons
    fdimg.place(relx = .55, rely = .45, anchor = CENTER)
    rqimg.place(relx = .80, rely = .45, anchor = CENTER)
    usimg.place(relx = .70, rely = .70, anchor = CENTER)
    #tools
    Button(x, text = 'See Feedbacks', font = ('arial', 13), bd = 3, command = lambda: seefeed(x), width = 15).place(relx = .55, rely = .55, anchor = CENTER)
    Button(x, text = 'See Service Requests', font = ('arial', 13), bd = 3, command = lambda: seereq(x), width = 18).place(relx = .80, rely = .55, anchor = CENTER)
    Button(x, text = 'See Users', font = ('arial', 13), bd = 3, command = lambda: seeusers(x), width = 15).place(relx = .70, rely = .80, anchor = CENTER)
    x.mainloop()
def adminback(win):
    win.destroy()
    adminpage()
def sidebackadmin(window):
    #rhs buttons & icons
    backimg = Image.open("Back.png")
    backrender = ImageTk.PhotoImage(backimg)
    bimg = Button(window, image = backrender, command = lambda: adminback(window), bd = 0)
    bimg.image = backrender
    bimg.place(relx = .02, rely = .04)
#see
#see feedbacks
def seefeed(win):
    win.destroy()
    window = Tk()
    window.title('See Feedbacks')
    window.attributes('-fullscreen', True)
    window.configure(bg='lightskyblue')
    sidebackadmin(window)
    sideexit(window)
    #feedback
    feedimg = Image.open("feed.png")
    feedrend = ImageTk.PhotoImage(feedimg)
    fdimg = Label(image = feedrend)
    fdimg.image = feedrend
    fdimg.place(relx = .5, rely = .20, anchor = CENTER)
    
    #feedback database on tkinter
    tree = ttk.Treeview(window, column = ("column1", "column2"), show='headings')
    #tree.heading("#1", text="Username")
    #tree.column("#1", minwidth = 300, width = 100)
    tree.heading("#1", text="Email")
    tree.column("#1", minwidth = 300, width = 100)
    tree.heading("#2", text="Feedback")
    tree.column("#2", minwidth = 600, width = 900)
    tree.place(relx = .5, rely = .3, anchor = N)

    conn = sq.connect("cmsfeed.db")
    cur = conn.cursor()
    cur.execute("select * from cmsfeed")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", END, values = row)
    conn.close()
    window.mainloop()
#see courier request
def seereq(win):
    win.destroy()
    window = Tk()
    window.title('See Courier Requests')
    window.attributes('-fullscreen', True)
    window.configure(bg='salmon')
    sidebackadmin(window)
    sideexit(window)
    #request img
    reqimg = Image.open("request.png")
    reqrend = ImageTk.PhotoImage(reqimg)
    rqimg = Label(image = reqrend)
    rqimg.image = reqrend
    rqimg.place(relx = .5, rely = .15, anchor = CENTER)
    #view database on tkinter window
    tree = ttk.Treeview(window, column = ("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show='headings')
    tree.heading("#1", text="Username")
    tree.heading("#2", text="Reg no")
    tree.column("#2", minwidth = 110, width = 110)
    tree.heading("#3", text="Mobile")
    tree.column("#3", minwidth = 150, width = 150)
    tree.heading("#4", text="Courier To")
    tree.heading("#5", text="Weight (gm)")
    tree.column("#5", minwidth = 110, width = 110)
    tree.heading("#6", text="Distance (km)")
    tree.column("#6", minwidth = 110, width = 110)
    tree.heading("#7", text="Delivery Type")
    tree.heading("#8", text="Consignment Number")
    tree.heading("#9", text="Status")
    tree.column("#9", minwidth = 100, width = 100)
    tree.place(relx = .5, rely = .3, anchor = N)

    conn = sq.connect("cmsreq.db")
    cur = conn.cursor()
    cur.execute("select * from cmsreq")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", END, values = row)
    conn.close()
    
    window.mainloop() 
#see cms users
def seeusers(win):
    win.destroy()
    window = Tk()
    window.title('See Users')
    window.attributes('-fullscreen', True)
    window.configure(bg='thistle')
    sidebackadmin(window)
    sideexit(window)
    #user img
    usimg = Image.open("user.png")
    usrend = ImageTk.PhotoImage(usimg)
    usimg = Label(image = usrend)
    usimg.image = usrend
    usimg.place(relx = .5, rely = .15, anchor = CENTER)
    #view database on tkinter window
    tree = ttk.Treeview(window, column = ("column1", "column2", "column3", "column4", "column5"), show='headings')
    tree.heading("#1", text="Username")
    tree.heading("#2", text="Reg no")
    tree.heading("#3", text="Gender")
    tree.heading("#4", text="Mobile")
    tree.heading("#5", text="Email")
    tree.place(relx = .5, rely = .3, anchor = N)

    conn = sq.connect("cmsuser.db")
    cur = conn.cursor()
    cur.execute("select * from cmsuser")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", END, values = row)
    conn.close()
    window.mainloop()

#Track package window
def track():
    window = Tk()
    window.title("Track the Product")
    window.attributes('-fullscreen',True)
    window.configure(bg='goldenrod')
    #images
    sideicons(window)
    #admin image
    adminimg = Image.open("track.jpg")
    adminrender = ImageTk.PhotoImage(adminimg)
    aimg = Label(image = adminrender)
    aimg.image = adminrender
    aimg.place(relx = .5, rely=.05, anchor = N)
    #admin label
    log = Label(window, text = 'Track the Product', font = ('Script-typeface', 23, 'bold'))
    log.place(relx = .5, rely = .25, anchor = N)
    #inputs
    #username
    us = Label(window, text = 'Username:', font = ('arial', 14))
    us.place(relx = .33, rely = .38,anchor = W)
    username = Entry(window, width = 20, font = ('roboto', 13), bd = 2)
    username.place(relx = .57, rely = .38, anchor = CENTER)
    username.focus_set()
    #consignment number
    cons = Label(window, text = 'Consignment Number:', font = ('arial', 14))
    cons.place(relx = .33, rely = .45, anchor = W)
    consnum = Entry(window, width = 20, font = ('roboto', 13), bd = 2)
    consnum.place(relx = .57, rely = .45, anchor = CENTER)
    #submit checker
    def trackcheck():
        str1 = username.get()
        str2 = consnum.get()
        conn = sq.connect('cmsreq.db')
        c = conn.cursor()
        c.execute("select * from cmsreq where username = '%s' and consnum = '%s'" % (str1, str2))
        if c.fetchone() is not None:
            messagebox.showinfo('Success', 'Courier found with entered tracking ID and Username.')

            tree = ttk.Treeview(window, column = ("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show='headings')
            tree.heading("#1", text="Username")
            tree.heading("#2", text="Reg no")
            tree.column("#2", minwidth = 110, width = 110)
            tree.heading("#3", text="Mobile")
            tree.column("#3", minwidth = 150, width = 150)
            tree.heading("#4", text="Courier To")
            tree.heading("#5", text="Weight")
            tree.column("#5", minwidth = 110, width = 110)
            tree.heading("#6", text="Distance")
            tree.column("#6", minwidth = 110, width = 110)
            tree.heading("#7", text="Delivery Type")
            tree.heading("#8", text="Consignment Number")
            tree.heading("#9", text="Status")
            tree.column("#9", minwidth = 100, width = 100)
            tree.place(relx = .5, rely = .6, anchor = N)

            #view database on tkinter window
            conn = sq.connect("cmsreq.db")
            cur = conn.cursor()
            cur.execute("select * from cmsreq where consnum = %s" % (str2))
            rows = cur.fetchall()
            for row in rows:
                print(row) # it print all records in the database
                tree.insert("", END, values = row)
            conn.close()

        else:
            messagebox.showerror('Failure', 'Enter the valid Tracking details!')
        conn.close()
    
    #Tracking details window
    
    #submit button
    Button(window, text = 'Track it!', command = trackcheck, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white', width = 10).place(relx = .55, rely = .52, anchor = CENTER)
    Button(window, text = 'Reset', command = lambda: trackreset(window), font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkred', fg = 'white', width = 10).place(relx = .45, rely = .52, anchor = CENTER)
    #keep window opened
    mainloop()
#Track reset
def trackreset(window):
    window.destroy()
    track()

#Cost Estimation using MLR
#importing linear model & creating object
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
#reading csv file for training
df = pd.read_csv('data.csv')
#defining feature & target variable
x = np.asanyarray(df[['weight', 'distance', 'speedtype']])
y = np.asanyarray(df[['cost']])
#fitting linear model
lr.fit(x, y)
#cost checker
def costcheck(w, d, ty, lb):
    #validate details first
    x1 = w.get()
    x2 = d.get()
    if x1 and x2:
        #conversion of del.type into numeric value
        cm = ty.get()
        if cm == 'Parcel':
            xc = 1
        elif cm == 'Express Parcel':
            xc = 2
        else:
            xc = 3
        if x1 == '0' or x1 == '1' or re.search('[a-zA-Z]', x1):
                messagebox.showerror('Failure', 'Enter valid value of weight!')
        elif x2 == '0' or x2 == '1' or x2 == '2' or x2 == '3' or re.search('[a-zA-Z]', x2):
                messagebox.showerror('Failure', 'Distance should be at least 4 Kms')
        #predict
        else:
            x1 = float(x1)
            x2 = float(x2)
            pr = [[x1, x2, xc]]
            pred = lr.predict(pr)
            pred = ceil(float(pred))
            cost = 'Approx. Cost for Courier Delivery is ₹ {}.'.format(pred)
            lb.configure(text = cost)
    else:
        messagebox.showerror('Failure', 'Enter Valid values for Cost Estimation!')
#Cost estimator window
def costestm():
    window = Tk()
    window.title("Cost Estimation")
    window.attributes('-fullscreen', True)
    window.configure(bg='green')
    #images
    sideicons(window)
    #admin image
    adminimg = Image.open("cost.png")
    adminrender = ImageTk.PhotoImage(adminimg)
    aimg = Label(image = adminrender)
    aimg.image = adminrender
    aimg.place(relx = .5, rely=.05, anchor = N)
    #admin label
    log = Label(window, text = 'Postage Cost Estimation', font = ('Script-typeface', 23, 'bold'))
    log.place(relx = .5, rely = .25, anchor = N)
    Label(window, text = 'Please Enter all of the following values:', font = ('roboto', 12)).place(relx = .33, rely = .34, anchor = W)
    #inputs
    #weight
    wgh = Label(window, text = 'Weight of Courier (in gms):', font = ('arial', 14))
    wgh.place(relx = .33, rely = .40,anchor = W)
    weight = Entry(window, width = 20, font = ('roboto', 13), bd = 2)
    weight.place(relx = .55, rely = .40, anchor = W)
    weight.focus_set()
    #Travel Distance
    dist = Label(window, text = 'Travel Distance (in kms):', font = ('arial', 14))
    dist.place(relx = .33, rely = .47, anchor = W)
    distance = Entry(window, width = 20, font = ('roboto', 13), bd = 2)
    distance.place(relx = .55, rely = .47, anchor = W)
    #Delivery Type
    ty = Label(window, text = 'Delivery Type:', font = ('arial', 14))
    ty.place(relx = .33, rely = .54, anchor = W)
    deltype = Combobox(window, font=('Arial', 14))
    deltype['values'] = ('Parcel', 'Express Parcel', 'Speed Post')
    deltype.current(0)
    deltype.place(relx = .55, rely = .54, anchor = W)
    #cost label
    costlabel = Label(window, text = '', font = ('arial', 15, 'bold'))
    costlabel.place(relx = .50, rely = .61, anchor = CENTER)    
    #submit button
    Button(window, text = 'Get Price', command = lambda: costcheck(weight, distance, deltype, costlabel), font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white').place(relx = .50, rely = .70, anchor = CENTER)
    #keep window opened
    mainloop()

#adminback window
def feedback():
    window = Tk()
    window.title("Feedback")
    window.attributes('-fullscreen',True)
    window.configure(bg='steelblue')
    #images
    sideicons(window)
    #admin image
    adminimg = Image.open("feed.png")
    adminrender = ImageTk.PhotoImage(adminimg)
    aimg = Label(image = adminrender)
    aimg.image = adminrender
    aimg.place(relx = .5, rely=.05, anchor = N)
    #admin label
    log = Label(window, text = 'Give Your Feedback', font = ('Script-typeface', 23, 'bold'))
    log.place(relx = .5, rely = .20, anchor = N)
    #labels and input
    mail = Label(window, text = 'Enter your Email:', font = ('arial', 14))
    mail.place(relx = .35, rely = .35, anchor = W)
    feedmail = Entry(window, width = 25, font = ('arial', 13), bd = 2)
    feedmail.place(relx = .55, rely = .35, anchor = CENTER)
    aw = Label(window, text = 'Please Give Your Feedback:', font = ('arial', 14))
    aw.place(relx = .20, rely = .43, anchor = W)
    scrolW = 80
    scrolH = 13
    feed = scrolledtext.ScrolledText(window, width = scrolW, height = scrolH, font = ('arial', 14), wrap = WORD)  
    feed.place(relx = .5, rely = .47, anchor = N)
    #submit
    def checkfeed():
        str1 = feedmail.get()
        str1 = str(str1)
        str2 = feed.get("1.0", END)
        str2 = str(str2)
        if str1 and str2:
            if re.search('[@]', str1) is None:
                messagebox.showerror('Failure', 'Please enter valid Email')
            elif len(str2) < 5:
                messagebox.showerror('Failure', 'Feedback must contain 5 words!')
            else:
                #add feedback in the database cmsfeed.db
                #establish the connection to database
                conn = sq.connect('cmsfeed.db')
                #add feedback to database
                conn.execute("insert into cmsfeed values (?,?)", (str1, str2,))
                #commit changes and close the connection
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'Thank you for Feedback.')
                back(window)
        else:
            messagebox.showerror('Failure', 'Please fill the email and Feedback!')
           
    submit = Button(window, text = 'Submit Feedback', command = checkfeed, font = ('Roboto', 13, 'bold'), bd = 3, bg = 'darkblue', fg = 'white')
    submit.place(relx = .5, rely = .85, anchor = CENTER)
    
    


#Run main screen
mainscreen()