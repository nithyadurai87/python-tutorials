txt = open("exercises.txt")
print txt.read()
txt.seek(0)
print txt.readline()
txt.close()

txt = open("exercises.txt",'a')
content = raw_input("Enter here:")
txt.write('\n'+content)
txt.close()

