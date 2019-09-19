#Project1File.py start
#inputs
outputFile = open("Prog1/DAT1.TXT", "w")
inputFile = open("Prog1/TEST1.TXT")

def inputMargins():
  global leftMargin 
  global rightMargin
  leftMargin = int(raw_input("Left margin: "))
  rightMargin= int(raw_input("Right margin: "))
  if leftMargin + rightMargin > 4:
    print "margins too large, need to fit: On some other shit"
    inputMargins()
  if leftMargin < 0:
    print "no negative numbers"
    inputMargins()
  if rightMargin < 0:
    print "no negative numbers"
    inputMargins()

def isThereSpace(word, index):
  if(index + len(word) < end):
    return True
  else: return False

def putSpaces(word):
  if word[-1] == "!" or word[-1] == "." or word[-1] == "?":
    return True
  else: return False

inputMargins()
start = leftMargin * 12
end = 96 - (rightMargin * 12)
spaces = "            "

#put words into array
wordArray = inputFile.read().split()

arrIndex = 0
lineIndex = 0
while arrIndex < len(wordArray):
  isSpace = True
  preSpace = 0
  outputFile.write(spaces * leftMargin)
  lineIndex = start
  while isSpace == True and arrIndex < len(wordArray):
    if isThereSpace((" " * preSpace)  + wordArray[arrIndex], lineIndex):
      outputFile.write((" " * preSpace) + wordArray[arrIndex])
      lineIndex += len(wordArray[arrIndex] + (" " * preSpace))
      if putSpaces(wordArray[arrIndex]):
        preSpace = 2
        arrIndex += 1
      else: 
        preSpace = 1
        arrIndex += 1
    
    else: isSpace = False #end inner while
      
  outputFile.write("\r\n") #end outer while

#output
outputFile.close()
inputFile.close()
