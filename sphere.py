print()
print()
print("Sphere TSA founder Activated")
print()
r = input("(Type none if not given)Radius: ")

def find():
    print()
    print("TSA of Circle  = 4×𝝅r² ")
    print(f"Radius = {r}")
    print(f"So, 4×22/7{r}² ")
    csa = 4*22/7*int(r)**2
    print()
    print(f"So Total Surface Area = {csa}cm²")
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



