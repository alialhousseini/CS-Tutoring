
def check_triplet(lst,sum):
    for i in range(0, len(lst)-2):

    # Fix the second element as A[j]
        for j in range(i + 1, len(lst) - 1):

        # Now look for the third number
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] + lst[k] == sum:
                    print("Triplet is", lst[i],
                        ", ", lst[j], ", ", lst[k])
                    return True

# If we reach here, then no
# triplet was found
    return False

# Driver program to test above function
lst1=[12,3,4,1,6,9]
sum1=24
lst2=[1,2,3,4,5]
sum2=9
check_triplet(lst1,sum1)
check_triplet(lst2,sum2)