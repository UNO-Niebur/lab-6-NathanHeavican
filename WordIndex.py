#WordIndex.py
#Name: Nathan Heavican
#Date: 3/1/26
#Assignment: Lab 6

def main():
  #textFile = open("fish.txt", 'r')
  filename = input("Enter filename: ")
  with open(filename, 'r') as textFile:
  
    words = {} #create an empty dictionary
    lineNum = 0

    for line in textFile:
      lineNum = lineNum + 1
      splitwords = line.replace("—" , " ") #separating words that are combined by "—"
      wordList = splitwords.split()
      for w in wordList:
        w = w.lower()
        w = w.replace("," , "")
        w = w.replace("." , "")
        w = w.replace("!" , "")
        w = w.replace("?" , "")
        w = w.replace(";" , "")
        w = w.replace(":" , "")

        if w in words:
          if lineNum not in words[w]:
            words[w].append(lineNum)
        else:
          words[w] = [lineNum]
  
  for word in sorted(words):
    print(word, sorted(set(words[word])))

if __name__ == '__main__':
  main()
