# This function was made to calculate change due, and return the greedy amount of bills needed.

def change(amt):
    cur = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    chg = []
    a = amt

    for bill in cur:
        while a >= bill:
            chg.append(bill)
            a -= bill
    return chg, len(chg)


# Proof of concept, doing the same thing, just recursively. 

chg = []


def recur_change(amt, x):
    cur = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    r = 0

    if amt == 0:
        return chg
    else:
        if amt - cur[x] >= 0:
            amt -= cur[x]
        elif amt - cur[x] < 0:
            r += 1
            chg.append(cur[x])

        return recur_change(amt, x+r)
