import matplotlib.pyplot as plt
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
    middle_1 = middle +1 
    return (ls[middle]+ls[middle_1])/2

def make_hist(data,n_bins):
    plt.hist(data,bins = n_bins)
    plt.title("Hours of Exercise")
    plt.ylabel("Counts")
    plt.show()             
new_list =[]
last_list=[]
fhand = open("StudentExercise.csv")
next(fhand)
for line in fhand:
    words = line.split(',')
    The_list = list(words)
    if The_list[0]:
        new_list.append(The_list[0])
for numbers in new_list:
    last_list.append(float(numbers))
sorting = last_list.sort()
print("The Average is",int(average(last_list)))
print("The proprotions above the average are at ",int(prop_above(last_list)),"%")
print("The median is",median(last_list))
make_hist(last_list,15)

    


    
    
