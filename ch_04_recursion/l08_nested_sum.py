def sum_nested_list(lst):
    total = 0
    for i in lst:
        if i == None:
            return 0
        if type(i) == int:
            total += i
            print("i == int",total)
        if type(i) == list:
            total += sum_nested_list(i)
            print("i == list",total)
    return total

def sum_nested_list2(lst):
    if not lst:
        return 0
    if type(lst) == int:
        print(lst)
        return lst
    return sum_nested_list2(lst[0]) + sum_nested_list2(lst[1:])
