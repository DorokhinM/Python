with open('example.txt', 'a') as ex:
  for i in range(10):
    ex.write(str(i)+"\n")


ex = open("example.txt", "r")
numbers = []

for i in ex:
  numbers.append(int(i))

print(sum(numbers))