"""
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

count = 0
while count <= 150:
    print(count)
    count +=1


for x in range(5, 1001, 5):
    print(x)

for y in range(1, 101):
    if y%10 == 0:
        print("Coding Dojo")
    elif y%5 == 0:
        print("Coding")
    else:
        print(y)


sumOfAllOdds = 0
currentCount = 0
while currentCount <= 500000:
    if currentCount %2 != 0:
        sumOfAllOdds += currentCount
    currentCount += 1
print(sumOfAllOdds)

for z in range(2018, 0, -4):
    print(z)

lowNum = 2
highNum = 9
mult = 3
for zx in range(lowNum, highNum+1):
    if zx%mult == 0:
        print(zx)