#---------1-------
number = 994
result = bin(number)
print(result)

#---------2-------
binary_number = '1011'
decimal_number = int(binary_number, 2)
print(decimal_number) 


#---------3-------
binary_number = '1011'
decimal_number = int(binary_number, 8)
print(decimal_number)


#---------4------- (НЕ ПОЛУЧИЛОСЬ)
binary_number = '1011'
decimal_number = int(binary_number, 4)
print(decimal_number)


#---------5-------
num1 = int('111101', 2)
num2 = int('11', 2) 

n_1 = num1
n_2 = num2
result = num1 * num2
result_dvoich = bin(num1 * num2)[2:]

print(result_dvoich)


#---------6-------
binary_number = '11100101'
decimal_number = int(binary_number, 2)
print(decimal_number) 


#---------7-------
def binar(x, n): 
    ans="" 
    while x>0:
        ans+=str(x%2)
        x//=2
    ans="0"*(n-len(ans))+(ans[::-1])
    return ans 
A=int(input()) 
n=int(input()) 
print(binar(A, n))


#---------8-------
x = 121
print(~x)

#---------9-------
import struct

bits = b"C1330000"  
decimal_number = struct.unpack('!f', bits)[0]

print(decimal_number) 
#---------10-------
import struct 

num = -179.578125
byte_num = struct.pack('!f', num)
hex_num=byte_num.hex()

print(hex_num)