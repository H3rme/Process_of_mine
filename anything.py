import random
import string
import cmd

str1 = string.ascii_letters + string.digits

class options(cmd.Cmd):
	intro = "A small program to record the learning process.Input 'help' for help:)"
	prompt = "Use>"

	def do_rndpwd(self, _):
		"Use rndpwd_builder"
		self.rndpwd()

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
	options().cmdloop()