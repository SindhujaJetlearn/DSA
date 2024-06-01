#function for fibonacci 
#Fibonacci - sum of two previous numbers
def fib(n):
    #Base case - stop condition
    if (n==0):
        return 0
    # Base Case
    if(n==1 or n==2):
        return 1
    #Recursive
    else:
       return (fib(n-1)+fib(n-2))
    
n=int(input("Enter a number : "))

print("Fibonacci series of {} is :".format(n),end=" ") 

for i in range(0,n):
    print(fib(i),end=" ") 
    




