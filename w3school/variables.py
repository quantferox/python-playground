""" x = int(10)
y = int(10.5)
# z = int("128.64") #error => string->float->int
z = int(float("128.64"))

print(x, y,z) """

""" x = int(10)
y = float(10.5)
z = str("string")

print(type(x))
print(type(y))
print(type(z))
 """

""" r,g,b = "red", "green", "blue"
print(r)
print(g)
print(b) """

""" r = g = b = "color"
print(r)
print(g)
print(b)  """

""" productList = ["apple","banana","cherry"]
x,y = productList[:2]
print(x)
print(y)
 """

""" print(type(productList))
print(productList[0]) """


""" productList = [
    "apple",
    "banana",
    "cherry",
    "date",
    "fig",
    "grape",
    "kiwi",
    "lemon",
    "mango",
    "orange",
] """
""" print(productList[:3]) #first 3 elements
print(productList[:-3]) #slice last 3 elements """
""" print(productList[0::2]) #odd """
""" print(productList[1::2])  # even """


""" def myfunc():
    global y
    y = 10
    x = 15
    y = x+y
    return x+y

print(myfunc())
print(y) """

""" x = 'awesome'
def myfunc():
  x = 'fantastic' #this x is not global(global x = awesome)
myfunc()
print('Python is ' + x) """ 