from Tkinter import *
from time import *
from sys import *
from os import *


# -------------GUI ------------------

def main():
	root = Tk()
	frame()
	root.mainloop()
	read_filelist()

def frame():
	f = Frame()
	f.grid()

	def instert_time(l_num, content):
		time_list.insert(l_num, content)

	label("Timer text here",1,1)
	button("start",2,1,start_time)
	button("reload files",2,2,read_filelist)

	time_list = Listbox()
	time_list.grid(row=1, column=2)
	instert_time(1, "entry01")
	instert_time(2, "entry02")



def label(_text, _row, _column):
	l = Label(text=str(_text))
	l.grid(row=_row, column=_column)

def button(_text, _row, _column, _command):
	b = Button(text=str(_text), command = _command)
	b.grid(row=_row, column=_column)

# ------------------Timer Programm ---------


def final_time(start_time, end_time):

	final_time = end_time - start_time
	print final_time
	return final_time

def start_time():
	start_time = time.time()
	return start_time

def end_time():
	end_time = time.time()
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

def read_filelist():
	for f in /timelists:
		print f

main()