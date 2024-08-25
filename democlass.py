print("RSA Algorithm Numerical :")
print("Example :=")
p=5
q=11
e=27
print(f"Given values : p={p} ,q={q} ,e={e}")
print("Calculate mod of n :")
mod_n=p*q
print(mod_n)
print("Calculate Fie of n :")
fie_n=(p-1)*(q-1)
print(fie_n)
print("Assume value of K ,which return integer number for d.")
k=2
print(f"k={k}")
print("Calculate d :")
d=(1+(k*fie_n))/e
print("d :",d)
m=2
print(f"Assume message is m={m}")
c=m**e % mod_n
print("Enctypted Message is : ",c)
message=c**d % mod_n
print("Decrypted message is : ",message)