#统计mnist训练集中，数字到各个边界的距离的平均值
import numpy as np 

trainImages = np.load('trainImagesUint8.npy')
imageNum = trainImages.shape[0]
edgeStride = np.zeros((4,imageNum))     #分别代表上下左右的距离值

for imgNo in range(imageNum):
    print(imgNo)
    imgData = trainImages[imgNo].reshape(28,28)
    for i in range(28):
        if imgData[:,i].sum() != 0:
            edgeStride[2][imgNo] = i
            break
    for i in range(27,-1,-1):
        if imgData[:,i].sum() != 0:
            edgeStride[3][imgNo] = 27-i
            break
    for i in range(28):
        if imgData[i].sum() != 0:
            edgeStride[0][imgNo] = i
            break
    for i in range(27,-1,-1):
        if imgData[i].sum() != 0:
            edgeStride[1][imgNo] = 27-i
            break

np.save('edgeStrideVal.npy',edgeStride)