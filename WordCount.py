#WordCount.py
#Name: Nathan Heavican
#Date: 3/1/26
#Assignment: Lab 6

def main():
  #textFile = open("gettysberg.txt", 'r')
  filename = input("Enter filename: ")
  
  try:
    with open(filename, 'r') as f:
  
      lineCount = 0
      wordCount = 0
      characterCount = 0

      for line in f:
        lineCount = lineCount + 1
        words = line.split()
        for w in words:
          wordCount = wordCount + 1
        characterCount = characterCount + len(line)
    
    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("Characters (including spaces/newlines):", characterCount)

  except FileNotFoundError:
    print("Error: File not found.")

if __name__ == '__main__':
  main()
