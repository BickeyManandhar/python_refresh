# for loop
for i in range(1,6):
    print("For loop iteration number:", i)

l = [41,27,63,49,58,56]

for item in l:
    print("List item:", item)

# while loop
j = 1
while (j<6):
    print("While loop iteration number:", j)
    j += 1

# for loop with else
for k in range(1,4):
    print("For loop with else iteration number:", k)
else:
    print("For loop completed")

# break
for m in range(1,10):
    if m == 5:
        print("Breaking the loop at:", m)
        break
    print("Loop iteration number before break:", m)

# continue
for n in range(1,6):
    if n == 3:
        print("Continuing at:", n)
        continue
    print("Loop iteration number:", n)

# pass
for p in range(1,6):
    if p == 4:
        print("Passing at:", p)
        pass # placeholder, does nothing, used when program may throw an error
    print("Loop iteration number:", p)