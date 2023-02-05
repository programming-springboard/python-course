sequence = (0, 1, 2, 3, 4, 5)

# В Python також можливо брати "зрізи" (англ. slice) певних послідовностей. Для
# цього знову використовується оператор квадратні дужки

# Синтаксис зрізу: [<start>:<end>:<step>], де кожен з параметрів є не
# обовʼязковим і може бути пропущений.
print("Items [2-4] of sequence:", sequence[2:4])
print("Items [<start>-3] of sequence:", sequence[:4])
print("Items [3-<end>] of sequence:", sequence[3:])
print("Items [1-5] with step 2:", sequence[1:6:2])
print("items [1-5] with step -1:", sequence[5:1:-1])
print("Items in reverse:", sequence[::-1])
print("ALl items of sequence:", sequence[:])
