ls = [4,9,2,8,61,49,77,21,34,66,6]
def bubble_sort(ls):

    for i in range(len(ls)):
        flag = False
        for j in range(1,len(ls)-i):
            if ls[j]<ls[j-1]:
                ls[j-1],ls[j] = ls[j],ls[j-1]
                flag = True


        if not flag:
            return ls


bubble_sort(ls)
print(ls)

