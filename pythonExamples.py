#In this challenge, we need to find the indices 
#in two equally sized lists where the numbers match. 
#We will be iterating through both of them at the same time 
#and comparing the values, if the numbers are equal, then we record the index. 
#These are the steps we need to accomplish this:
#Write your function here
def same_values(lst1, lst2):
  match = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      match.append(index)
  return match

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))