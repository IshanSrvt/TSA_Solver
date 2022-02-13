
print("Hey I can find Total Surface Area for you ")
print()
x = input('For Cube Type "cube" For sphere type "sphere" For Cylinder type "cylinder" : ')

if x == 'cube':
    exec(open("cube.py").read())
elif x == 'sphere':
    exec(open("sphere.py").read())
elif x == 'cylinder':
    exec(open("cylinder.py").read())
else:
    print("Try Again")
    