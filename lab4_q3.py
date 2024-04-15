A=[7,5,1,4]
B=[6,17,9,3]

def product_sum(A,B):
    A.sort()
    B.sort(reverse=True)
    n=len(A)
    result=sum(A[i]*B[i] for i in range(n))
    return result

minimized_sum = product_sum(A,B)
print("Minimum sum of products:", minimized_sum)