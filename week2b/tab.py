def lend_money(debts, person, amount):
    if person in debts:
        debts[person].append(amount)
    else:
        debts[person]=[amount]
    return None

def amount_owed_by(debts,person):
    amnt=0
    for i in debts.get(person, []):
        amnt+=i
    return amnt

def total_amount_owed(debts):
    tot=0
    for i in debts:
        tot+=amount_owed_by(debts,i)
    return tot
