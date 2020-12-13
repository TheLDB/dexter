# This first part is just gonna be me expirementing with how fibonacci works and shi

def search(lys, val):
    fibM_2 = 0
    fibM_1 = 1
    fibM = fibM_1 + fibM_2
    while(fibM < len(lys)):
        fibM_2 = fibM_1
        fibM_1 = fibM
        fibM = fibM_1 + fibM_2
    index = -1
    while(fibM > 1):
        i = min(index + fibM_2, len(lys)-1)
        if(lys[i] < val):
            fibM = fibM_1
            fibM_1 = fibM_2
            fibM_2 = fibM - fibM_1
            index = i
        elif(lys[i] > val):
            fibM = fibM_2
            fibM_1 = fibM_1 - fibM_2
            fibM_2 = fibM - fibM_1
        else:
            return i
    
    if(fibM_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1

print(search([1,2,3,4,5,6,7,8,9,10,11], 17))
