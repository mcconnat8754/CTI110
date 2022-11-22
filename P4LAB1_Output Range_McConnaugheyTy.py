x = int(input())
y = int(input())

if x > y:
    print("Second integer can't be less than the first.")

while x <= y:
    if x == y:
        print(y, '')
        break
    if (x + 5) <= y:
        print(x, end= ' ')
        x += 5
    else: 
        print(x, '')
        break



