def average(ls):
    return sum(ls)/len(ls)
def prop_above(ls):
    i = 0
    for items in last_list:
        if items > average(ls):
            i+=1
    return (i/len(ls))*100
def median(ls):
    middle = int(len(ls)/2)
    return ls[middle]
 
    
               

new_list =[]
last_list=[]
fhand = open("StudentExercise.csv")
next(fhand)
for line in fhand:
    words = line.split(',')
    The_list = list(words)
    if The_list[0]:
        new_list.append(The_list[0])
#print(new_list)
for numbers in new_list:
    last_list.append(float(numbers))


sorting = last_list.sort()
#print(last_list)
print("The Average is",int(average(last_list)))
print("The proprotions above are",int(prop_above(last_list)),"%")
print("The median is",median(last_list))
#for numbers in last_list:
  # the_average = average(numbers)
#print("The average is",the_average)
    


    
    
