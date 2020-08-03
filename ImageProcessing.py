import PIL.Image as Image
from EssentialPack import *


def ImageConcat(IMAGES_PATH,IMAGE_SAVE_PATH,IMAGE_COLUMN,IMAGE_ROW,IMAGE_SIZE):
    '''
    Function for concat multi images into one image.
    :param IMAGES_PATH: dictionary of input images
    :param IMAGE_SAVE_PATH: output image path
    :param IMAGE_COLUMN: final columns
    :param IMAGE_ROW:final rows
    :param IMAGE_SIZE: size of input image, must be like 256x256
    :return:
    '''
    IMAGES_FORMAT = ['.jpg', '.JPG']

    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))  # 创建一个新图
    # Step1. get image from images_path
    list_n = os.listdir(IMAGES_PATH)
    list_n.sort(key=lambda x:int(x.split("_")[-1][:-4]))
    image_names = [name for name in list_n for item in IMAGES_FORMAT if
                   os.path.splitext(name)[1] == item]

    # Step2. concat image in order , save to ImageSavePath
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(os.path.join(IMAGES_PATH,image_names[IMAGE_COLUMN * (y - 1) + x - 1])).resize(
                (IMAGE_SIZE, IMAGE_SIZE), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH)  # save