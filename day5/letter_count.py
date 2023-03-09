name='umbrella'
count={}
for letter in name:
   if letter in count:
     count[letter]= count[letter] + 1  #remaining addition of a same element
   else:
      count[letter]= 1 #first addition 
print(count)

maxCount_so_far=0   #finding max count of most occuring letter
most_occuring=''

for letter in count:
   if count[letter] > maxCount_so_far:
      maxCount_so_far=count[letter]
      most_occuring=letter

print('most occuring letter is',most_occuring,'and its count is',maxCount_so_far)      