print()
print()
print("Cylinder TSA founder Activated")
print()
h = input("height : ")
r = input("(Type none if not given)Radius: ")
\
def find():
    print()
    print("TSA = 2πr (h + r)")
    print(f"Radius = {r}")
    print(f"So, 2×22/7×{r} ({h} + {r}) ")
    x = int(h) + int(r)
    tsa = 2*22/7*int(r)*int(x)
    print()
    print(f"So Total Surface Area = {tsa}cm")
    print()
    print()

if r == "none":
    d = int(input("what is Diameter: "))
    r = d/2
    print("d/2 = r")
    print(f"So, {d}/2 = r = {r}")
    find()
else:
    find()



