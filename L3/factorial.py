# Factorial function 
def f(n): 
  
    # Stop condition 
    if (n == 0 or n == 1): 
        return 1; 
  
    # Recursive condition 
    else: 
        return n * f(n - 1); 
  
n = 5; 
print("factorial of",n,"is:",f(n)) 
      