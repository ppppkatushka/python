money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
m = money_capital+salary - spend
i=0
while (m>0):
    i+=1
    spend = spend*(1+increase)
    m = m-spend+salary


print("Количество месяцев, которое можно протянуть без долгов:", i)
