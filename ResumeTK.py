from calendar import c
from email import header
from msilib.schema import Font
from re import U
from tkinter import *
from tkinter import font
from urllib import request, response
import webbrowser
from PIL import ImageTk, Image
from click import command
from tkinter import ttk 
import requests
import urllib.request 

# main window set

main = Tk()
main.title("Resume in Python")
main.minsize(width=1000,height=700)
main.resizable(False,False)
main.iconbitmap("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/RESUMEe.ico")
main.config(background="#c8dceb")
      
# url github 

class weburl():
    def github():
        url = 'https://github.com/vinaygupta077'
        webbrowser.open_new(url)
        
    def telegram():
        url = "https://t.me/vinaygupta077"
        webbrowser.open_new(url)
        
    def twitter():
        url = "https://twitter.com/vinaygupta077"
        webbrowser.open_new(url)
        
    def linkedin():
        url = "https://www.linkedin.com/in/vinaygupta077"
        webbrowser.open_new(url)
        
    def facebook():
        url = "https://www.facebook.com/vinaygupta077"
        webbrowser.open_new(url)
        
    def instagram():
        url = "https://www.instagram.com/_vk.95/"
        webbrowser.open_new(url)
        
    def koo():
        url = "https://www.kooapp.com/profile/vinaygupta077"
        webbrowser.open_new(url)
        
    def whtsapp():
        url = "https://wa.link/n86dgj"
        webbrowser.open_new(url)
        
    def pin():
        url = "https://in.pinterest.com/vinaygupta077/_created/"
        webbrowser.open_new(url)
        
    def mail():
        url = "mailto:?to=077v.kumar@gmail.com&subject=Welcome Mail"
        webbrowser.open_new(url)
        
    def RD():
        url = "http://rdec.in/"
        webbrowser.open_new(url)
        
    def JSS():
        url = "https://jssaten.ac.in/"
        webbrowser.open_new(url)
        
    def GPG():
        url = "https://www.gpghaziabad.ac.in/"
        webbrowser.open_new(url)
        
    def DUCAT():
        url = "https://www.ducatindia.com/"
        webbrowser.open_new(url)
        
    def SNC():
        url = "https://sncinfotech.com/"
        webbrowser.open_new(url)
        
    def GL():
        url = "https://www.mygreatlearning.com/"
        webbrowser.open_new(url)
        
    def NTS():
        url = "https://www.msde.gov.in/"
        webbrowser.open_new(url)
      
# for fifth window

class Fifth_window:
    def fifth_window():
        main4 = Toplevel()
        main4.title("Contact")
        main4.minsize(width=900,height=500)
        main4.resizable(False,False)
        main4.iconbitmap("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/CONTACT.ico")
        main4.config(background="#d0deec")
        
        
    # label
    
        leb = Label(main4,text="Contact Me _@_",bg="skyBlue",fg="Black",width=65,font=("tohoma",15,font.BOLD))
        leb.place(x=60,y=20)
        leb1 = Label(main4,text= "If you`d like to get in touch, feel free to say hello through any of the social links below.",fg="black",font=("tohoma",12,font.BOLD,font.ITALIC))
        leb1.place(x=150,y=70)
        leb1.config(background="#d0deec")
        leb2 = Label(main4,text="Version 1.4.8",fg="black",font=("tohoma",8,font.ITALIC))
        leb2.place(x=815,y=480)
        leb2.config(background="#d0deec")
        leb3 = Label(main4,text="Proprietary content. ©Vinay Gupta. All Rights Reserved. Unauthorized use or distribution prohibited. © 2022 All rights reserved.",fg="black",font=("tohoma",8,font.ITALIC,font.BOLD))
        leb3.place(x=188,y=465)
        leb3.config(background="#d0deec")
            
    # button
    
        butexit = Button(main4, text="EXIT",bg="orange",fg="black",height=1, width=7, borderwidth=5,font="times 10 bold",command=main4.quit)
        butexit.place(x=400,y=410)
        
    # MAIL PHOTO
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/MAIL.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=200,y=150) 
    
    # mail button
    
        buttonmail = Button(main4, image=pic5.image,borderwidth=0,command=weburl.mail)
        buttonmail.place(x= 200,y=150)
        
    # LINKEDIN PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/LINKEDINN.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=300,y=150) 
        
    # linkedin button

        buttonlinkedin = Button(main4, image=pic5.image,borderwidth=0,command=weburl.linkedin)
        buttonlinkedin.place(x= 300,y=150)
    
    # GITHUB PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/GITHUB.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=400,y=150) 
        
    # github button
    
        buttongithub = Button(main4, image=pic5.image,borderwidth=0,command=weburl.github)
        buttongithub.place(x= 400,y=150)
        
    # WHATSAPP PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/WHTSAPP.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=500,y=150) 
        
    # whtsapp button
    
        buttonwhtsapp = Button(main4, image=pic5.image,borderwidth=0,command=weburl.whtsapp)
        buttonwhtsapp.place(x= 500,y=150)
        
    # TWITTER PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/TWITTER.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=600,y=150) 
    
    # twitter button
    
        buttontwit = Button(main4, image=pic5.image,borderwidth=0,command=weburl.twitter)
        buttontwit.place(x= 600,y=150)
        
    # FACEBOOK PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/FACEBOOK.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=200,y=250) 
        
    # facebook button 
    
        buttonfb = Button(main4, image=pic5.image,borderwidth=0,command=weburl.facebook)
        buttonfb.place(x= 200,y=250)
        
    # INSTA PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/INSTA.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=300,y=250) 
        
    # insta button 
    
        buttoninsta = Button(main4, image=pic5.image,borderwidth=0,command=weburl.instagram)
        buttoninsta.place(x= 300,y=250)
        
    # PINTEREST PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/PIN.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=400,y=250) 
        
    # pin button
    
        buttonpin = Button(main4, image=pic5.image,borderwidth=0,command=weburl.pin)
        buttonpin.place(x= 400,y=250)
        
    # TELEGRAM PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/TELEGRAM.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=500,y=250) 
    
    # tele button
    
        buttontele = Button(main4, image=pic5.image,borderwidth=0,command=weburl.telegram)
        buttontele.place(x= 500,y=250)
    
    # KOO PHOTO
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/KOO.PNG")
        resized1 = pic3.resize((75,75),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main4, image=pic4)         
        pic5.image = pic4
        pic5.place(x=600,y=250)  
        
    # koo button 
    
        buttonkoo = Button(main4, image=pic5.image,borderwidth=0,command=weburl.koo)
        buttonkoo.place(x= 600,y=250)
        
# for fourth window

class Fourth_window:
    def fourth_window():
        main3 = Toplevel()
        main3.title("Certification")
        main3.minsize(width=990,height=600)
        main3.resizable(False,False)
        main3.iconbitmap("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/CERTIFICATE.ico")
        main3.config(background="#d0deec")
    
    # label
     
        leb2 = Label(main3,text="Certification |+|",bg="skyBlue",fg="Black",width=65,font=("tahoma",15,font.BOLD))
        leb2.place(x=90,y=20)
        
    # ducat image
    
        picD = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/DUC.PNG")
        resizedD = picD.resize((130,70),Image.ANTIALIAS)
        pic9 = ImageTk.PhotoImage(resizedD)
        pic10 = Label(main3, image = pic9)
        pic10.image = pic9
        pic10.place(x=200,y=80)
        
    # ducat text
        leb3 = Label(main3,text="""DUCAT, GHAZIABAD • PYTHON
        JANUARY 2022
        I learned basic python, some libraries (e.g. NumPy & Tkinter) and 
        gained some knowledge of frameworks (e.g. Django & Flask).""",fg="black", font=("tohoma",10,font.BOLD,font.ITALIC))
        leb3.place(x=360, y=80)
        leb3.config(background="#d0deec")
        
    # ducat button

        buttonmail = Button(main3, image=pic10.image,borderwidth=0,command=weburl.DUCAT)
        buttonmail.place(x= 200,y=80)
        
    # GL image
    
        picD = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/GL.PNG")
        resizedD = picD.resize((130,70),Image.ANTIALIAS)
        pic9 = ImageTk.PhotoImage(resizedD)
        pic10 = Label(main3, image = pic9)
        pic10.image = pic9
        pic10.place(x=200,y=190)
    
    # GL text
    
        leb3 = Label(main3,text="""GREAT LEARNING • PYTHON & MYSQL 
        I obtained most of the my certificate from Great Learning in Python & MySql.""",fg="black", font=("tohoma",10,font.BOLD,font.ITALIC))
        leb3.place(x=360, y=205)
        leb3.config(background="#d0deec")
        
    # gl button
    
        buttonmail = Button(main3, image=pic10.image,borderwidth=0,command=weburl.GL)
        buttonmail.place(x= 200,y=190)
    
    # SNC image
    
        picSN = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/SNC.PNG")
        resizeSN = picSN.resize((130,70),Image.ANTIALIAS)
        pic9 = ImageTk.PhotoImage(resizeSN)
        pic10 = Label(main3, image = pic9)
        pic10.image = pic9
        pic10.place(x=200,y=290)
    
    # SNC text
    
        leb4 = Label(main3,text="""SNC INFOTECH PVT. LTD. • WEB DESIGNING
        JULY 2016
        I have done certification in web designing here. I learned basic 
        HTML, CSS, and JavaScript & Ajax.""",fg="black", font=("tohoma",10,font.BOLD,font.ITALIC))
        leb4.place(x=360, y=290)
        leb4.config(background="#d0deec")
        
    # snc button
    
        buttonmail = Button(main3, image=pic10.image,borderwidth=0,command=weburl.SNC)
        buttonmail.place(x= 200,y=290)
    
    # NCT image
    
        picN = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/NCT.PNG")
        resizeN = picN.resize((130,90),Image.ANTIALIAS)
        pic9 = ImageTk.PhotoImage(resizeN)
        pic10 = Label(main3, image = pic9)
        pic10.image = pic9
        pic10.place(x=200,y=390)
        
    # NCT text
    
        leb4 = Label(main3,text="""NATIONAL COUNCIL FOR VOCATIONAL TRAINING • HARDWARE & NETWORKING
        JULY 2016
        I have done certification in hardware & networking in which I 
        learned about Fundamentals of Information Technology & Operating 
        Systems, Pc Assembling & Troubleshooting, Computer Networks, 
        Database Administration.""",fg="black", font=("tohoma",10,font.BOLD,font.ITALIC))
        leb4.place(x=360, y=390)
        leb4.config(background="#d0deec")
    
    # nct button
    
        buttonmail = Button(main3, image=pic10.image,borderwidth=0,command=weburl.NTS)
        buttonmail.place(x= 200,y=390) 
    
    # Button
    
        b4 = Button(main3,text= "NEXT",bg ="orange",fg = "black",height=1, width=7, borderwidth=5,font="times 10 bold",command=Fifth_window.fifth_window)
        b4.place(x=450,y=520)
        
        
# for third window

class Third_window:
    def third_window():
        main2 = Toplevel()
        main2.title("Education")
        main2.minsize(width=1000,height=580)
        main2.resizable(False,False)
        main2.iconbitmap("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/ED.ico")
        main2.config(background="#d0deec")
        
    # label
        leb1 = Label(main2,text="Education \@/",bg="skyBlue",fg="black",width=65,font=("tahoma",15,font.BOLD))
        leb1.place(x=80,y=20)
    
    # RD
    
        picRD = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/RD.PNG")
        resizedRD = picRD.resize((100,100),Image.ANTIALIAS)
        pic9 = ImageTk.PhotoImage(resizedRD)
        pic10 = Label(main2, image = pic9)
        pic10.image = pic9
        pic10.place(x=200,y=100)
    
    # RD text
    
        leb2 = Label(main2,text="""R.D ENGINEERING COLLEGE, GHAZIABAD • M. TECH
        SEPTEMBER 2020 - Present
        Computer Science & Engineering
        AKTU""",fg="black",font=("tahoma",10,font.BOLD))
        leb2.place(x=350,y=120)
        leb2.config(background="#d0deec")
        
    # rd button
    
        buttonmail = Button(main2, image=pic10.image,borderwidth=0,command=weburl.RD)
        buttonmail.place(x= 200,y=100)
    
    # jss
        
        picJSS = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/JSS.PNG")
        resizedJSS = picJSS.resize((100,100),Image.ANTIALIAS)
        pic11 = ImageTk.PhotoImage(resizedJSS)
        pic12 = Label(main2, image = pic11)
        pic12.image = pic11
        pic12.place(x=200,y=220)
    
    # jss text
        
        leb3 = Label(main2,text="""JSS ACADEMY OF TECHNICAL EDUCATION, NOIDA • B. TECH
        AUGUST 2017 - SEPTEMBER 2020 
        Computer Science & Engineering
        AKTU""",fg="black",font=("tahoma",10,font.BOLD))
        leb3.place(x=350,y=240)
        leb3.config(background="#d0deec")
        
    # jss button
    
        buttonmail = Button(main2, image=pic12.image,borderwidth=0,command=weburl.JSS)
        buttonmail.place(x= 200,y=220)
    
    # diploma
    
        picGPG = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/GPG.PNG")
        resizedGPG = picGPG.resize((100,100),Image.ANTIALIAS)
        pic13 = ImageTk.PhotoImage(resizedGPG)
        pic14 = Label(main2, image = pic13)
        pic14.image = pic13
        pic14.place(x=200,y=340)
    
    # gpg text
    
        leb4 = Label(main2,text="""GOVERNMENT POLYTECHNIC GHAZIABAD, GHAZIABAD • DIPLOMA
        AUGUST 2014 - AUGUST 2017 
        Information Technology
        BTEUP""",fg="black",font=("tahoma",10,font.BOLD))
        leb4.place(x=350,y=360)
        leb4.config(background="#d0deec")
        
    # gpg button
    
        buttonmail = Button(main2, image=pic14.image,borderwidth=0,command=weburl.GPG)
        buttonmail.place(x= 200,y=340)
    
    # Button
        
        b3 = Button(main2,text= "NEXT",bg ="orange",fg = "black",height=1, width=7, borderwidth=5,font="times 10 bold",command=Fourth_window.fourth_window)
        b3.place(x=450,y=490)
    
        
# for second window
    
class Second_window:   
    def second_window():
        main1 = Toplevel()
        main1.title("About me")
        main1.minsize(width=1390,height=700)
        main1.resizable(False,False)
        main1.iconbitmap("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/ABOUTME.ico")
        main1.config(background="#d0deec")  
        
    # label
    
        leb = Label(main1,text="About me -|-",bg="skyBlue",fg = "black",width=90,font=("tahoma",15,font.BOLD))
        leb.place(x=80,y=20)
        
    # image
    
        pic3 = Image.open("C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/Dp.PNG")
        resized1 = pic3.resize((380,250),Image.ANTIALIAS)
        pic4 = ImageTk.PhotoImage(resized1)
        pic5 = Label(main1, image=pic4)         
        pic5.image = pic4
        pic5.place(x=500,y=70) 
    
    # text label
    
        leb1 = Label(main1,text="""I`m a software engineer pursuing a master`s degree from R D Engineering College, Ghaziabad (AKTU).
                After finishing my Bachelor of Technology in Computer Science & Engineering from JSS Academy of Technical Education Noida (AKTU),
                I`m looking for a career as a software developer. I`m building my skills in Data Structure, Python, C, Oops Concepts, HTML5, and MySQL.
                Along with this, I`ve completed my diploma in the Information Technology branch from Government Polytechnic Ghaziabad (BTEUP).
                And also did my high school at Kendriya Vidyalaya, Ballia (CBSE).
                Currently living in New Delhi.
                In the era of computers and digital technology, I`m always interested building up my logical thinking, and programming is one of the top best for me.
                Programming develops the skill of logical thinking, building algorithms, and problem-solving.
                This programming will teach me to solve non-trivial problems and think outside the box.
                On the other side of me, I`m an athlete playing lots of games like Cricket, Football, Volleyball, and Badminton since high school and I have also been the captain of my college team.
                I love playing Badminton or Chess in my free time as it helps me unwind, relax as well as boosts my creativity and analytical thinking skills. 
                And with this Listing music has been my favourite pastime since I was in high school.
                Also, I like spending time in nature capturing all the wonderful moments of beauty with my camera.
                My favourite hobby is travelling because I love friend`s trips outings bring me the real adventure and thrill and also lots of fun into new places all by my friend`s group.""",fg="black",font=("tohoma",11,font.BOLD,font.ITALIC))
        leb1.place(x=30,y=350)
        leb1.config(background="#d0deec")
    
    # button
        
        b2 = Button(main1,text= "NEXT",bg ="orange",fg = "black",height=1, width=7, borderwidth=5,font="times 10 bold",command=Third_window.third_window)
        b2.place(x=650,y=620)
        
# for first window

# image

pic1 = PhotoImage(file="C:/Users/HP/OneDrive/Desktop/TKINTER/FILE/hello.PNG")
pic2 = Label(main,image=pic1)
pic2.place(x=85 ,y=50)

# label

l1 = Label(main,text = "__/\__HELLO__/\__",bg = "yellow",fg = "red", width = 50, font=("Tahoma",15,font.BOLD))
l2 = Label(main,text = "Please tap on 'Next'",bg = "yellow",fg = "red", width = 80,font=("Tahoma",10,font.ITALIC))
l1.place(x=150,y=500)
l2.place(x=200,y=540)

# button

b1 = Button(main,text= "NEXT",bg ="orange",fg = "black",height=1, width=7, borderwidth=5,font="times 10 bold",command=Second_window.second_window)
b1.place(x=450,y=580)

# for run window

main.mainloop()
