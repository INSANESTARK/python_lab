#(the "r" in the beginning is making sure that the string is being treated as a "raw string")
#r"ain\b"
import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")