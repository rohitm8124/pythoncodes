a= int (input("Enter a "))
b= int (input("Enter b "))
c= int (input("Enter c "))
d = b*b - 4*a*c
if (d>=0):
 print("Real Roots are:", -b/(2*a) + (d**0.5)/(2*a), -b/(2*a) - (d**0.5)/(2*a))
else:
 print ("Complex Roots are:", -b/(2*a) - (d**0.5)/(2*a), -b/(2*a) - (d**0.5)/(2*a))
# print(-b/(2*a))