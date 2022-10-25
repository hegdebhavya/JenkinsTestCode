prev = 0
next = 1
sum = 0
while (sum<100):
    sum = prev + next
    if sum<100:
        print(sum)
    prev = next
    next = sum
