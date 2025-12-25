# swapping with temp/third variable 
x = 13 
y = 12

temp = x
x = y
y = temp

print("x =", x)
print("y =", y)

# swapping without temp/third variable 
x1 = 13 
y1 = 12

x1, y1 = y1, x1

print("x1 =",x1)
print("y1 =",y1)