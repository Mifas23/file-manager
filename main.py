class Folder:
	''' Folder class with all methods '''

	def __init__(self, name, folders = []):
		self.name = name
		self.folders = folders

	def __str__(self):
		return self.name


	def show_folders(self):
		for i in self.folders:
			print(i)


	def open_folder(self, name):
		for i in self.folders:
			if i.name == name:
				path.append(i)
				return i
		print("There are no such folder")
		return Folder(self.name, self.folders) 


	def add_folder(self, name):
		for i in self.folders:
			if i.name == name:
				print("You already have such folder")
				return
		self.folders.append(Folder(name, []))#!


	def delite_folder(self, name):
		for i in self.folders:
			if i.name == name:
				self.folders.remove(i)
				return
		print("There are no such folder")


	def clear_folder(self):
		self.folders.clear()

	def up(self):
		path.pop(-1)
		return path[-1]



Main_folder = Folder("MAIN")
Main_folder.add_folder("test1")
selected = Main_folder
path = [Main_folder]

modes = {
	"open": "chose a folder to open",
	"add": "enter name for folder you want to add",
	"delite": "chose a folder to delite",
	"up": "back to the prefolder",
	"clear": "clear the folder"
}
mode = None


while True:

	print(selected.name.center(40, "*"), end="\n\n")
	selected.show_folders()
	print()
	
	mode_checker = input() # mode [folder name]
	if not mode_checker.isalnum() and len(mode_checker) < 1: # checking for SPACE
		continue
	mode = mode_checker.split()[0] if mode_checker.split()[0] in modes else None

	if mode_checker == "help":
		for i in modes:
			print(i, " - ", modes[i])

	if mode and len(mode_checker.split(" ")) > 1:
		match mode:
			case "open":
				selected = selected.open_folder(" ".join(mode_checker.split(" ")[1:]))
			case "add":
				selected.add_folder(" ".join(mode_checker.split(" ")[1:]))
			case "delite":
				selected.delite_folder(" ".join(mode_checker.split(" ")[1:]))

	elif mode:
		match mode:
			case "up":
				if len(path) > 1:
					selected = selected.up()
			case "clear":
				selected.clear_folder()