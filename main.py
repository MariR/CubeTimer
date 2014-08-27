from Tkinter import *
from sys import *
from os import *
import time


global inprocess
inprocess = 0

# -------------GUI ------------------

def main():
	root = Tk()
	frame()
	root.mainloop()

def frame():
	f = Frame()
	f.bind('<space>',space_event)
	f.focus_set()
	f.grid()

	label("Cube Timer",1,1,23)
	label("Press Space to start the Timer",2,1,12)

def label(_text, _row, _column, _fontsize):
	l = Label(text=str(_text), font=("Arial", _fontsize))
	l.grid(row=_row, column=_column)

def button(_text, _row, _column, _command):
	b = Button(text=str(_text), command = _command)
	b.grid(row=_row, column=_column)

def start_button(start):
	
	global start_button_text
	
	if start == True:
		start_button_text = "Stop"
	if start == False:
		start_button_text = "Start"
	

# ------------------Timer Programm ---------


def final_time(start_time, end_time):

	global final_time
	final_time = end_time - start_time
	print final_time

def space_event(event):
	wire()

def wire():

	global inprocess
	inprocess = inprocess + 1

	if inprocess == 1:
		start_time()

	if inprocess == 2:
		end_time()


def start_time():
	start_time = time.time()
	print "Timer started..."
	return start_time

def end_time():
	end_time = time.time()
	print "... Timer stopt."
	return end_time

	final_time()

def date():
	local_time = time.asctime(time.localtime(time.time()))
	return local_time

def write(file_name, final_time, date):
	temp_data = open(file_name, "a")
	content = str(round(final_time, 3)) + "[" + str(date) + "]"
	temp_data.write(content)
	temp_data.close()
	print "time saved"

main()