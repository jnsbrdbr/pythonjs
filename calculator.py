from tkinter import *


class calculator:
    def __init__(self,master):
        self.master=master
        master.title("calculator")
        self.equation=Entry(master, width=36, borderwidth=5)
        self.equation.grid(row=0, column=0, columnspan=100, padx=10, pady=10)

        self.createbutton()
        

    def createbutton(self):
    
        c0=self.addbutton(0)
        c1=self.addbutton(1)
        c2=self.addbutton(2)
        c3=self.addbutton(3)
        c4=self.addbutton(4)
        c5=self.addbutton(5)
        c6=self.addbutton(6)
        c7=self.addbutton(7)
        c8=self.addbutton(8)
        c9=self.addbutton(9)
        c10_add=self.addbutton("+")
        c11_minus=self.addbutton("-")
        c12_mul=self.addbutton("*")
        c13_div=self.addbutton("/")
        c14_equal=self.addbutton("=")
        c15_clear=self.addbutton("c")
        

        row_one=[c7,c8,c9,c10_add]
        row_two=[c4,c5,c6,c11_minus]
        row_three=[c1,c2,c3,c12_mul]
        row_four=[c15_clear,c0,c14_equal,c13_div]



        r=1
        for row in [row_one, row_two, row_three, row_four]:
            c=0
            for buttn in row:
                buttn.grid(row=r, column=c ,columnspan=1)
                c+=1
            r+=1


    def addbutton(self,value):

            return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))


    def clickButton(self, value):
        
        current_equation=str(self.equation.get())

        if value == 'c':
            self.equation.delete(-1, END)

        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1,END) 
            self.equation.insert(0, answer)  #answer it

        else:
            self.equation.delete(-1, END) #do not let the previous number to act again
            self.equation.insert(0, current_equation+value)

        


if __name__=='__main__':
    root=Tk()
    my_gui = calculator(root)


    root.mainloop()