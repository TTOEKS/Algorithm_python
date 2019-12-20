def bubbleSort(a):
    for last in range(len(a)-1, 0, -1):
        for i in range(0, last):
            if(a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
    return a
if __name__ == '__main__':
    array = [3,5,7,1,2,3,88,9,5,4]
    print(bubbleSort(array))
