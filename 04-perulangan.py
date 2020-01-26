# WHILE
count = 0
while (count < 9):
    print("The count is ", count)
    count = count + 1

print("Finish!!")

# for loop
rpg = ["brigandine", "saga frontier", "breat of fire"]
for game in rpg:
    print("Saya suka RPG", game)

# nested loop
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i % j):
            break
        j = j + 1
    if (j > i/j):
        print(i, " is prime")
    i = i + 1

print("Good bye!")
