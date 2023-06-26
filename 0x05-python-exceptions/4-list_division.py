#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """
     a function that divides element by element 2 lists.
    """
    div_list = list()
    for i in range(list_length):
        try:
            div_result = my_list_1[i] / my_list_2[i]
            div_list.append(div_result)
        except (TypeError, ValueError):
            print("wrong type")
            div_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)
        except IndexError:
            print("out of range")
            div_list.append(0)
        finally:
            continue
    return div_list
