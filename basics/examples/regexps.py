# Regular expressions
import re
txt = "No#pain,#no#gain"

x = re.search("^No.*gain$", txt)
if x:
    print("x: YES! We have a match!")
else:
    print("x: No match")

y = re.findall('ai', txt)
if y:
    print("y: YES! We have a match:", y)
else:
    print("y: No match")

z = re.split("#", txt)
if z:
    print("z: YES! We have a match:", z)
else:
    print("z: No match")

w = re.sub("#", "*", txt)
if w:
    print("w: YES! We have a match:", w)
else:
    print("w: No match")