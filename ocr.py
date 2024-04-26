import os
import pytesseract
import re
from alive_progress import alive_bar

def main():
   os.system('cls')
   #Make current location to current working directory instead of one directory up
   __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
   picturesFolder = (__location__ + "\\pictures1")
   allEntry = ""
   dir = os.listdir(picturesFolder)
   length = len(dir)
   count = 0
   print("Processing images in "+ picturesFolder)
   print()
   print("Progress:")
   #Create progress bar
   with alive_bar(length) as bar: 
      for filename in os.listdir(picturesFolder):
         count += 1
         newEntry = pytesseract.image_to_string(picturesFolder + "\\" + filename, lang='eng' )
         allEntry = allEntry + newEntry
         #Trigger update for progress bar
         bar()
   #Regex for finding MAC address, negative lookahead to skip duplicates.
   result = re.findall(r"(([A-F0-9]{2}[-]){1,5}([A-F0-9]{2})(\n))(?![\s\S]*\1)", allEntry)
   print()
   print("Results: ")
   print("==========================================")
   for string in result:
      print (string[0])

   print ("Count: %d" % len(result))
   print()
   input()
   print(allEntry)

if __name__ == '__main__':
    main()