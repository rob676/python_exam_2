
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getNumber():

    user_input = input('number of automobile')

    if (re.match(r"\w{2}\-\d{4}", user_input) ):
        return user_input
    else:
        return getNumber()


"""
    Написати валідатор ....
    Правило валідації
"""

def getCompetitionName():
    #перевіряємо чи складається з літер чи існує 1 пробіл
    name_compet=input()
    iterator=0
    if name_compet.isalpha()==True :
        for i in name_compet:
            if i == ' ':
                iterartor+=1
        if iterator>1:
            return getCompetitionName()
    return name_compet




"""
    Написати валідатор ....
    Правило валідації
"""


def getMark():
    #записуєм числа і перевіряємо їх
    mark=input()
    list_mark=[]
    if mark.isnum()==True:
        mark=int(mark)
        list_mark.append(mark)
        return list_mark
    else:
        return getMark()