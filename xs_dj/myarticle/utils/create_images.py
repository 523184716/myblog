#!/usr/bin/env python
#coding:utf-8
from  PIL import  Image,ImageDraw,ImageFilter,ImageFont
import  random
import  string
import  os

# 随机数位数
random_num = 5
# 设定生成图片的宽高
size = (100,46)
# 图片背景色
bgl = (255,255,255)
# 在系统选取一种字体类型
font_path = 'C:\\Windows\\Fonts\\Arial.ttf'
# 验证码字体颜色设置
fontcolor = (0,0,255)
draw_line = True
# 干扰线的颜色
linecolor = (0,0,255)
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"static"+os.sep+"img"+os.sep+"test"+os.sep)
def Creat_random():
    # 创建一个字符列表
    random_list = list(string.ascii_letters)
    # print random_list
    # 加入数字,必须得先转换成字符串，不然后面join的时候会有问题
    for i in range(0,10):
        random_list.append(str(i))
    # 抽取指定数量的字符组成字符串
    return  ''.join(random.sample(random_list,random_num))

# 绘制图片中的干扰先
def Create_line(draw,width,height):
    begin = (random.randint(0,width),random.randint(0,height))
    end = (random.randint(0,width),random.randint(0,height))
    draw.line([begin,end],fill=linecolor)


def Create_image():
    # 调用前面设置的图片大小来获取宽高
    width,height = size
    # 生产图片
    image = Image.new('RGBA',size,bgl)
    # 设置字体类型及大小
    font = ImageFont.truetype(font_path,25)
    #针对这张图片创建画笔
    draw = ImageDraw.Draw(image)
    text = Creat_random()
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / random_num, (height - font_height) / random_num), text, \
              font=font,fill=fontcolor)  # 填充字符串

    if draw_line:
        Create_line(draw, width, height)
        Create_line(draw, width, height)
        Create_line(draw, width, height)
        Create_line(draw, width, height)
        Create_line(draw, width, height)
    image = image.transform((width, height), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
    # image.save('{}{}.png'.format(file_path,filename))
    return  image,text
# print Creat_random()
# print Create_image(file_path,"111")