def warehouse_process(totals, transaction):
    good=transaction[1]
    if transaction[0]=='receive':
        totals[good]=totals.get(good, 0)+transaction[2]
    elif transaction[0]=='ship':
        totals[good]+=-transaction[2]

        
