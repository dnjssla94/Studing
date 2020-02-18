from PIL import Image
# import requests

# url = 'https://cdn.pixabay.com/photo/2019/12/08/16/00/nature-4681448_1280.jpg'
# img = Image.open(requests.get(url, stream = True).raw)
# img.save('sample2.jpg')
# #img = Image.open('C:\\test\\sample.jpg')
# # img = img.rotate(45)
# # img.save('sample.png')
# img.show()

import cv2
import requests
import numpy

# url = 'https://cdn.pixabay.com/photo/2015/01/28/23/35/landscape-615429_1280.jpg'
# arr = numpy.asarray(bytearray(requests.get(url).content), dtype = numpy.uint8)
# #content는 바이트 형태다. uint8은 '부호가 없는 정수형 값', 즉 부호가 없는 정수형 타입으로 numpy배열을 생성한것
# img = cv2.imdecode(arr,cv2.IMREAD_COLOR)

# print(type(img))

# cv2.imshow('A',img)#A는 윈도우 이름 아무거나
# cv2.waitKey(0)#openCV는 창이 자체적으로 만들어지는데 이게 없으며 창이 떳다가 바로 사라짐.
# cv2.destroyAllWindows()

#------------------------------------------
pil_image = Image.open('sample2.jpg')
opencv_image = numpy.array(pil_image)
opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)
# pillow는 RGB고 openCV는 BGR이기 때문에 컨퍼트를 안하면 색이 달라진다. 
cv2.imshow('A', opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()