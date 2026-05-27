def MergeSort(app):
    if len(app) > 1:
        n = len(app)//2
        L = app[:n]
        R = app[n:]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                app[k] = L[i]
                i += 1
                k += 1
            else:
                app[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            app[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            app[k] = R[j]
            j += 1
            k += 1

    return app


if __name__ == '__main__':

    n = int(input())

    app = list(map(int, input().split()))

    print(*MergeSort(app))


