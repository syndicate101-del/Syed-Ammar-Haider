readings=(3.3,3.1,3.4,2.9,3,6,3.0,3.2)

above_3_2=0
highest=readings[0]
lowest=readings[0]
total_sum=0
count=0

for value in readings:
    if value>3.2:
        above_3_2+=1
    if value >highest:
        highest=value
    if value<lowest:
        lowest=value
    total_sum+=value
    count+=1
    
average=total_sum/count
print(f"Readingd above 3.2 V: {above_3_2}")
print(f"Highest: {highest}V")
print(f"Lowest: {lowest}V")
print(f"the average is: {average}")
