money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months_survived = 0
current_spend = spend

while money_capital >= 0:
    deficit = current_spend - salary
    if deficit > 0:
        money_capital -= deficit
    else:
        break
    if money_capital < 0:
        break
    current_spend *= (1 + increase)
    months_survived += 1

print("Количество месяцев, которое можно протянуть без долгов:", months_survived)
