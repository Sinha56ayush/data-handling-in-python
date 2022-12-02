
list1 = []
N = int(input("No. of numbers to find mean:"))

for i in range(0,N):
  a = int(input())
  list1.append(a)
  i+=1
  
  
mean = sum(list1)/len(list)
print("mean of",N,"numbers is",mean)
 

