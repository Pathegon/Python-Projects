
nMax = int(round(float(input("Enter a variable for the power of x: \n"))))
xMax = int(round(float(input("Enter the amount of integers you want to multiply x with: \n"))))

for i in range(1, nMax + 1):
        print("%10d" % i, end="",)
print()
for i in range(1, nMax+1):
        print("%9s" % "x", end = " ")
print()
print("-"*(xMax*13))

for i in range(1, xMax+1):
        for n in range(1, nMax+1):
                print("%10d" % i**n, end="")
        print()
