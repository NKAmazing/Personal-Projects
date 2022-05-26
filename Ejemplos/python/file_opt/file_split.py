
txt = "welcome to the jungle"
x = txt.split(", ")

fd = open("/tmp/txt.txt", "w")
fd.write(str(x))

fd = open("/tmp/txt.txt", "r")



lines = fd.readlines()

for line in lines:
	print(line)
