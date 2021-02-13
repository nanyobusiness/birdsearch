# birdsearch
def birdsearch():
  bird = input("What is the bird name? ")
  numspecies = len(birdname)
  for count in range(numspecies):
    if bird == birdname[count]:
     birdIndex = count
     birdfound = True
  if birdfound == False:
    print("Bird not found.")
    if input("Would you like to add this species? Y//N: ") == "Y":
      inputname, inputno = input("Enter the name and quantity of species, seperated by a space")  
      birdname.append({inputname: inputno}) 
    else:
      print("Going back to menu.")
  else:
    print("Bird found at", birdIndex)
  return birdname

def viewspecies():
  print(birdname)
  return

def menu():
  command = int(input("What you like to do?\nFor bird search, press 1\nTo view the current species, press 2\n: "))
  if command == 1:
   birdsearch()
  elif command == 2:
    viewspecies()
  return command
 
paNo, owNo, huNo, woNo, eaNo = [0,0,0,0,0]
birdname = {"parrot":paNo, "owl":owNo, "hummingbird":huNo, "woodpeckers":woNo, "eagles":eaNo}

command = 1
while command != range(2):
  menu()
