def dao_nguoc_list(lst):
    return lst[:: -1]

input_list = input("Nhập sanh sách các số, cách nhau bằng đấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược: ", list_dao_nguoc)