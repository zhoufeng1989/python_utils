#-*-coding:utf-8-*-
from PIL import Image


def watermark(src_path, dest_path, mark_path, margin=(0, 0)):
    '''
    src_path: 源图片路径
    dest_path: 目标图片路径
    mark_path: 水印图片路径
    margin:水印位置
    '''
    src_image = Image.open(src_path)
    water_mark = Image.open(mark_path)
    if src_image.mode != "RGB":
        src_image = src_image.convert("RGB")
    layer = Image.new('RGBA', src_image.size, (0, 0, 0, 0))
    position = (src_image.size[0] - water_mark.size[0] - margin[0],
                src_image.size[1] - water_mark.size[1] - margin[1])
    layer.paste(water_mark, position)
    Image.composite(layer, src_image, layer).save(dest_path)

if __name__ == '__main__':
    watermark('test.jpg', 'wm_test.jpg', 'watermark.jpg', (20, 20))
