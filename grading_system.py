print("Marks obtained in 5 subjects : ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())
tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5
if avg>= 91 and avg<= 100:
    print("A")
elif avg<= 91 and avg>= 80:
    print("B")
elif avg<= 80 and avg>= 71:
    print("C")
elif avg<= 71 and avg>= 0:
    print("D")
else :
    print("Invalid input")