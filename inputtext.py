import os

settext = input("Vorname? ")
with open("settext_file.py", "w") as f:
    f.write("settext = '" + settext + "'")

settextb = input("Nachname? ")
with open("settextb_file.py", "w") as f:
    f.write("settextb = '" + settextb + "'")
    
settextc = input("Zusatz? ")
with open("settextc_file.py", "w") as f:
    f.write("settextc = '" + settextc + "'")

print ("Eingabe wurde gespeichert!")
