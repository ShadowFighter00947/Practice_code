def circle_area(r):
    a = 3.14 * r * r
    return(a)

def circle_perimeter(r):
    p = 2 * 3.14 * r
    return(p)

def rect_area(l, w):
    a = l * w
    return(a)

def rect_perimeter(l, w):
    p = 2 * (l + w)
    return(p)


shape = input('Enter shape ').lower()
find = input('Area or  Perimeter ').lower()

if shape == 'circle' and find == 'area':
    r = int(input('Enter radius '))
    area = round(circle_area(r))
    print(f'\n Area of circle is: {area}')
elif shape == 'circle' and find == 'perimeter':
    r = int(input('Enter radius '))
    perimeter = round(circle_perimeter(r))
    print(f'\n perimeter of circle is: {perimeter}')
elif shape == 'rectangle' and find == 'area':
    l = int(input('Enter length of rectangle '))
    w = int(input('Enter width of rectangle '))
    area =  round(rect_area(l, w))
    print(f'\n Area of rectangle is: {area}')
elif shape == 'rectangle' and find == 'perimeter':
    l = int(input('Enter length of rectangle '))
    w = int(input('Enter weidth of rectangle '))
    perimeter = round(rect_perimeter(l, w))
    print(f'\n Perimeter of rectangle is: {perimeter}')
elif shape == 'exit'.lower():
    print('Stop execution')