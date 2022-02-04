import random
import string
import cmd
import time
import os
import sys

str1 = string.ascii_letters + string.digits

banner = """
                       _   _     _             
     /\               | | | |   (_)            
    /  \   _ __  _   _| |_| |__  _ _ __   __ _ 
   / /\ \ | '_ \| | | | __| '_ \| | '_ \ / _` |
  / ____ \| | | | |_| | |_| | | | | | | | (_| |
 /_/    \_\_| |_|\__, |\__|_| |_|_|_| |_|\__, |
                  __/ |                   __/ |
                 |___/                   |___/ 
                              Author By LkB1ng
"""

def animate_banner(tick = 0.001):
	for c in banner:
		time.sleep(tick)
		print(c,end="")
animate_banner()

class options(cmd.Cmd):
	intro = "A small program to record the learning process.Input 'help' for help:)"
	prompt = "Use>"

	def do_rndpwd(self, _):
		"Use rndpwd_builder"
		self.rndpwd()

	def emptyline(self):
		print("Please input command!")

	def do_exit(self, _):
		"Exit"
		exit(0)

	def rndpwd(self):
		#建立循环随机输出密码
		lenth = input("How long do you want to your password to be? ")
		for i in range(0,int(lenth)):
			rnd = random.randint(0,57)
			print(str1[rnd],end='')
		print("\n")

if __name__ == '__main__':
	try:
		options().cmdloop()
	except:
		exit()