import random
print ("\n-------------------------------")
print(".:gissaTalet:.\n\n")

print("gissa ett tal mellan 1 och 10 och prova lyckan")
slumptal = random.randrange (1, 10)
#print(f"Fusk: {slumptal}")
i = 0
hittat = False
 #loop
while i < 3:
    gissatal =input("mata in tal: " )
    
    if slumptal == int(gissatal):
      hittat = True
      print("\ rätt svar! \n")
    
    i += 1

if hittat:
  print("\nbra gjort här e fem spän")
else:
  print("\n dålig")

print("\n-------------------------------")