produce = [["Mangoes", 3], ["Oranges", 4], ["Pineapples", 2], ["Coconuts", 1]]

print(produce)
print(produce[1])
print("You have", produce[1][1], "oranges.")

oranges_total = produce[1][1]

print(oranges_total)

produce[1][1] = 3

print(oranges_total)
print(produce[1][1])

#interestingly it doesn't update oranges_total so you have to update oranges total

oranges_total = produce[1][1]

print(oranges_total)

produce[1].remove(3) 

print(produce[1])

produce[1].append(4)

print(produce[1][1])

produce_update = produce + [["Apples", 5], ["Kiwis", 4]]

print(produce_update)