
# list1 = []
# N = int(input("No. of numbers to find mean:"))

# for i in range(0,N):
#   a = int(input())
#   list1.append(a)
#   i+=1
  
  
# mean = sum(list1)/len(list)
# print("mean of",N,"numbers is",mean)

list1 = []
N = int(input("No. of numbers to find median: "))



for i in range(0,N):
    a = int(input())
    list1.append(a)
    i += 1

list1.sort()


if len(list1)%2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2-1]
    median = (m1 + m2)/2

else:
    median = list1[len(list1)//2]

print("Median:",median)