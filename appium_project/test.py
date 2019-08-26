from PIL import Image
import pytesseract


# img = Image.open(r'C:\Users\Emotion\Desktop\TIM截图20190821151545.png')
#
# # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')
# Img.save("./test.jpg")
#
# # 自定义灰度界限，大于这个值为黑色，小于这个值为白色
# threshold = 200
#
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# # 图片二值化
# photo = Img.point(table, '1')
# photo.save("./test1.jpg")


# 上面都是导包，只需要下面这一行就能实现图片文字识别
text = pytesseract.image_to_string(Image.open(r'./test.jpg'), lang='chi_sim')
print(text)
