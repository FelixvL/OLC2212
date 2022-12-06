print("goedemorgen")

# operators
# assignment - toekennen van een waarde
#    =        += -= *= /=

# commentaar

# wiskundig
# + - * / %   **    5 % 2    == 1    13 % 5  ==  3

# comparative  -- eindigen boolean
# < == <=  > >=  != 

# logische operators
#   &&  ||    And   Or

getal = 15

print( getal + getal)

getal += 4
getal = getal + 4

print(getal < 40)

if getal == 23 :
    print("ja het is 23")
else:
    print("nee het is geen 23") 
    print("LET HIER OP")

a = 10
b = 20

if a == 11 and b == 20:
    print("yes")

leeftijd = input("Wat is jouw leeftijd")
print("check")
print(leeftijd)
print(leeftijd + leeftijd)
leeftijdingetal = int(leeftijd)  # casten
print(leeftijdingetal + leeftijdingetal)
age = 44 
print("mijn leeftijd = "+str(age))

print("mijn leeftijd 2e : ", age)

# loop
for x in range(15):
    print("lets go", x)

# array   list   []
getallen = [34, 2, 17, 22]
print(getallen[2])
for g in getallen:
    print(g)
    if g == 17:
        print("hiep hiep hoera het is 17")

