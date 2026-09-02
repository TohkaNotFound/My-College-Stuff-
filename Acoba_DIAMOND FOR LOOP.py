rows = 5

# Upper part of the diamond
for i in range(rows):
    spaces = ' ' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

# Lower part of the diamond
for i in range(rows - 2, -1, -1):
    spaces = ' ' * (rows - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)