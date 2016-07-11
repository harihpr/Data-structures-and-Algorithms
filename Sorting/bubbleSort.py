import timeit

def bubbleSort():
    arr = [8,20,20,5,68,3,48,6,98,25,10,13,21,20,55,6,2,3,2,2,5,73,4,15,4,5,7,10,15,7,10,40,6,5,5,5,98,15,2,7,16,42,80,54,2,26,8,5,35,7,4,60,5,30,58,20,135,10,4,40,5,50,10,47,6,22,1,32,5,25,45,5,6,18,2,6,40,15,11,10,20,48,1,52,19,4,44,6,6,2,57,83,5,6,5,14,7,10,10,6,10,10,20,1,100,1,54,16,16,62,15,70,8,5,56,72,2,105,10,24,4,6,15,107,50,4,10,20,5,0,146,25,30,10,19,14,66,10,10,45,22,90,70,32,2,32,4,4,0,5,96,6,38,50,10,4,11,2,12,2,60,5,10,40,2,5,34,5,36,8,25,14,2,26,4,10,35,20,10,3,35,25,15,10,35,6,41,19,38,4,65,6,30,145,5,6,18,3,5,1,5,10,145,12,5,2,134,3,2,20,6,4,8,15,22,20,5,4,19,4,50,48,4,2,8,70,45,5,5,1,5,4,10,5,18,28,22,12,40,14,80,2,5,66,2,2,45,88,5,6,95,125,110,97,7,28,3,2,2,5,48,4,5,62,20,4,19,88,3,6,56,82,55,58,5,6,40,15,2,2,6,5,8,6,10,5,32,22,5,4,2,2,2,5,30,15,5,4,20,7,5,15,30,40,10,5,6,3,10,10,30,4,12,40,20,7,60,10,2,8,5,8,95,21,3,8,10,2,29,10,30,86,2,2,5,40,4,6,90,86,5,78,47,2,72,5,25,3,26,25,36,78,42,4,85,10,2,2,5,19,10,33,7,2,52,5,6,32,5,50,20,5,21,4,11,25,50,0,2,24,10,5,5,32,10,1,40,53,6,2,22,10,44,5,4,8,32,4,6,34,8,38,16,42,5,136,5,4,2,112,22,7,5,10,51,50,10,34,20,4,24,7,2,10,20,14,15,35,5,8,12,142,0,25,38,7,67,4,37,10,133,4,25,50,15,8,16,55,150,1,5,5,90,7,3,25,8,5,100,70,114,102,70,10,5,64,126,22,25,26,24,35,5,4,76,70,7,58,28,1,10,40,10,3,4,1,10,5,5,116,6,32,75,10,20,148,10,20,7,4,16,10,6,6,42,1,40,56,35,4,25,2,5,10,37,5,5,5,24,40,4,1,85,6,4,15,5,5,6,8,26,5,80,20,6,8,15,76,5,90,14,5,19,46,20,8,12,15,10,2,2,30,0,15,25,16,55,26,60,6,5,0,8,31,5,2,5,24,5,6,3,5,4,2,80,4,1,10,62,10,2,15,5,16,5,82,10,6,15,15,78,30,35,80,32,5,10,15,10,8,8,4,50,8,3,39,14,10,46,5,2,5,10,30,7,36,4,10,44,3,39,6,20,5,95,27,30,10,14,10,45,8,24,16,60,10,105,5,10,10,10,6,2,109,12,20,41,1,38,2,86,20,4,7,56,20,40,35,6,18,25,5,9,5,25,4,6,2,2,15,3,2,2,5,45,82,2,30,5,5,15,10,30,32,38,10,2,4,23,20,5,69,4,40,31,5,5,12,30,1,5,3,2,20,24,22,10,4,15,20,20,22,6,7,10,16,8,2,86,5,84,31,25,91,10,2,40,23,18,34,20,6,95,19,94,33,5,2,5,100,46,14,30,30,51,35,50,6,26,5,17,6,5,77,53,66,2,30,4,25,27,56,6,70,3,18,170,30,5,6,14,135,50,24,22,4,5,10,2,40,4,16,5,19,7,6,10,30,3,4,20,10,35,10,14,33,100,45,20,10,6,2,30,98,5,6,6,32,5,50,10,5,22,2,10,5,54,10,8,19,20,28,5,38,25,5,18,10,24,5,2,41,16,23,5,30,34,18,15,1,35,155,8,25,16,20,93,40,10,6,10,2,5,14,34,2,40,6,48,10,2,10,55,30,16,28,56,125,6,8,30,32,6,36,2,65,78,10,3,5,13,6,38,5,10,65,75,3,5,21,8,2,3,16,15,10,2,5,7,5,38,8,6,13,30,8,4,38,45,4,25,25,5,60,40,25,8,34,5,10,22,30,42,5,2,60,13,5,12,3,35,44,15,22,5,4,41,22,49,2,24,54,5,12,4,1,58,10,5,4,2,6,64,38,56,32,66,42,50,35,30,5,12,87,1,5,37,10,15,7,44,9,35,20,5,40,10,38,5,34,12,8,1,75,52,4,2,25,86,9,51,1,27,15,2,10,6,83,30,10,5,45,5,20,14,35,35,25,46,15,30,65,26,40,5,6,6,25,18,20,22,30,5,30,40,25,95,18,9,15,24,31,10,79,101]
    #print "Unsorted array: ", arr
    noOfElem = len(arr)
    sort = False;
    while not sort:
        sort = True;
        for index in range(0,noOfElem-1):
            if arr[index] > arr[index+1]:
                temp = arr[index+1]
                arr[index+1] = arr[index]
                arr[index] = temp
                sort = False;
    
    print "Sorted array: ", arr

def main():
    t = timeit.timeit(bubbleSort,number=1)
    print "Time taken to sort the array: %0.8ls s" %t

main()