#(the "r" in the beginning is making sure that the string is being treated as a "raw string")
#r"ain\B"
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
