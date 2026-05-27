def Choice(app, n):
    if len(app) == 0:
        return []

    for i in range(n):
        min_i = i
        for j in range(i, n):
            if app[j] < app[min_i]: min_i = j;

        app[min_i], app[i] = app[i], app[min_i]

    return app


if __name__ == '__main__':

    n = int(input())

    app = list(map(int, input().split()))

    print( *Choice(app, n) )