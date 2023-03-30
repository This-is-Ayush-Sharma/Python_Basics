def update_mark_list(mark_list, new_element, pos):
    mark_list.insert(new_element, pos)
    return mark_list


if __name__ == '__main__':
    ar = [89, 78, 99, 76,77,67,99,98,90]
    ar = update_mark_list(ar, 78, 8)
    print(ar[5],ar[7])