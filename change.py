def SelectionSort(A):
    for i in range(0, len(A) - 1):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

        if i % (len(A)//10) == 0:
            print(f'ready {i//(len(A)//100)}%')
    print(f'ready 100%')
    return A