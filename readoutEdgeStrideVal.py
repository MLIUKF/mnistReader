#读出距边界的距离信息并画出分布图；
import numpy as np 

edgeStride = np.load('edgeStrideVal.npy')
print(edgeStride.shape)
imgNum = edgeStride.shape[1]
print('   meanUpStride =',edgeStride[0].sum()/imgNum)
print(' meanDownStride =',edgeStride[1].sum()/imgNum)
print(' meanLeftStride =',edgeStride[2].sum()/imgNum)
print('meanRightStride =',edgeStride[3].sum()/imgNum)