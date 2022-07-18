def f1(a,b):
  if a>b:
    return b
  else:
    return a
  
def f2(a,b,c):
  x = f1(b,c)   
  y = x+f1(c,a) 
  return x+y    

x,y,z = map(int,input().split())
print(f2(x,y,z))

"""
Entrada 1: 10, 20, 15
Entrada 2: 20, 10, 30
Entrada 3: 3, 2, 1

Saída 1: 40
Saída 2: 40
Saída 3: 3

"""
