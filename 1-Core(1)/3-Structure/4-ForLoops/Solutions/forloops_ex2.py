
def display_shopping_lists(shopping_lists):
    margin = 3
    length_of_longest_list = 0
    width_of_longest_item = 0

    for shopping_list in shopping_lists:
        if len(shopping_list)>length_of_longest_list:
            length_of_longest_list = len(shopping_list)

        for item in shopping_list:
            if len(item)>width_of_longest_item:
                width_of_longest_item = len(item)
    list_width = width_of_longest_item + margin

    output_lines = []
    for i in range(length_of_longest_list):
        line = ''
        for shopping_list in shopping_lists:
            if i<len(shopping_list):
                item = shopping_list[i]
            else:
                item = '' 
            line += f'{item:<{list_width}}'
        output_lines.append(line)
    return output_lines


