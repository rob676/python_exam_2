from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct(dataset ,number, competition, mark):
    #TODO
    if number in dataset:
        if competition in dataset[number]  :
            dataset[number][competition] = mark

        else:
            dataset[number][competition].append(mark)

    else:
        dataset[number]=dict()
        dataset[number][competition]=mark









print("Task 1")

#Додати нового користувача та нову покупку
addUserProduct(dataset,'DD-5555','som a',[34])

#Додати існуючому користувачу нову покупку нового продукту
addUserProduct(dataset,'GI-8878','jui',[78])

#Додати існуючому користувачу нову покупку існуючого продукту
addUserProduct(dataset,'UU-7879','olo',[67])

print(dataset)


print("\n\n")