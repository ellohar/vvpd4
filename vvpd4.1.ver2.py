# some comments
import numpy as np
import sys


def integral_view(image):
    height, width = image.shape
    integral = np.zeros((height, width), dtype=np.int32)

    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                integral[y, x] = image[y, x]
            elif x == 0:
                integral[y, x] = integral[y-1, x] + image[y, x]
            elif y == 0:
                integral[y, x] = integral[y, x-1] + image[y, x]
            else:
                integral[y, x] = integral[y-1, x] + integral[y, x-1] - integral[y-1, x-1] + image[y, x]

    return integral


def generate_integer_matrix(rows, columns):
    return np.random.randint(0, 256, size=(rows, columns), dtype=np.int32)


def rect_sum(integral_image, x1, y1, x2, y2):

    sum_a = integral_image[y1-1, x1-1]
    print(sum_a)
    sum_b = integral_image[y1-1, x2]
    print(sum_b)
    sum_c = integral_image[y2, x2]
    print(sum_c)
    sum_d = integral_image[y2, x1-1]
    print(sum_d)
    print()

    sum_of_rect = sum_a + sum_c - sum_b - sum_d

    return sum_of_rect


rect = generate_integer_matrix(5, 6)
print(rect)
print()
print(rect[2-1, 2-1], rect[4-1, 4-1])
print()
print(integral_view(rect))
print()
print(rect_sum(integral_view(rect), x1=2-1, y1=2-1, x2=4-1, y2=4-1))


def main():
    while True:
        menu = '----------------------------------------------------------------\n' \
               'enter what do you want to do:\n' \
               '(1) - to see integral image;\n' \
               '(2) - to calculate sum of pixels in rectangle;\n' \
               '(3) - to see both integral image and sum of pixels in rectangle;\n' \
               '(4) - to exit\n' \
               '----------------------------------------------------------------'
        print(menu)
        request = input()
        if request == '1':
            rows, columns = input('enter the amount of rows and columns separate by space\n').split()
            img = generate_integer_matrix(int(rows), int(columns))
            print(img)
            print()
            print(integral_view(img))

        elif request == '4':
            sys.exit()

        else:
            print('input data is incorrect. carefully read possible operations')


if __name__ == '__main__':
    main()
