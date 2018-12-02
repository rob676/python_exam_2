
from data import dataset
from task1 import addUserProduct

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByCompetitions(name,competitions, amount_of_marks = 0):
    #TODO
    if competitions == []:
        return amount_of_marks
    list_mark=list(dataset[name][competitions[0]])
    print(list_mark)
    for i in list_mark:
        amount_of_marks += i
    return recursionByCompetitions(name,competitions[1:], amount_of_marks)

def recursionByAutomobiles(names = list(dataset.keys()), result_dict = dict()):
    #TODO
    if names == []:
        return result_dict
    name = names[0]
    competition = list(dataset[name].keys())
    result=recursionByCompetitions(name, competition)

    result_dict[name] = result
    return recursionByAutomobiles(names[1:],result_dict)

print("Task 3")

result = recursionByAutomobiles()
print(result)

print("\n\n")



