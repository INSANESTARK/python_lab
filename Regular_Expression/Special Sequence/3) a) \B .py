#Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#r"\Bain"
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
