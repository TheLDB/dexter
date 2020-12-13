# This first part is just gonna be me expirementing with how fibonacci works and shi

def search(lys, val):
    fibM_2 = 0
    # thats the numbers thats 2 gens behind the current fib number
    fibM_1 = 1
    # 1 gen behind current
    fibM = fibM_1 + fibM_2
    # current
    while(fibM < len(lys)):
        # Makes it so if the number is less than it it just keeps on generating
        fibM_2 = fibM_1
        fibM_1 = fibM
        fibM = fibM_1 + fibM_2
    index = -1
    while(fibM > 1):
        i = min(index + fibM_2, len(lys)-1)
        # min is iterable so it just keeps on going while its true
        if(lys[i] < val):
            # if the list current value is less than the value it just keeps going 
            fibM = fibM_1
            fibM_1 = fibM_2
            fibM_2 = fibM - fibM_1
            index = i
        elif(lys[i] > val):
            #if the current list value is more than the value it goes back 
            fibM = fibM_2
            fibM_1 = fibM_1 - fibM_2
            fibM_2 = fibM - fibM_1
        else:
            return i
    
    if(fibM_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1

print(search([1,2,3,4,5,6,7,8,9,10,11], 8))
