'''
def get_file_name():

    file_name = ""

    file_name = "input.txt"

    return file_name


def get_file_contents(file_name):

    fh = open(file_name)

    lines = fh.readlines()

    return lines

def main():


    file_name = get_file_name()

    lines = get_file_contents(file_name)

    count = 0
    for line in lines:
        print(line)
        count = count + (line).count("and")
    print(count)


    pass

main()
'''
'''
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
          
'''

name=input("enter a number:")
print('hello',name)

class student:
    mark=[]
    def getdata(self, rollno, name, m1, m2, m3):
        student.rollno = rollno
        student.name = name
        student.mark.append(m1)
        student.mark.append(m2)
        student.mark.append(m3)

    def displaydata(self):
        print("rollno is :",student.rollno)
        print("name is :",student.name)
        print("marks are:",student.mark)
        print("total mark are:",self.total())
        print("average make:",self.average())

    def total(self):
        return (student.mark[0] + student.mark[1] +student.mark[2])
    def average(self):
        return ((student.mark[0] + student.mark[1] + student.mark[2]/3))

rollno= int  (input("enter the rollno:"))
name = input("enter the name:")
m1= int  (input("enter the mark 1 :"))
m2= int  (input("enter the mark 2 :"))
m3= int  (input("enter the mark 3 :"))

s1=student()
s1.getdata(rollno,name, m1,m2,m3)
s1.displaydata()
