import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt


# Random Noise Function
def add_random_noise(x):  # 노이즈 추가 함수
    x = x + np.random.normal(size=x.shape) * np.random.uniform(1, 5)
    x = x - x.min()
    x = x / x.max()

    return x * 255.0


# Set your dataset directory
# Directory Structure:
# -- train-set
# ------------/on_mask
# ------------/off_mask
# --- test-set
# ------------/on_mask
# ------------/off_mask

TRAINING_DIR = "./dataset/train"  # 학습데이터셋 경로 설정
VALIDATION_DIR = "./dataset/val"  # 테스트데이터셋 경로 설정

batch_size = 8

# Image Data Generator with Augmentation
training_datagen = ImageDataGenerator(  # image augmentation
    rescale=1. / 255,  # 0~1로 범위 조정
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    brightness_range=(0.5, 1.3),
    horizontal_flip=True,
    fill_mode='nearest',
    preprocessing_function=add_random_noise)

validation_datagen = ImageDataGenerator(rescale=1. / 255)  # testset에서는 augmentation 진행하지 않음

# Reading images from directory and pass them to the model
train_generator = training_datagen.flow_from_directory(TRAINING_DIR)  # batch_size=batch_size,
# target_size=(224, 224),
# class_mode='categorical',shuffle=True

validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    batch_size=batch_size,  # batch size(한번에 처리할 이미지 개수) 설정
    target_size=(224, 224),  # 이미지 크기 설정
    class_mode='categorical'  # 분류
)

# Plotting the augmented images
img, label = next(train_generator)  # train에서 학습데이터 불러와서 augmentation까지 처리
plt.figure(figsize=(20, 20))

for i in range(8):
    plt.subplot(3, 3, i + 1)
    plt.imshow(img[i])
    plt.title(label[i])
    plt.axis('off')

plt.show()

# Load pre-trained base model.
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                               include_top=False, weights='imagenet')
# Freeze the base model
base_model.trainable = False

# Add Custom layers
out_layer = tf.keras.layers.Conv2D(128, (1, 1), padding='SAME', activation=None)(base_model.output)
out_layer = tf.keras.layers.BatchNormalization()(out_layer)
out_layer = tf.keras.layers.ReLU()(out_layer)  # 7x7x128

out_layer = tf.keras.layers.GlobalAveragePooling2D()(out_layer)  # 128

out_layer = tf.keras.layers.Dense(2, activation='softmax')(out_layer)

# Make New Model
model = tf.keras.models.Model(base_model.input, out_layer)

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              metrics=['accuracy'])

# Training
history = model.fit(train_generator, epochs=25,
                    validation_data=validation_generator, verbose=1)

# Save the trained model
model.save("saved_model.h5")
