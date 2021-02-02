#python 

#iterative method
def printnumbers(n):
   for i in range(0,n+1):
       print(i)
       
       
# recurisve method 
def printnumbersrec(n):
    if n==1:
      return 1
    else:
    printnumbersrec(n-1)
    
    
    
    
