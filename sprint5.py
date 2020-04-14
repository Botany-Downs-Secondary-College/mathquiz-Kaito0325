#GUIObjectOriented.py
#Creates a Frame
#K.Kasuya, Feb 2020

from tkinter import * #imports all modules of tool kit interface, * is called wildcard
from random import *

class MathQuiz: #OOP will have classes and functions will be part of classes
    #Keep your widgets in instanceiate (_init_) method, each instance (object) must have self. as prefix
    def __init__(self, parent):
    

        """Widgets for frame 1"""
        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)

        self.TitleLabel = Label(self.frame1, bg = "black", fg = "white", width = 30, padx = 30, pady = 10,
                       text = "Welcome to Math Quiz", font=("Times", "16", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)

        self.NameLabel = Label(self.frame1, text = "Name" , width = 20, pady = 5)
        self.NameLabel.grid(row = 2, column = 0, sticky = W)

        """checking to see something entered"""
        self.name = StringVar()
        self.name.set("")
        self.NameEntry = Entry(self.frame1, textvariable = self.name, bg = "white", fg = "black")
        self.NameEntry.grid(row = 2, column = 1, sticky = W)

        self.AgeLabel = Label(self.frame1, text = "Age", width = 20, pady = 5)
        self.AgeLabel.grid(row = 3, column = 0, sticky = W)

        self.age = IntVar()
        self.age.set("")
        self.AgeEntry = Entry(self.frame1, textvariable = self.age, bg = "white", fg = "black")
        self.AgeEntry.grid(row = 3, column = 1, sticky = W)

        self.warning = Label(self.frame1, text = "")
        self.warning.grid(row = 4, column = 1, columnspan = 3)

        self.SelectLabel = Label(self.frame1, text = "Select Diffculty", width = 20, font=("Times", "14", "bold italic"))
        self.SelectLabel.grid (row = 5, column = 0, sticky = W)                         

        self.radio_var = StringVar()
        self.radio_var.set(1)

        self.options = ["Easy", "Medium", "Hard"]
        self.options_lvl = StringVar()
        self.options_lvl.set(0)
        self.options_btns = []

        for i in range(len(self.options)):
            rb = Radiobutton(self.frame1, variable = self.options_lvl, value = i, text = self.options[i], anchor = W, padx = 50,
            width = "10", height = "2")
            self.options_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)
        
        #Button that calls frame 2
        self.button1 = Button(self.frame1, text = "Next", anchor = W, command = self.show_frame2)
        self.button1.grid(row = 9, column = 1)
        
        """Widgets for frame 2"""
        self.index = 0
        self.score = 0
        self.frame2 = Frame(parent, height = "450", width = "400") #notice grid() method is missing here

        self.questions = Label(self.frame2, bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                               text = "Answer Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(columnspan = 2)

        self.QuestionLabel = Label(self.frame2, text ="", width = 15, height = 3)
        self.QuestionLabel.grid(row = 1, column = 0, sticky = W)

        self.AnswerEntry = Entry(self.frame2, width = 20)
        self.AnswerEntry.grid(row = 1, column = 1, sticky = W)

        self.quiz_label = Label(self.frame2, text = "Problems", font = ("Times", "14", "bold"))
        self.quiz_label.grid(row = 1, column = 2, columnspan = 5, sticky = "EW")

        self.feedback = Label(self.frame2, text = "Click Check Answer button")
        self.feedback.grid(row = 2, column = 0, columnspan = 4)
         
        self.home = Button(self.frame2, text = "Home", anchor = W, command = self.show_frame1)
        self.home.grid(row = 2, column = 0)

        self.check = Button(self.frame2, text = "Check answer", anchor = W, command = self.check_answer)
        self.check.grid(row = 2, column = 3)
    

        """Widgets for Report frame"""
        self.report_frame = Frame(parent, height = "450", width = "400")
        self.report_frame.grid_propagate(0)

        report_page = ["Name", "Age", "Score"]
        self.report_labels = []

        for i in range(len(report_page)):
            lb = Label(self.report_frame, text = report_page[i], anchor = W, width = "7", height = "2", font = ("Times", "22", "bold"))
            self.report_labels.append(lb)
            lb.grid(row = 1, column = i+1, sticky = "EW")

        self.report_name = Label(self.report_frame, textvariable = self.name)
        self.report_name.grid(row = 3, column = 1, sticky = "EW")

        self.report_age = Label(self.report_frame, textvariable = self.age)
        self.report_age.grid(row = 3, column = 2, sticky = "EW")

        self.report_score = Label(self.report_frame, text = "")
        self.report_score.grid(row = 3, column = 3)
            

    def show_frame1(self):
        self.frame2.grid_remove() #removes frame 2
        self.report_frame.grid_remove()
        self.frame1.grid()


        
    def show_frame2(self):
        try:

            if self.name.get() == "":
               self.warning.configure(text = "Please Enter your Name")
               self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.warning.configure(text = "Please Enter Text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()
                
            elif self.age.get() == "":
                self.warning.configure(text = "Please Enter your Age")
                self.AgeEntry.delete(0, END)
            elif self.age.get() > 12:
                self.warning.configure(text = "You are too old to try this quiz")
                self.AgeEntry.delete(0, END)   
            elif self.age.get() <= 0:
                self.warning.configure(text = "You need to enter a number higher than 0")
                self.AgeEntry.delete(0, END)
            elif self.age.get() <=7:
                self.warning.configure(text = "You are too young to try this quiz")

            else:
                self.frame1.grid_remove()
                self.frame2.grid(row = 1, columnspan = 4)
                self.next_problem()

        except:
            self.warning.configure(text = "Please enter your age")
            self.AgeEntry.delete(0, END)
            self.next_problem()

        
    def show_frame1(self):
        self.frame2.grid_remove() #removes frame 2
        self.frame1.grid()

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct!")
                self.score += 1
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()
            else:
                self.feedback.configure(text = "Incorrect!, Try again")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()

        except:
             self.feedback.configure(text = "Please enter a number")
             self.AnswerEntry.delete(0, END)
             self.AnswerEntry.focus()

        if self.score <= 5:
            self.report_score.configure(text = str(self.score))

    def next_problem(self):
        """ Creates a problem, stores the correct answer """
        x = randrange(10)
        y = randrange(10)
        self.select = self.options_lvl.get()
        
        if self.select == "0":
            easy_text = str(x) + " + " + str(y) + " = "

            self.answer = x + y
            self.index += 1

            self.QuestionLabel.configure(text = easy_text)
            self.quiz_label.configure(text = "Question" + str(self.index)+ "/5")

        elif self.select == "1":
            medium_text = str(x) + " - " + str(y) + " = "

            self.answer = x - y
            self.index += 1

            self.QuestionLabel.configure(text = medium_text)
            self.quiz_label.configure(text = "Question" + str(self.index)+ "/5")

        else:

            hard_text = str(x) + " x " + str(y) + " = "

            self.answer = x * y
            self.index += 1

            self.QuestionLabel.configure(text = hard_text)
            self.quiz_label.configure(text = "Question" + str(self.index)+ "/5")

        if self.index >= 6:
            self.frame2.grid_remove()
            self.report_frame.grid(row = 1, columnspan = 4)


#code in the main routine
#create a window with title and control its size and location
#code in the main routine

if __name__ == "__main__": #checking to see class name is the main module
    root = Tk() # root is a variable that calls the module to create GUI
    frames = MathQuiz(root)
    root.title("OOP") #Window title appears on top left
    root.geometry("600x300+850+0")
    root.mainloop()


      
        
                       





#code in the main routine
#create a window with title and control its size and location
#code in the main routine

if __name__ == "__main__": #checking to see class name is the main module
    root = Tk() # root is a variable that calls the module to create GUI
    frames = MathQuiz(root)
    root.title("Maths") #Window title appears on top left
    root.geometry("600x300+850+0")
    root.mainloop()
