def print_lyrics():
	print ("i'm a programmer, and i'm okay.")
	print ("i code all night, and i code all day")
def repaeat_lyrics(count=1):
	for number in range(count):
		print_lyrics()
	print("{}############".format(number), end=".")
	print_lyrics()
	print("############")
def main():
	repaeat_lyrics()
	repaeat_lyrics(4)
if __name__== "__main__":
	main()