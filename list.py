#The input is a list of unsorted numbers in the range of -10000 to 10000. This program finds the smallest positive missing number in this list
#For example if the given list is [-100,-2,-1,0,1,200]. The output should be 2
#If the given list [-20,-10,-1,0]. The output should be 1
mylist=[]
size=int(input("Enter List Size\n"))
for i in range(size):
    a=(input("Enter \t"))
    mylist.append(int(a))
print(mylist)
# Shorter Version
for i in range(10000):
    if i not in mylist and i!=0:
        print(i)
        break
# Long Version
missing=0 #Buffer for storing the minimum Value
mylist.sort() # Sorting the list to make it easier for us 
print("Sorted List is"+str(mylist))
if 1 in mylist: #if the list contains 1 
    for i in range(len(mylist)):
        if mylist[i]>0 and i!=size-1: # only iterate for 
            print(str(i)+" Iteration")
            if mylist[i+1]-mylist[i]==1 or mylist[i+1]-mylist[i]==0:
                missing=mylist[i]+1
                print("Missing is :"+str(missing)+"\tin "+str(i)+"th iteration")
            else:
                missing=mylist[i]+1
                break
else: #Print 1 if List doesn't contains 1 as it is the smallest positive number
    print("Smallest Positive Number Missing is: 1")
if missing>10000: #If list contains 1...10000 then no number is missing
    print("No number missing")
elif missing!=0: #Print missing value only if its not 0
    print("The missing Smallest Positive Number is:"+str(missing))