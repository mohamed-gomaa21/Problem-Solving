
def remove_repeat(repeat_item , my_list) :
    """"

        this function to remove all selected items if they repeated
        11/08/2022

    """

    while repeat_item in my_list :
        my_list.remove(repeat_item)

    return my_list


mylist = [20,30,5,110,12,20,30,20]
item = 30

remove_repeat(item,mylist)
print(mylist)
print(remove_repeat.__doc__)
