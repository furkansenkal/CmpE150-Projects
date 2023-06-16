
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

if operation == 1:
    newMin = int(input())
    newMax = int(input())

    img = read_ppm_file(filename)[0]
    # Called the function that convert the image to a 3d list
    oldMax = read_ppm_file(filename)[1]
    oldMin = 0
    # Sets the image's max and min colour values
    new_img = []
    for i in range(len(img)):
        img_row = []
        for j in range(len(img[i])):
            pixel_col = []
            for k in range(len(img[i][j])):
                oldVal = img[i][j][k]
                newVal = round(((oldVal-oldMin)/(oldMax-oldMin)*(newMax-newMin) + newMin), 4)
                pixel_col.append(newVal)
            img_row.append(pixel_col)
        new_img.append(img_row)
    img_printer(new_img)
    # iterates all the elements of the 3d list one by one,
    # applies the operation to all of them,
    # adds this value to the new list and creates a new 3d list

if operation == 2:

    img = read_ppm_file(filename)[0]
    # Called the function that convert the image to a 3d list
    FirstChannelSum = 0
    FirstChannelStandardSum = 0
    SecondChannelSum = 0
    SecondChannelStandardSum = 0
    ThirdChannelSum = 0
    ThirdChannelStandardSum = 0
    new_img = []
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if k == 0:
                    FirstChannelSum += img[i][j][k]
                if k == 1:
                    SecondChannelSum += img[i][j][k]
                if k == 2:
                    ThirdChannelSum += img[i][j][k]
    FirstChannelMean = FirstChannelSum/(len(img)*len(img))
    SecondChannelMean = SecondChannelSum/(len(img)*len(img))
    ThirdChannelMean = ThirdChannelSum/(len(img)*len(img))
    # It calculates the mean for each channel separately
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if k == 0:
                    FirstChannelStandardSum += (img[i][j][k]-FirstChannelMean)**2
                if k == 1:
                    SecondChannelStandardSum += (img[i][j][k]-SecondChannelMean)**2
                if k == 2:
                    ThirdChannelStandardSum += (img[i][j][k]-ThirdChannelMean)**2
    FirstChannelStandardDeviation = (FirstChannelStandardSum/(len(img)*len(img)))**(1/2) + 1e-6
    SecondChannelStandardDeviation = (SecondChannelStandardSum/(len(img)*len(img)))**(1/2) + 1e-6
    ThirdChannelStandardDeviation = (ThirdChannelStandardSum/(len(img)*len(img)))**(1/2) + 1e-6
    # It calculates the standard deviation for each channel separately
    for i in range(len(img)):
        img_row = []
        for j in range(len(img[i])):
            pixel_col = []
            for k in range(len(img[i][j])):
                if k == 0:
                    normalized = round((img[i][j][k]-FirstChannelMean) / FirstChannelStandardDeviation, 4)
                    pixel_col.append(normalized)
                if k == 1:
                    normalized = round((img[i][j][k]-SecondChannelMean) / SecondChannelStandardDeviation, 4)
                    pixel_col.append(normalized)
                if k == 2:
                    normalized = round((img[i][j][k]-ThirdChannelMean) / ThirdChannelStandardDeviation, 4)
                    pixel_col.append(normalized)
            img_row.append(pixel_col)
        new_img.append(img_row)
    img_printer(new_img)
    # iterates all the elements of the 3d list one by one,
    # calculates the normalized value for all of them,
    # appends this normalized value to the new list and creates a new 3d list

if operation == 3:

    img = read_ppm_file(filename)[0]
    # Called the function that convert the image to a 3d list
    PixelSum = 0
    new_img = []
    for i in range(len(img)):
        img_row = []
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                # iterates all the elements of the 3d list one by one,
                PixelSum += img[i][j][k]
            PixelAvg = int(PixelSum/3)
            # sums the rgb values of each pixel and takes average of them
            img_row.append([PixelAvg, PixelAvg, PixelAvg])
            PixelSum = 0
            # when this process is completed,
            # it appends this average to the list correctly(sets the pixel's rgb values to average)
            # resets PixelSum value and moves to the next pixel.
        new_img.append(img_row)
    img_printer(new_img)
    # Creates a 3d list of output image correctly and then prints it

if operation == 4:

    filtername = input()
    Stride = int(input())

    def read_filter_file(f):
        filterlst = []
        fp = open(f)
        for i in fp:
            filterlst.append(i.split())
        return filterlst
    # Converts filter file to a 2d list so that it can be used below.

    filterlst = read_filter_file(filtername)
    img = read_ppm_file(filename)[0]
    # Called the functions that convert the image to a 3d list and convert the filter to a 2d list.
    new_img = []
    var1 = len(filterlst)-1
    var2 = len(filterlst[0])-1
    # I used these variables to finish the for loop at the right position and not get a list index error
    for i in range(0, len(img) - var1, Stride):
        # Iterates over the list with respect to stride value, For example, if Stride==2 moving forward two by two.
        img_row = []
        for j in range(0, len(img[i]) - var2, Stride):
            # Iterates over the list with respect to stride value, For example, if Stride==2 moving forward two by two.
            sum1 = 0
            sum2 = 0
            sum3 = 0
            # When the point where the filter starts changes,
            # I set this variables to 0 so that so that the filter can be applied correctly to new numbers
            for x in range(len(filterlst)):
                for y in range(len(filterlst[x])):
                    for k in range(len(img[i][j])):
                        if k == 0:
                            sum1 += (float(filterlst[x][y])*img[i+x][j+y][k])
                        if k == 1:
                            sum2 += (float(filterlst[x][y])*img[i+x][j+y][k])
                        if k == 2:
                            sum3 += (float(filterlst[x][y])*img[i+x][j+y][k])
                        # it applies the filter to each channel of each pixel in the correct order

            if sum1 < 0:
                sum1 = 0
            if sum2 < 0:
                sum2 = 0
            if sum3 < 0:
                sum3 = 0
            if sum1 > 255:
                sum1 = 255
            if sum2 > 255:
                sum2 = 255
            if sum3 > 255:
                sum3 = 255
            # If the new value of any channel of any pixel exceeds the image maximum color value or becomes less than 0,
            # This block clips it correctly such that it is always between 0 and maximum color value.

            img_row.append([int(sum1), int(sum2), int(sum3)])
        new_img.append(img_row)
        # Appends new values to the lists in the right order and creating a new 3d list filtered image.
    img_printer(new_img)
    # Prints the filtered image.

if operation == 5:
    filtername = input()
    Stride = int(input())


    def read_filter_file(f):
        filterlst = []
        fp = open(f)
        for i in fp:
            filterlst.append(i.split())
        return filterlst
    # Converts filter file to a 2d list so that it can be used below.

    filterlst = read_filter_file(filtername)
    img = read_ppm_file(filename)[0]
    # Called the functions that convert the image to a 3d list and convert the filter to a 2d list.
    for x in range(0, (len(filterlst)//2)):
        img.insert(0, [])
        img.insert(len(img), [])
        for i in range(len(img)):
            img[0].insert(0, [0, 0, 0])
            img[-1].insert(0, [0, 0, 0])
            if 0 < i < len(img)-1:
                img[i].insert(0, [0, 0, 0])
                img[i].insert(len(img[1]), [0, 0, 0])
    # This part allows us to add a frame of black pixels to the image according to the size of the filter.
    # In other words, it pads zeros to the edges of the input image
    # so that the output image has the same dimensions as the input image.

    new_img = []
    var1 = len(filterlst) - 1
    var2 = len(filterlst[0]) - 1
    # I used these variables to finish the for loop at the right position and not get a list index error.
    for i in range(0, len(img) - var1, Stride):
        # Iterates over the list with respect to stride value, For example, if Stride==2 moving forward two by two.
        img_row = []
        for j in range(0, len(img[i]) - var2, Stride):
            # Iterates over the list with respect to stride value, For example, if Stride==2 moving forward two by two.
            sum1 = 0
            sum2 = 0
            sum3 = 0
            # When the point where the filter starts changes,
            # I set this variables to 0 so that so that the filter can be applied correctly to new numbers
            for x in range(len(filterlst)):
                for y in range(len(filterlst[x])):
                    for k in range(len(img[i][j])):
                        if k == 0:
                            sum1 += (float(filterlst[x][y]) * img[i + x][j + y][k])
                        if k == 1:
                            sum2 += (float(filterlst[x][y]) * img[i + x][j + y][k])
                        if k == 2:
                            sum3 += (float(filterlst[x][y]) * img[i + x][j + y][k])
                        # it applies the filter to each channel of each pixel in the correct order
            if sum1 < 0:
                sum1 = 0
            if sum2 < 0:
                sum2 = 0
            if sum3 < 0:
                sum3 = 0
            if sum1 > 255:
                sum1 = 255
            if sum2 > 255:
                sum2 = 255
            if sum3 > 255:
                sum3 = 255
            # If the new value of any channel of any pixel exceeds the image maximum color value or becomes less than 0,
            # This block clips it correctly such that it is always between 0 and maximum color value.

            img_row.append([int(sum1), int(sum2), int(sum3)])
        new_img.append(img_row)
        # Appends new values to the lists in the right order and creating a new 3d list filtered image.
    img_printer(new_img)
    # Prints the filtered image.

if operation == 6:

    rangeinp = int(input())

    def operation6_func(img, i, j, rangeinp, m=0, n=1, down=True, up=False, right=False):
        if j >= len(img[0]):
            return
        # Base condition

        sayac1 = 0
        sayac2 = 0
        sayac3 = 0
        for k in range(len(img[i][j])):
            if down:
                if i != 0:
                    if -1*rangeinp < int(img[i-1][j][k]) - int(img[i][j][k]) < rangeinp:
                        sayac1 += 1
                    # it compares all the channels of the pixel with the top one(previous),
                    # and adds 1 to the counter if it meets the conditions.
            if up:

                if -1*rangeinp < int(img[i+1][j][k]) - int(img[i][j][k]) < rangeinp:
                    sayac2 += 1
                # it compares all the channels of the pixel with the bottom pixel(previous),
                # and adds 1 to the counter if it meets the conditions.
            if right:

                if -1*rangeinp < int(img[i][j-1][k]) - int(img[i][j][k]) < rangeinp:
                    sayac3 += 1
                # it compares all the channels of the pixel with with the pixel on the left(previous),
                # and adds 1 to the counter if it meets the conditions.

        if sayac1 == 3:
            img[i][j] = img[i-1][j]
            # if all the channels in the pixels have met the conditions,
            # it equalizes all the values of the pixel to that of the pixel it compares(previous pixel).
        if sayac2 == 3:
            img[i][j] = img[i+1][j]
            # if all the channels in the pixels have met the conditions,
            # it equalizes all the values of the pixel to that of the pixel it compares(previous pixel).
        if sayac3 == 3:
            img[i][j] = img[i][j-1]
            # if all the channels in the pixels have met the conditions,
            # it equalizes all the values of the pixel to that of the pixel it compares(previous pixel).

        if m == 0 and n == len(img):
            operation6_func(img, i, j+1, rangeinp, 1, 1, False, False, True)
            # when we think of the image as 2-dimensional,
            # when we move down or up the column and come to the edge, we move to the left column

        elif j % 2 == 0:
            operation6_func(img, i+1, j, rangeinp, 0, n+1, True, False, False)
            # when we think of the image as 2-dimensional,
            # if the value of the line(row) we are in is even, it moves down recursively.

        elif j % 2 == 1:
            operation6_func(img, i-1, j, rangeinp, 0, n+1, False, True, False)
            # when we think of the image as 2-dimensional,
            # if the value of the line(row) we are in is odd, it moves up recursively.


    img = read_ppm_file(filename)[0]
    new_img = img
    operation6_func(new_img, 0, 0, rangeinp)
    img_printer(new_img)
    # Calls the recursive function and prints the color quantization applied image's 3d list.

if operation == 7:

    rangeinp = int(input())

    def operation7_func(img, i, j, k, rangeinp, m=0, n=1, r=0, s=1, down=True, up=False, right=False, left=False, innerright=False):
        if k >= len(img[i][j]):
            return
        # Base condition

        if down:
            if -1 * rangeinp < int(img[i-1][j][k]) - int(img[i][j][k]) < rangeinp:
                if i != 0:
                    img[i][j][k] = img[i-1][j][k]
                    # it compares the channels of the pixel with the top one(previous),
                    # it equalizes the corresponding channel value of the pixel
                    # to that of the pixel it compares(previous pixel) if it meets the conditions.
        if up:
            if -1 * rangeinp < int(img[i+1][j][k]) - int(img[i][j][k]) < rangeinp:
                img[i][j][k] = img[i+1][j][k]
                # it compares the channels of the pixel with the bottom one(previous),
                # it equalizes the corresponding channel value of the pixel
                # to that of the pixel it compares(previous pixel) if it meets the conditions.
        if right:
            if -1 * rangeinp < int(img[i][j-1][k]) - int(img[i][j][k]) < rangeinp:
                img[i][j][k] = img[i][j-1][k]
                # it compares the channels of the pixel with the left one(previous),
                # it equalizes the corresponding channel value of the pixel
                # to that of the pixel it compares(previous pixel) if it meets the conditions.
        if left:
            if -1 * rangeinp < int(img[i][j+1][k]) - int(img[i][j][k]) < rangeinp:
                img[i][j][k] = img[i][j+1][k]
                # it compares the channels of the pixel with the right one(previous),
                # it equalizes the corresponding channel value of the pixel
                # to that of the pixel it compares(previous pixel) if it meets the conditions.
        if innerright:
            if -1 * rangeinp < int(img[i][j][k-1]) - int(img[i][j][k]) < rangeinp:
                img[i][j][k] = img[i][j][k-1]
                # it compares the channel of the pixel with the left channel of it(previous),
                # it equalizes the corresponding channel value of the pixel
                # to the pixels other channel value it compares(previous channel) if it meets the conditions.

        if m == 0 and n == len(img):
            if r == 0 and s == len(img[i]):
                operation7_func(img, i, j, k + 1, rangeinp, 1, 1, 1, 1, False, False, False, False, True)
                # when we think of the image as 3-dimensional,
                # when we move down or up the column and come to the edge
                # if we already moved to the all columns in the channel we are in,
                # we move to the inside(the one on the left in the list) channel

            else:
                if k % 2 == 0:
                    operation7_func(img, i, j + 1, k, rangeinp, 1, 1, 0, s+1, False, False, True, False, False)
                    # when we think of the image as 3-dimensional,
                    # when we move down or up the column and come to the edge
                    # if the value of channel(width) we are in is even, we move to the left column
                if k % 2 == 1:
                    operation7_func(img, i, j - 1, k, rangeinp, 1, 1, 0, s+1, False, False, False, True, False)
                    # when we think of the image as 3-dimensional,
                    # when we move down or up the column and come to the edge
                    # if the value of channel(width) we are in is odd, we move to the right column
        elif (k+j) % 2 == 0:
            operation7_func(img, i + 1, j, k, rangeinp, 0, n + 1, 0, s, True, False, False, False, False)
            # when we think of the image as 3-dimensional,
            # if the sum of the line(row) and channel(width) we are in is even, it moves down recursively.
        elif (k+j) % 2 == 1:
            operation7_func(img, i - 1, j, k, rangeinp, 0, n + 1, 0, s, False, True, False, False, False)
            # when we think of the image as 3-dimensional,
            # if the sum of the line(row) and channel(width) we are in is odd, it moves up recursively.

    img = read_ppm_file(filename)[0]
    new_img = img
    operation7_func(new_img, 0, 0, 0, rangeinp)
    img_printer(new_img)
    # Calls the recursive function and prints the color quantization applied image's 3d list.


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

