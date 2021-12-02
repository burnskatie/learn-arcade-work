def selection_sort(my_list):
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
            temp = my_list[min_pos]
            my_list[min_pos] = my_list[cur_pos]
            my_list[cur_pos] = temp


def insertion_sort(my_list):
    for key_pos in range(1, len(my_list)): # 100
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while(scan_pos >= 0) and (my_list[scan_pos] > key_value): # worst - 50, avg 25
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
insertion_sort(my_list)
print(my_list)

# Average
# n = 10, 10 * 2.5 = 25
# n = 100, 100 * 14 = 2,500
# n = 1,000, 1,000 * 250 = 250,000
# n * (n / 4) = n^2 / 4

# Selection
# n = 10, 10 * 5 = 50
# n = 100, 100 * 50 = 5,000
# n = 1,000, 1,000 * 500 = 500,000
# n * (n / 2) = n^2 / 2

# Insertion
# n = 10, 10 * 1 = 10
# n = 100, 100 * 1 = 100
# n = 1,000, 1,000 * 1 = 1,000

