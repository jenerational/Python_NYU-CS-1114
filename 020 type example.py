
xyz = input("Enter a number.")

try:
    int(xyz)
except ValueError:
    try:
        print("hi")
        float(xyz)
    except ValueError:
        xyz = xyz

print(type(xyz))

 
