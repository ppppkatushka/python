# TODO решите задачу
import json




def task() -> float:
    summa =0
    with open("input.json","r",encoding = "utf-8") as file:
        a = json.load(file)
    for ddd in a:
        summa = summa +(ddd.get("score", 0)*ddd.get("weight", 0))
    return round(summa,3)



print(task())
