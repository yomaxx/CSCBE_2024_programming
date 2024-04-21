puzzle = '''
+----+----+----+----+
| 11 |  5 | 15 |  4 |
+----+----+----+----+
|  3 | 12 |  6 |  1 |
+----+----+----+----+
| 14 |  7 | 10 | 13 |
+----+----+----+----+
|  8 |  9 |  2 | 16 |
+----+----+----+----+

'''

# puzzle coordinates
# +----+----+----+
# |  00 |  10 |  20 |
# +----+----+----+
# |  01 |  11 |  21 |
# +----+----+----+
# |  02 |  12 |  22 |
# +----+----+----+



# swap element with buffer
def swap_elements(buffer, y, x, array):
    extra = array[x][y]
    array[x][y] = buffer
    buffer = extra
    return buffer, array


# find element
def find_position(element, array):
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] == element:
                return y,x


# find final position of the element
def determine_final_position(element, array):
    n = len(array)
    x = (element-1) % n
    y = (element-1) // n
    return x, y


# find the path
def find_path(startx, starty, endx, endy):
    path = []
    if startx < endx:
        for i in range(startx, endx):
            path.append('r')
    else:
        for i in range(startx, endx, -1):
            path.append('l')
    if starty < endy:
        for i in range(starty, endy):
            path.append('d')
    else:
        for i in range(starty, endy, -1):
            path.append('u')
    return ''.join(path)
    

if __name__ == "__main__":
    # create array from puzzle
    rows = [row for row in puzzle.strip().split('\n') if row.startswith('|')]
    array = [[int(num) for num in row.split('|')[1:-1]] for row in rows]
    print(array)
    
    #start setup
    buffer = "0"
    path = []
    currentx, currenty = 0, 0
    
    for element in range(1, len(array)*len(array)+1):
        if element != buffer:
            x, y = find_position(element, array)
        fx, fy = determine_final_position(element, array)

        print(f"Element {element} is at position {x}, {y}")
        print(f"Element {element} should be at position {fx}, {fy}")
        #print(array)

        if x == fx and y == fy:
            continue
        if element != buffer:
        # move cursor to element
            path.append(find_path(currentx, currenty, x, y))
            currentx, currenty = x, y
            # take element to buffer
            buffer, array = swap_elements(buffer, currentx, currenty, array)
            path.append('b')

        print('cursor:', currentx, currenty)

        # move cursor to final position
        path.append(find_path(currentx, currenty, fx, fy))
        currentx, currenty = fx, fy
        # set element in final position
        buffer, array = swap_elements(buffer, currentx, currenty, array)
        path.append('b')

        print('cursor:', currentx, currenty)
        print()
        if element == 13:
            print(array)


    print(array)
    final_path = ''.join(path)
    print(final_path)
    print(buffer)