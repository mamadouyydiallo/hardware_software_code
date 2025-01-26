def conversation():
	print("Do you like coding in python? Answer yes or no")
	answer = input().lower().strip()
	if answer == "yes":
		print("That's good - the United States needs more coders!!")
	elif answer == "no":
		print("perhaps you will change your mind ")
	else:
		print("i don't understand?")
		conversation()
	def main():
		print("Welcome to my conversation program")
		conversation()
		print("thanks for chatting with me")
	if __name__ =="__main__":
		main()

