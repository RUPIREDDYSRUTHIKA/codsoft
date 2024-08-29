from tkinter import *
expression = ""
def press(num):
  global expression
  expression = expression + str(num)
  equation.set(expression)
def equalpress():
  try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
  except:
    equation.set(" error ")
    expression = ""
def clear():
  global expression
  expression = ""
  equation.set("")
if __name__ == "__main__":
  mw = Tk()
  mw.configure(background="black")
  mw.title("Simple Calculator")
  mw.geometry("320x230")
  equation = StringVar()
  expression_field = Entry(mw, textvariable=equation)
  expression_field.grid(columnspan=4, ipadx=100)
  button1 = Button(mw, text=' 1 ', fg='black', bg='grey',command=lambda: press(1), height=2, width=9)
  button1.grid(row=2, column=0)
  button2 = Button(mw, text=' 2 ', fg='black', bg='grey',command=lambda: press(2), height=2, width=9)
  button2.grid(row=2, column=1)
  button3 = Button(mw, text=' 3 ', fg='black', bg='grey',command=lambda: press(3), height=2, width=9)
  button3.grid(row=2, column=2)
  button4 = Button(mw, text=' 4 ', fg='black', bg='grey',command=lambda: press(4), height=2, width=9)
  button4.grid(row=3, column=0)
  button5 = Button(mw, text=' 5 ', fg='black', bg='grey',command=lambda: press(5), height=2, width=9)
  button5.grid(row=3, column=1)
  button6 = Button(mw, text=' 6 ', fg='black', bg='grey',command=lambda: press(6), height=2, width=9)
  button6.grid(row=3, column=2)
  button7 = Button(mw, text=' 7 ', fg='black', bg='grey',command=lambda: press(7), height=2, width=9)
  button7.grid(row=4, column=0)
  button8 = Button(mw, text=' 8 ', fg='black', bg='grey',command=lambda: press(8), height=2, width=9)
  button8.grid(row=4, column=1)
  button9 = Button(mw, text=' 9 ', fg='black', bg='grey',command=lambda: press(9), height=2, width=9)
  button9.grid(row=4, column=2)
  button0 = Button(mw, text=' 0 ', fg='black', bg='grey',command=lambda: press(0), height=2, width=9)
  button0.grid(row=5, column=0)
  plus = Button(mw, text=' + ', fg='black', bg='grey',command=lambda: press("+"), height=2, width=9)
  plus.grid(row=2, column=3)
  minus = Button(mw, text=' - ', fg='black', bg='grey',command=lambda: press("-"), height=2, width=9)
  minus.grid(row=3, column=3)
  multiply = Button(mw, text=' * ', fg='black', bg='grey',command=lambda: press("*"), height=2, width=9)
  multiply.grid(row=4, column=3)
  divide = Button(mw, text=' / ', fg='black', bg='grey',command=lambda: press("/"), height=2, width=9)
  divide.grid(row=5, column=3)
  equal = Button(mw, text=' = ', fg='black', bg='grey',command=equalpress, height=2, width=9)
  equal.grid(row=5, column=2)
  clear = Button(mw, text='Clear', fg='black', bg='grey',command=clear, height=2, width=9)
  clear.grid(row=5, column='1')
  Decimal= Button(mw, text='.', fg='black', bg='grey',command=lambda: press('.'), height=2, width=9)
  Decimal.grid(row=6, column=0)
mw.mainloop()









