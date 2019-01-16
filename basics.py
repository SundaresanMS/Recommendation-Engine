# example =[1,5,6,1,5,4,8]
# for no in example:
	# print (no)
	
	
# for no in range(1,10):
	# print (no)
	
	
	
	
	# #basics of functions
	
	
# def example():
	# return 0
	
	
# # print (example(3))


# def simple(num1,num2):
	# return num1+num2

# # print(simple(5))


# def simple(num1,num2=5):
	# return num1+num2
	
	
	
# print(simple(5,10))



# #saving data to a file 
# #writing and appending


# text ='Sample text to save\nNew Line!'
# # print (text)

# newinfo ='Sundaresan'

# saveFile= open('exampleFile.txt','w')

# saveFile.write(text+text)



# # saveFile1= open('exampleFile1.txt','w')

# # saveFile1.writelines(text+text)

# # Append= open('exampleFile.txt','a')

# # Append.write(newinfo)





# readfile =open('exampleFile1.txt','r').read()
# print(readfile)



# #Classes

# # Use class intead of modules 
# # class is treated  as if equal to a module 

# # it is a way of grouping things together

# class calculator:
	
	# def add(x,y):
		# return x+y

	# def sub(x,y):
		# return x-y
	# def	multiply(x,y):
		# return x*y
		
	# def divide(x,y):
		# return x/y
	


# print (calculator.divide(51,10))




# #Built In Functions

# exNUm=5
# exNUm1=-5
# print (abs(exNUm))



# if abs(exNUm) ==abs(exNUm1):
 # print ('True')
 
 

 # help('print')


 # exlist=[5,2,6,7,8,0]
 # print (max(exlist))


# print (min(exlist))




# import os
# import time

# curDir =os.getcwd()
# print (curDir)



# os.mkdir('Newdir')

# time.sleep(2)

# os.rename('Newdir','Newdir2')

# os.rmdir('Newdir')
# os.rmdir('Newdir2')



# import sys

# sys.stderr.write('This is stderror text\n')
# sys.stderr.flush()

# sys.stdout.write('This is stdoutput text\n')



# print (sys.argv)

# if len(sys.argv) >1:
	# print (float(sys.argv[1])+5)

	
	
import urllib.request

# url ='https://www.google.com'
# url ='https://pythonprogramming.net/introduction-intermediate-python-tutorial/'


# x =urllib.request.urlopen(url)

# print (x.read())



# url ='https://pythonprogramming.net'

# values={'s' :'basic',	
        # 'submit' :'search'

# }


# data =urllib.parse.urlencode(values)
# data =data.encode('utf-8')


# req =urllib.request.Request(url,data)
# resp =urllib.request.urlopen(req)
# respData =resp.read()
# print (respData)



# try:
	# url = 'http://www.google.com/search?q=test'
	# headers={}
	# headers['User-Agent'] ='Mozilla/5.0 (Amiga; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14'
	
	# req =urllib.request.Request(url,headers=headers)
	# resp =urllib.request.urlopen(req)
	
	# respData =resp.read()
	# print (respData)
# except Exception as e:
	# print (str(e))

	
# saveFile =open('withHeaders.txt','w')
# saveFile.writelines(str(respData))
	
"""

	
Identifier
\d any number
\D anything but a number
\s space
\S anything but a Space
\w any character 
\W anything but a character
. = any character ,except new line
\b the whitespacec around words
\. a period

Modifier
{1,3} we are expecting 1-3
+ Match 1 or More
? Match 0 or more
* Match 0 or more
$ match the end of a string
^ matching the beginning of the string
| ether or              \d{1-3} | \w {5-6}
[] range or 'variance'
{x} expecting 'x' amount 


White Space Characters:
\n New line
\s space
\t tab
\e escape
\f form feed
\r return


DONT FORGET!:

. + * ? [ ] $ ( ) { } | \

"""
	
	
# import re 

# example =' Jessica is 15 years old, and Daniel is 27 years old. Edward is 97, and his grandfather, Oscar is 102.'
	
	
	
# ages= re.findall(r'\d{1,3}',example)

	
# names= re.findall(r'[A-Z][a-z]*',example)

# print (ages)

# print (names)





from tkinter import *
from PIL  import Image,ImageTk


class Window(Frame):
	def __init__(self,master = None):
		Frame.__init__(self,master)
		
		self.master =master
		self.init_window()

	def init_window(self):
		self.master.title('Analytics')
		
		self.pack(fill =BOTH ,expand=1)
		
		# quitButton = Button(self,text='Quit',command = self.client_exit)
		
		# quitButton.place(x=0,y=0)
		
		menu = Menu(self.master)
		self.master.config(menu=menu)
		file =Menu(menu)
		file.add_command(label ='Exit',command=self.client_exit)
		file.add_command(label ='New',command=self.master)
		
		menu.add_cascade(label ='File',menu =file)
		
		
		edit =Menu(menu)
		edit.add_command(label ='Undo')
		edit.add_command(label ='Show Image',command =self.showImg)
		edit.add_command(label ='Show Text',command =self.Showtxt)
		
		menu.add_cascade(label ='Edit',menu =edit)
		
		
	def showImg(self):
		load =Image.open('pic.jpeg')
		render =ImageTk.PhotoImage(load)
		
		img =Label(self, image =render)
		img.image =render
		img.place(x=0,y=0)
		
	def Showtxt(self):
		text =Label(self,text='Hey there good looking')
		text.pack()

	
	def client_exit(self):
		# self.master.quit()
		exit()
		
root =Tk()
root.geometry("400x300")

app =Window(root)

root.mainloop()



