ls = [4,2,9,1,7,8,5,3,6,1,0]

def selection_sort(list):
    for j in range(0,len(ls)):
        maxIndex = 0
        for i in range(1,len(ls)-j):
            if ls[maxIndex] < ls[i]:
                maxIndex = i
        ls[maxIndex],ls[len(ls)-1-j] = ls[len(ls)-1-j],ls[maxIndex]

selection_sort(ls)
print(ls)