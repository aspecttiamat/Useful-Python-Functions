def change(pay, cost):
    cur = [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]
    chg = []
    amt = pay - cost

    for bill in cur:
        while amt >= bill:
            chg.append(bill)
            amt -= bill
    return chg, len(chg)
