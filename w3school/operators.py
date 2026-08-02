""" #Math
a = 5
b = 12

print(a + b) #17
print(a - b) #-7
print(a * b) #60
print(a / b) #0.41(6)
print(a % b) #5
print(a ** b) #244140625
print(a // b) #0 """

""" #Bitwise

# ^ & | ~ << >>

a = 8 # 1000
b = 5 # 0101

xor_op = a ^ b     # 1101
and_op = a & b     # 0000
or_op = a | b      # 1101
not_op = ~a        # 0111
lshift_op = a << b # 0001 0000 0000
rshift_op = a >> b # 0000 (1000) => 0


print(xor_op)
print(and_op)
print(or_op)
print(not_op)
print(lshift_op)
print(rshift_op) """


"""
#List
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR """

""" a = "5"
print(type(+a)) #TypeError """


""" a = -5
print(-a) #5
 """

""" a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6]
c = a

print(f"memory region:a={id(a)}\tb={id(b)}\tc={id(c)}")
print(a is b)
print(a is c)
print(b is c) """


""" a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5, 6] """

# print(a == b)
""" print(a[0] in b)
print(a[len(a) - 1] in b)
print(a[len(a) - 1] not in b) """

""" a = True
b = False
print(a and b)
print(a or b) """

""" a = 11
b = 99
print((a < 99 and a > 66) or not (a == 0)) """