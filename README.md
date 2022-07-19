# hello-world
def rotate(input,n):
    return input[n:]+ input[:n]
myarray=[1,3,4,5,7,9,8 ]
rotate_array=int(input("enter a number:"))    
print(rotate(myarray,rotate_array))
'''
'''

def rotate(input,n):
    return input[n:]+input[:n]
myarr=[1,2,3,4,5,6,7,8,9]
rotate_arr=int(input("enter a number:"))
for i in range(0,rotate_arr):
    last =myarr[len(myarr)-1]
    for j in range(len(myarr)-1, -1, -1):
        myarr[j]=myarr[j-1]
    myarr[0]=last
for i in range(0,len(myarr)):
    print(myarr[i])
          

