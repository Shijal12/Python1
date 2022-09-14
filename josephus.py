def josephus_survivor(n,k):
    people = list(range(1,n+1)) #create a list of people from 1 to n ( pyhton list exclude the last number)
    i=0 #start from  the first person
    while len(people)>1: #loop through the list of people
        i=(i+k-1)%len(people) #calculate the next person to be removed and update the i
        people.pop(i) #remove the person (dont get confused with the index and number)
    return people[0] #return the last person

josephus_survivor(7,3)