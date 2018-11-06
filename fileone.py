 #Error handlin

try:
     file = open("king.txt","w")
     file.write("My name is king")


except IOError:
 print("Unable")

else:
 print("File created and written successfully")