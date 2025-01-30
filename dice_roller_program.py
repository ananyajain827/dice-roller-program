import random

dice_art={1:("----------------",
             "|              |",
             "|              |",
             "|       ●      |",
             "|              |",
             "|              |",
             "----------------"),
          2:("----------------",
             "|              |",
             "|   ●          |",
             "|              |",
             "|          ●   |",
             "|              |",
             "----------------"),
          3:("----------------",
             "|              |",
             "|   ●          |",
             "|       ●      |",
             "|          ●   |",
             "|              |",
             "----------------"),
          4:("----------------",
             "|              |",
             "|   ●      ●   |",
             "|              |",
             "|   ●      ●   |",
             "|              |",
             "----------------"),
          5:("----------------",
             "|              |",
             "|   ●      ●   |",
             "|       ●      |",
             "|   ●      ●   |",
             "|              |",
             "----------------"),
          6:("----------------",
             "|              |",
             "|   ●      ●   |",
             "|   ●      ●   |",
             "|   ●      ●   |",
             "|              |",
             "----------------")}

dice=[]
total=0


no_of_dice=int(input("enter the number of the dice?"))
for die in range(no_of_dice):
 roll = random.randint(1, 6)
 dice.append(roll)
 total+=roll

for line in range(7):
 for die in dice:
  print(dice_art.get(die)[line],end="        ")
 print()


#for die in range(no_of_dice):
 #for line in dice_art.get(dice[die]):
  #print(line)

print(dice)
print(total)