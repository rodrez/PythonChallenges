def filter_list(l):
    filtered_list = [item for item in l if type(item) == int]
    # for item in l:
    #     if type(item) == int:
    #         filtered_list.append(item)
    print(filtered_list)

filter_list([1, 2, 'a', 'b'])
filter_list([1,'a','b',0,15])
filter_list([1,2,'aasf','1','123',123])
