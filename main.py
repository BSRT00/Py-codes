import tkinter
from tkinter import*
import time
import threading
def main():
    global mainWindow
    global Main
    #Window GUI
    mainWindow = tkinter.Tk()
    mainWindow.title("CPS Test")
    mainWindow.resizable(False, False)
    w = 300
    h = 300
    ws = mainWindow.winfo_screenwidth()
    hs = mainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    mainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    mainWindow.configure(bg='#333333')
    #Frame
    Main = tkinter.Frame(bg='#333333')
    Main.place(relx=.5, rely=.2, anchor= CENTER, y=87)
    def test():
        print("HI")
    def windowkill1():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test1()
    def windowkill2():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test2()
    def windowkill3():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test3()
    def windowkill4():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test4()

    button1s = Button(Main, text="1s Test", command=windowkill1, pady=10, padx=20, width=20)
    button5s = Button(Main, text="5s Test", command=windowkill2, pady=10, padx=20, width=20)
    button10s = Button(Main, text="10s Test", command=windowkill3, pady=10, padx=20, width=20)
    buttoncustom = Button(Main, text="Custom Test", command=windowkill4, pady=10, padx=20, width=20)

    button1s.pack(pady=10)
    button5s.pack(pady=10)
    button10s.pack(pady=10)
    buttoncustom.pack(pady=10)
    mainWindow.mainloop()
def main2():
    global mainWindow
    global Main
    #Frame
    Main = tkinter.Frame(bg='#333333')
    Main.place(relx=.5, rely=.2, anchor= CENTER, y=87)
    def test():
        print("HI")
    def windowkill1():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test1()
    def windowkill2():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test2()
    def windowkill3():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test3()
    def windowkill4():
        button1s.destroy()
        button5s.destroy()
        button10s.destroy()
        buttoncustom.destroy()
        test4()

    button1s = Button(Main, text="1s Test", command=windowkill1, pady=10, padx=20, width=20)
    button5s = Button(Main, text="5s Test", command=windowkill2, pady=10, padx=20, width=20)
    button10s = Button(Main, text="10s Test", command=windowkill3, pady=10, padx=20, width=20)
    buttoncustom = Button(Main, text="Custom Test", command=windowkill4, pady=10, padx=20, width=20)

    button1s.pack(pady=10)
    button5s.pack(pady=10)
    button10s.pack(pady=10)
    buttoncustom.pack(pady=10)
    mainWindow.mainloop()
def test1():
    global lable
    lable = Label(Main, text="0")
    lable.grid(column=0, row=0, columnspan=3)
    input_of_time = 1 #Change
    global numberoftime
    global clicks
    global counter
    clicks = 0
    numberoftime = 0

    def timerClock():
        global timer
        global input_of_time
        input_of_time = 1
        timer = input_of_time
        for i in range (input_of_time):
            time.sleep(1)
            timer -= 1
    counter = threading.Thread(target=timerClock)

    def restart():
        global numberoftime
        global timer
        global counter
        global clicks
        score.destroy()
        reset.destroy()
        numberoftime = 0
        clicks = 0

        counter = threading.Thread(target=timerClock)

        lable = Label(Main, text=clicks,)
        lable.grid(column=0, row=0, columnspan=3)

        clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='normal')
        clicker.grid(column=0, row=1, columnspan=2)

    def click():
        global score
        global reset
        global numberoftime
        global clicks
        global lable
        global clicker
        global counter
        if numberoftime == 0:
            counter.start()
            numberoftime += 1 
        else:
            if timer == 0:
                Main.place(relx=.5, rely=.2, anchor= CENTER)    
                clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='disabled')
                clicker.grid(column=0, row=1, columnspan=2)

                CPS = clicks%input_of_time
                
                if CPS > 0:
                    cps = clicks/input_of_time
                    score = Label(Main, text=(cps, "CPS"))
                    score.grid(column=0, row=3, columnspan=2)
                else:
                    cps = clicks//input_of_time
                    score = Label(Main, text=(cps, "CPS"))
                    score.grid(column=0, row=3, columnspan=2)

                reset = Button(Main, text="Restart", command=restart)
                reset.grid(column=0, row=4, columnspan=2)  
            else:
                clicks += 1
                lable.destroy()
                lable = Label(Main, text=clicks,)
                lable.grid(column=0, row=0, columnspan=3)   


    clicker = Button(Main, text="click", command=click, pady=10, padx=10)
    clicker.grid(column=0, row=1, rowspan=2, columnspan=2)
    def clear():
        global numberoftime
        global timer
        global counter
        global clicks
        global clicker
        global lable
        score.destroy()
        reset.destroy()
        clicker.destroy()
        lable.destroy()
        numberoftime = 0
        clicks = 0
    def kill():
        try:
            clear()
            back.destroy()
            main2()
        except:
            clicker.destroy() 
            lable.destroy()
            back.destroy()
            main2()

    back = Button(mainWindow, text=("back"), command=kill)
    back.pack(anchor=SE,side="bottom", padx=40, pady=100)
def test2():
    global lable
    lable = Label(Main, text="0")
    lable.grid(column=0, row=0, columnspan=3)
    input_of_time = 5 #Change
    global numberoftime
    global clicks
    global counter
    clicks = 0
    numberoftime = 0



    def timerClock():
        global timer
        timer = input_of_time
        for i in range (input_of_time):
            time.sleep(1)
            timer -= 1
    counter = threading.Thread(target=timerClock)



    def restart():
        global numberoftime
        global timer
        global counter
        global clicks
        score.destroy()
        reset.destroy()
        numberoftime = 0
        clicks = 0

        counter = threading.Thread(target=timerClock)

        lable = Label(Main, text=clicks,)
        lable.grid(column=0, row=0, columnspan=3)

        clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='normal')
        clicker.grid(column=0, row=1, columnspan=2)

    def click():
        global score
        global reset
        global numberoftime
        global clicks
        global lable
        global counter
        if numberoftime == 0:
            counter.start()
            numberoftime += 1 
        else:
            if timer == 0:
                Main.place(relx=.5, rely=.2, anchor= CENTER)    
                clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='disabled')
                clicker.grid(column=0, row=1, columnspan=2)

                CPS = clicks%input_of_time
                
                if CPS > 0:
                    cps = clicks/input_of_time
                    score = Label(Main, text=(cps, "CPS"))
                    score.grid(column=0, row=3, columnspan=2)
                else:
                    cps = clicks//input_of_time
                    score = Label(Main, text=(cps, "CPS"))
                    score.grid(column=0, row=3, columnspan=2)

                reset = Button(Main, text="Restart", command=restart)
                reset.grid(column=0, row=4, columnspan=2)  
            else:
                clicks += 1
                lable.destroy()
                lable = Label(Main, text=clicks,)
                lable.grid(column=0, row=0, columnspan=3)   


    clicker = Button(Main, text="click", command=click, pady=10, padx=10)
    clicker.grid(column=0, row=1, rowspan=2, columnspan=2)
    def clear():
        global numberoftime
        global timer
        global counter
        global clicks
        global clicker
        global lable
        score.destroy()
        reset.destroy()
        clicker.destroy()
        lable.destroy()
        numberoftime = 0
        clicks = 0
    def kill():
        try:
            clear()
            back.destroy()
            main2()
        except:
            clicker.destroy() 
            lable.destroy()
            back.destroy()
            main2()

    back = Button(mainWindow, text=("back"), command=kill)
    back.pack(anchor=SE,side="bottom", padx=40, pady=100)
def test3():
    global lable
    lable = Label(Main, text="0")
    lable.grid(column=0, row=0, columnspan=3)
    input_of_time = 10 #Change
    global numberoftime
    global clicks
    global counter
    clicks = 0
    numberoftime = 0



    def timerClock():
        global timer
        timer = input_of_time
        for i in range (input_of_time):
            time.sleep(1)
            timer -= 1
    counter = threading.Thread(target=timerClock)



    def restart():
        global numberoftime
        global timer
        global counter
        global clicks
        score.destroy()
        reset.destroy()
        numberoftime = 0
        clicks = 0

        counter = threading.Thread(target=timerClock)

        lable = Label(Main, text=clicks,)
        lable.grid(column=0, row=0, columnspan=3)

        clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='normal')
        clicker.grid(column=0, row=1, columnspan=2)

    def click():
        global score
        global reset
        global numberoftime
        global clicks
        global lable
        global counter
        if numberoftime == 0:
            counter.start()
            numberoftime += 1 
        else:
            if timer == 0:
                Main.place(relx=.5, rely=.2, anchor= CENTER)    
                clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='disabled')
                clicker.grid(column=0, row=1, columnspan=2)

                CPS = clicks%input_of_time
                
                if CPS > 0:
                    cps = clicks/input_of_time
                    score = Label(Main, text=(cps, "CPS"))
                    score.grid(column=0, row=3, columnspan=2)
                else:
                    cps = clicks//input_of_time
                    score = Label(Main, text=(cps, "CPS"))
                    score.grid(column=0, row=3, columnspan=2)

                reset = Button(Main, text="Restart", command=restart)
                reset.grid(column=0, row=4, columnspan=2)  
            else:
                clicks += 1
                lable.destroy()
                lable = Label(Main, text=clicks,)
                lable.grid(column=0, row=0, columnspan=3)   


    clicker = Button(Main, text="click", command=click, pady=10, padx=10)
    clicker.grid(column=0, row=1, rowspan=2, columnspan=2)
    def clear():
        global numberoftime
        global timer
        global counter
        global clicks
        global clicker
        global lable
        score.destroy()
        reset.destroy()
        clicker.destroy()
        lable.destroy()
        numberoftime = 0
        clicks = 0
    def kill():
        try:
            clear()
            back.destroy()
            main2()
        except:
            clicker.destroy() 
            lable.destroy()
            back.destroy()
            main2()

    back = Button(mainWindow, text=("back"), command=kill)
    back.pack(anchor=SE,side="bottom", padx=40, pady=100)
def test4():
    def custom():
        
        def run():
                
            global input_of_time_custom
            E4 = Label(Main)
            try:
                input_of_time_custom = (int(E1.get()))
                E1.destroy()
                E2.destroy()
                E3.destroy()
                E4.destroy()
                back.destroy()
                custom_test()
            except ValueError:
                E4 = Label(Main, text="Thats not a number")
                E4.grid(column=0, row=3, columnspan=2)
                E4 = Label(Main, text="Try again..")
                E4.grid(column=0, row=4, columnspan=2)
                E1.delete(0, END)
                E1.insert(0, "Time (S)")

        def clear(event):
            E1.delete(0, END)

        E1 = Entry(Main, width=10,)
        E1.grid(column=1, row=0, sticky=E)
        E1.insert(0, "Time (S)")
        E1.bind("<Button-1>", clear)
        E2 = Label(Main, text="Duration of test?")
        E2.grid(column=0, row=0, sticky=W)
        E3 = Button(Main, text="Submit", command=run)
        E3.grid(column=0, row=2, columnspan=2)
        E4 = Label(Main)
        E4.grid(column=0, row=3, columnspan=2)
        def clear1():
            E1.destroy()
            E2.destroy()
            E3.destroy()
            E4.destroy()
        def kill():

            try:
                clear1()
                back.destroy()
                main2()
            except:
                clicker.destroy() 
                lable.destroy()
                back.destroy()
                main2()

        back = Button(mainWindow, text=("back"), command=kill)
        back.pack(anchor=SE,side="bottom", padx=40, pady=100)
    
    def custom_test():
        global lable
        lable = Label(Main, text="0")
        lable.grid(column=0, row=0, columnspan=3)
        global numberoftime
        global clicks
        global counter
        clicks = 0
        numberoftime = 0


        def timerClock():
            global timer
            timer = input_of_time_custom
            for i in range (input_of_time_custom):
                time.sleep(1)
                timer -= 1
        counter = threading.Thread(target=timerClock)



        def restart():
            global numberoftime
            global counter
            global clicks
            score.destroy()
            reset.destroy()
            numberoftime = 0
            clicks = 0

            counter = threading.Thread(target=timerClock)

            lable = Label(Main, text=clicks,)
            lable.grid(column=0, row=0, columnspan=3)

            clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='normal')
            clicker.grid(column=0, row=1, columnspan=2)

        def click():
            global score
            global reset
            global numberoftime
            global clicks
            global lable
            global counter
            if numberoftime == 0:
                counter.start()
                numberoftime += 1 
            else:
                if timer == 0:
                    Main.place(relx=.5, rely=.2, anchor= CENTER)    
                    clicker = Button(Main, text="click", command=click, pady=10, padx=10, state='disabled')
                    clicker.grid(column=0, row=1, columnspan=2)

                    CPS = clicks%input_of_time_custom
                    
                    if CPS > 0:
                        cps = clicks/input_of_time_custom
                        score = Label(Main, text=(cps, "CPS"))
                        score.grid(column=0, row=3, columnspan=2)
                    else:
                        cps = clicks//input_of_time_custom
                        score = Label(Main, text=(cps, "CPS"))
                        score.grid(column=0, row=3, columnspan=2)

                    reset = Button(Main, text="Restart", command=restart)
                    reset.grid(column=0, row=4, columnspan=2)  
                else:
                    clicks += 1
                    lable.destroy()
                    lable = Label(Main, text=clicks,)
                    lable.grid(column=0, row=0, columnspan=3)   


        clicker = Button(Main, text="click", command=click, pady=10, padx=10)
        clicker.grid(column=0, row=1, rowspan=2, columnspan=2)
        def clear():
            global numberoftime
            global timer
            global counter
            global clicks
            global clicker
            global lable
            score.destroy()
            reset.destroy()
            clicker.destroy()
            lable.destroy()
            numberoftime = 0
            clicks = 0
        def kill():
            try:
                clear()
                back.destroy()
                main2()
            except:
                clicker.destroy() 
                lable.destroy()
                back.destroy()
                main2()

        back = Button(mainWindow, text=("back"), command=kill)
        back.pack(anchor=SE,side="bottom", padx=40, pady=100)

    custom()
main()











