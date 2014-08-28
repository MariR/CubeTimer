from Tkinter import *
from sys import *
import os
import time


global inprocess
inprocess = False

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


# ------------------Timer Programm ---------


def final_time():
	global e_time
	global s_time
	f_time = e_time - s_time
	print f_time
	date()
	file_name = "test"
	write(file_name, f_time)

def space_event(event):
	wire()

def wire():

	global inprocess

	if inprocess == False:
		start_time()	
	else: 
		end_time()
		

def start_time():
	global inprocess
	inprocess = True
	global s_time
	s_time = time.time()
	print "Timer started..."


def end_time():
	global inprocess
	inprocess = False
	global e_time
	e_time = time.time()
	print "... Timer stopt."
	final_time()

def date():
	global local_time
	local_time = time.asctime(time.localtime(time.time()))

def write(file_name, final_time):
	global local_time
	temp_data = open(file_name, "a")
	content = str(round(final_time, 3)) + "			[" + str(local_time) + "]\n"
	temp_data.write(content)
	temp_data.close()
	print "time written in %r" %(file_name)

main()