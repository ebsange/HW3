in_file = "test_grids/medium_grid.txt"
myfile = open(in_file)

for line_of_text in myfile:
    num_list = line_of_text.split(",")
    int_list = []
    for i in num_list:
        int_list.append(int(i))
    print(int_list)
myfile.close()