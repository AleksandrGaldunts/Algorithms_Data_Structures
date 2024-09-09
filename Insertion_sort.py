# ls = [9,7,2,9,3,4,8,1,2]
#
# for i in range(1,len(ls)):
#     for j in range(0,i):
#         if ls[j]>ls[i]:
#             ls[i],ls[j] = ls[j],ls[i]
#
# print(ls)

ls = [9,7,2,9,3,4,8,1,2]

for i in range(1,len(ls)):

    key = ls[i]
    j = i-1

    while j>=0 and key<ls[j]:
        ls[j+1],ls[j] = ls[j],ls[j+1]
        j-=1
print(ls)







