# # import math
# # string = str(input)
# # print(string)
# # words = string.split()
# # print(words)
# # average = sum(len(w))

# import math
# no_of_colors = int(input())
# total = 0.0
# cost_color = no_of_colors*5.00
# cost_brush = 40.00
# total = cost_color + cost_brush
# tax = total * 0.1
# final_cost = total + tax
# print(round(final_cost))

import math 
string=input() 
c=0  
words=len(string.split())
for i in string: 
    if i!= '?':
        if(i!=" "): 
            c=c+1 
average =c/words
print(math.ceil(average))