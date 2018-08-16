def rightRightTriangle(height):
    x = ""
    for i in range(height):
        x = x + (" "*(height - i-1) + "*" *(i+1)) + "\n"
    return (x)
def triangle(height):
    x = ""
    for i in range(height):
        x = x + (" "*(height - i-1) + "*" *(2*i+1)) + "\n"
    return (x)

def semicircle(radius):
    import math
    str = ''
    for count in range(radius -1, -radius, -1):
        x = math.sqrt((radius**2) - (count**2))
        x = int(round(x))
        str += (x * '*') + '\n'
    return str

def aLaCarte():
        print("Shapes  Menu ")
        print (21 * "-")
        print ("1. Righ Triangle")
        print ("2. Triangle")
        print ("3. Semicircle")
        print ("4. Exit")
        print("")
  
ans=True      
  
while ans:          
    aLaCarte()    
    ans = input("Enter your choice [1-4]: ")
    if ans=="1":
        print(rightRightTriangle(5))
    elif ans=="2":
      print(triangle(5))
    elif ans=="3":
        print(semicircle(3))
     
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
