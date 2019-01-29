from PIL import Image
import argparse
import requests
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')

args = parser.parse_args()
INPUT = args.input


def get_bin_table(threshold=140):
    """
    获取灰度转二值的映射table
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table

sample = 10

# for i in range(sample):
#     i = str(i)
#     res = requests.get(INPUT, stream=True)
#     with open('img/' + i + '.png', 'wb') as handle:
#         for chunk in res.iter_content(chunk_size=1024):
#             if chunk:  # filter out keep-alive new chunks
#                 handle.write(chunk)
#                 handle.flush()
#         handle.close()

dir_list = list('img/' + file_name for file_name in os.listdir('img'))


# 去除杂项干扰
# for img_path in dir_list:
#
#     image = Image.open(img_path)
#     imgry = image.convert('L')  # 转化为灰度图
#
#     table = get_bin_table()
#
#     out = imgry.point(table, '1')
#     out.save(img_path)


# 切割 sample 到最小元素
def cut_pic(file_path):
    image = Image.open(file_path)
    image_info = image.size

    first_black = []
    last_black = []
    continue_flag = False
    for width in range(image_info[0]):
        isBlack = False
        for height in range(image_info[1]):

            pixel_info = image.getpixel((width, height))

            # 是黑色 说明是第一个的起始位置找到了
            # 记录到 list 里面
            if pixel_info == 0 and first_black == []:
                first_black = [width, height]

                isBlack = True
            elif pixel_info == 0:
                last_black = [width, height]
                isBlack = True

        # 什么时候停下?
        # 当找到一个竖列都是白色的时候
        # 现在是最后一列全是白色

        top_black = []
        bottom_black = []
        if isBlack == False and first_black != [] and last_black != []:
            width_start = first_black[0] if first_black[0] < last_black[0] else last_black[0]
            width_end = last_black[0] if last_black[0] > first_black[0] else first_black[0]

            for height in range(image_info[1]):
                if continue_flag:
                    continue
                widthBlack = False
                for width in range(width_start, width_end):

                    pixel_info = image.getpixel((width, height))
                    if pixel_info == 0 and top_black == []:
                        top_black = [width, height]
                        widthBlack = True
                    elif pixel_info == 0:
                        bottom_black = [width, height]
                        widthBlack = True

                if widthBlack == False and top_black != [] and bottom_black != []:
                    area = (first_black[0], top_black[1], last_black[0], bottom_black[1])
                    region = image.crop(area)
                    region.show()
                    continue_flag = True
                    print(area)
                else:
                    continue_flag = False

for img_path in dir_list:
    cut_pic(img_path)