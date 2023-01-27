# def top_left_triangle(n):
#     output_lines = []
#     for i in range(n):
#         line = '*'*(n-i)
#         output_lines.append(line)
#     return output_lines

# def bottom_right_triangle(n):
#     output_lines = []
#     for i in range(n):
#         line = ' '*(n-i-1) + '*'*(i+1)
#         output_lines.append(line)
#     return output_lines


def top_left_triangle(n):
    triangle_list = []
    for i in range(n, 0, -1):
        triangle_list.append(i * "*")

    return triangle_list


# def bottom_right_triangle(n):
#     triangle_list = []
#     for i in range(n):
#         line = " " * (n-i-1)
#         line += (i+1) * "*"
#         triangle_list.append(line)

#     return triangle_list


def bottom_right_triangle(n):
    triangle_list = []
    for i in range(1, n+1):
        line = " " * (n - i)
        line += i * "*"
        triangle_list.append(line)

    return triangle_list

tri_list = bottom_right_triangle(5)
[print(line) for line in tri_list]