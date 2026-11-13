import numpy as np
#global variables 
arr = None
rear = -1 
front = 0

#Create 
def create(size):
    global rear, arr
    if rear == (size - 1):
        print("Queue is full!")
    else:
        arr = np.zeros(size, dtype=int)
        i = 0
        if rear == -1: 
            rear = rear + 1
        while i < size: 
            ans = int(input("\nEnter Data => "))
            arr[i] = ans
            i= i+1
            rear= rear+1



#Sort 

def sort(size):
    global arr
    i = 0 
    j = i+1
    while (i<size):
        min = i 
        while (j <size):
            if (arr[j]< arr[min]):
                min = j
            j= j+1
        swap = arr[i]
        arr[i] = arr[min]
        arr[min] = swap 

        i= i+1
    print("Sorted array:", arr)

#Progression check
def P_Check(size):

    j = 0
    r = arr[j+1]/arr[j]
    d = arr[j+1]-arr[j]
    i = 0
    while(i < size-1):
        if (arr[i+1]-arr[i])== d:
            progression = 'A'
        elif (arr[i+1]/arr[i]) == r:
            #added edge case to check divide by zero 
            try: 
                arr[i] = 0
            except:
                progression == 'N'

            progression = 'G'
        else:
            progression = 'N'
        i= i+1
    if (arr[1]-arr[0])== 0:
        progression = 'N'

    if (arr[1]/arr[0]) == 1:
        progression = 'N'

    if size < 2:
            progression = 'N'

    return progression

#Arithemtic 
def AP(n):
    a = arr[0]
    d = arr[1]-arr[0]
    a_n = a + (d*(n-1))
    print("the ",n ,"th term is,", a_n)

#Geometric 
def GP(n):
    a = arr[0]
    r= arr[1]/arr[0]
    u_n = a*(r**(n-1))
    print("the ",n ,"th term is,", u_n)



#Main 
def main():
    print("Chiyo MODEL 1.0")
    print("")
    size = int(input("Enter an array size => "))

    create(size)

    choice_1 = int (input("Do you want to sort data(1) or predict(2) "))

    if choice_1 == 1: 
        sort(size)
    elif choice_1 == 2:
        n = int(input( "Enter a nth term=> "))
        s = P_Check(size)

        if s == 'A':
            AP(n)
        elif s == 'G':
            GP(n)

        elif s == 'N': 
            print(" Data set is either too small, an Undefined occured or too random to make a prediction please change data set")

        else: 
            print("Invalid")

    else :
        print("Inavlid enter 1 or 2")



if __name__ == '__main__':
    main()