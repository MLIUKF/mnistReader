import matplotlib.pyplot as plt
import numpy as np

class Image(object):
    def __init__(self, ax):
        self.ax = ax
        ax.set_title('MNIST')
        self.trainImages = np.load('trainImagesUint8.npy')
        self.trainLabels = np.load('trainLabelsNumUint8.npy')
        self.imageOrder = 986
        #self.image = (np.array([self.trainImages[self.imageOrder]]*3)).transpose().reshape(28,28,3)
        self.image = (self.trainImages[self.imageOrder].reshape(28,28))/255
        self.im = ax.imshow(self.image, cmap='gray_r')
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        temp = self.imageOrder + int(event.step)
        if temp >= 0 and temp < 55000:
            self.imageOrder = temp
        elif temp < 0:
            self.imageOrder = 0
        else:
            self.imageOrder = 54999
        self.update()

    def update(self):
        #self.image = (np.array([self.trainImages[self.imageOrder]]*3)).transpose().reshape(28,28,3)
        self.image = (self.trainImages[self.imageOrder].reshape(28,28))/255
        self.im.set_data(self.image)
        ax.set_ylabel('Image %s' % self.imageOrder)
        ax.set_xlabel('Num %s' % self.trainLabels[self.imageOrder])
        self.im.axes.figure.canvas.draw()


fig, ax = plt.subplots(1, 1)
imageDisplay = Image(ax)
fig.canvas.mpl_connect('scroll_event', imageDisplay.onscroll)
#plt.grid(True, linestyle = "-.", color = "#DEDEDE", linewidth = "1") 
xline = np.arange(-0.5, 28, 1)
yline = np.arange(-0.5, 28, 1)
plt.vlines(xline, -0.5, 27.5, colors="#efefef", linestyles='solid')
plt.hlines(yline, -0.5, 27.5, colors="#efefef", linestyles='solid')
plt.show()