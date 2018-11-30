from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getNumber
from validators.lib import getCompetitionName
from validators.lib import getMark


from task1 import addUserProduct


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію

def addUserProductValidator():
    #get names
    number = getNumber()

    competition_name = getCompetitionName()

    mark= getMark()


    addUserProduct(number,competition_name,mark)



print("Task 1")
addUserProductValidator()
print(dataset)


print("\n\n")