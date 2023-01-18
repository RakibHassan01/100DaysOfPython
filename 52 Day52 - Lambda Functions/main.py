# def double (x):
#     return x * 2

def apply(fx, value):
    return fx(value)

double = lambda x : x *2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3


print(double(5))    
print(cube(5))    
print(avg(5,5,8))  
print(apply(cube, 5))  
print(apply(lambda x: x*x*x, 5))  