def countingSort(listt):

    lenn = len(listt)
    cikti = [0] * lenn

    say = [0] * 10

    for _ in range(0, lenn):
        say[listt[_]] += 1

    for _ in range(1, 10):
        say[_] += say[_ - 1]

    _ = lenn - 1
    while _ >= 0:
        cikti[say[listt[_]] - 1] = listt[_]
        say[listt[_]] -= 1

        _ -= 1

    for _ in range(0, lenn):
        listt[_] = cikti[_]

    return listt


dizi = [5, 6, 8, 1, 5, 5, 7]
dizi = countingSort(dizi)

print(dizi)
