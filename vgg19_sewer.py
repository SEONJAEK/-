from keras.applications.vgg19 import VGG19, preprocess_input
from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50
from keras.applications.inception_v3 import InceptionV3
#from keras.applications import AlexNet
from keras.models import Model
from keras.layers import GlobalAveragePooling2D, Dense
from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.optimizers import SGD,Adam,RMSprop
import keras.backend as K
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "1,2,3" #gpu선택 우리 서버 gpu는 0,1,2,3 중 3개선택

def eachFile(filepath):
	pathDir = os.listdir(filepath)
	out = []
	for allDir in pathDir:
		child = allDir
		out.append(child)
	return out



NUM_CLASSES = 9
TRAIN_PATH = '/data1/newestsewer/sewer/'  #data location 1class 500이상하면 좋음
TEST_PATH = '/data1/yanfen/new_dataset/test' #test data 1class 100개이상

FC_NUMS = 4096 #fully connected number 4096은 뉴런의 개수

FREEZE_LAYERS = 17  #

IMAGE_SIZE = 224 #input image size 224,224 고정되어있음


base_model = VGG19(input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3), include_top=False, weights='imagenet')  #keras function  식 참고 사이트:https://keras.io/ko/applications/#vgg19
#base_model로 vgg19썼다. alexnet으로 고쳐서 써도 됨


x = base_model.output #base_model.output  the final output 마지막 layer는 FC3(fully connected) imagenet은 1000class 가지고 있는데 그래서 1000neurons  ,하수관은 9 class

x = GlobalAveragePooling2D()(x)
x = Dense(4096, activation='relu')(x) #Dense는 fully connected laye
#x = normalization.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001)(x)
prediction = Dense(NUM_CLASSES, activation='softmax')(x)


model = Model(inputs=base_model.input, outputs=prediction)

model.summary()

print("layer nums:", len(model.layers))



for layer in model.layers[:FREEZE_LAYERS]:
    layer.trainable = False
for layer in model.layers[FREEZE_LAYERS:]:
    layer.trainable = True


# for layer in base_model.layers:
# 	layer.trainable = False
for layer in model.layers:
    print("layer.trainable:", layer.trainable)

# 预编译模型
model.compile(optimizer=SGD(lr=0.001, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])
#model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator()
train_generator = train_datagen.flow_from_directory(directory=TRAIN_PATH,
                                                    target_size=(IMAGE_SIZE, IMAGE_SIZE), classes=eachFile(TRAIN_PATH))
# test_datagen = ImageDataGenerator()
# test_generator = test_datagen.flow_from_directory(directory=TEST_PATH,
#                                                   target_size=(IMAGE_SIZE, IMAGE_SIZE), classes=eachFile(TEST_PATH))
filepath = 'sewer_weight_9.h5'
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
# 运行模型
history_ft = model.fit_generator(train_generator, epochs=10, callbacks=[checkpoint])
model.save('sewer_weight_9(final).h5')



# import matplotlib.pyplot as plt
# #% matplotlib inline
#
#
# def plot_training(history):
# 	plt.figure(12)
#
# 	plt.subplot(121)
# 	train_acc = history.history['acc']
# 	val_acc = history.history['val_acc']
# 	print("VGG19 val_acc:")
# 	print(val_acc)
# 	epochs = range(len(train_acc))
# 	plt.plot(epochs, train_acc, 'b', label='train_acc')
# 	plt.plot(epochs, val_acc, 'r', label='test_acc')
# 	plt.title('Train and Test accuracy')
# 	plt.legend()
#
# 	plt.subplot(122)
# 	train_loss = history.history['loss']
# 	val_loss = history.history['val_loss']
# 	print("VGG19 val_loss:")
# 	print(val_loss)
# 	epochs = range(len(train_loss))
# 	plt.plot(epochs, train_loss, 'b', label='train_loss')
# 	plt.plot(epochs, val_loss, 'r', label='test_loss')
# 	plt.title('Train and Test loss')
# 	plt.legend()
#
# 	plt.show()
# plot_training(history_ft)