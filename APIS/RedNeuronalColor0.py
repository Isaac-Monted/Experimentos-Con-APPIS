import tensorflow as Tf
import tensorflow_datasets as tfds
import numpy as Np

RGB_R = Np.array([255,127,0,127,255], dtype=int)
RGB_G = Np.array([0,255,255,0,0], dtype=int)
RGB_B = Np.array([0,0,255,255,4], dtype=int)
HSV = Np.array([0,90,180,270,359], dtype=int)

#Neurona 
Modelo = Tf.keras.Sequential([
    #Tf.keras.layers.Dense(units=4, input_shape=[4])
    Tf.keras.layers.Flatten(input_shape=[4]),
    Tf.keras.layers.Dense(4,activation=Tf.nn.relu),
    Tf.keras.layers.Dense(1,activation=Tf.nn.softmax)
])

#Entrenamiento
Modelo.compile(
    optimizer='adam',
    loss=Tf.keras.losses.sparse_categorical_crossentropy(),
    metrics=['accuracy']
)

#Tamaño de Lotes
TamayoLote = 4
NumEjentrena = 20
datosEntrenamiento = [RGB_R, RGB_G, RGB_B, HSV]
datosPrueba = ""

datosEntrenamiento = datosEntrenamiento.repeat().shuffle(NumEjentrena).batch(TamayoLote)
datosPrueba = datosPrueba.batch(TamayoLote)

import math
historial = Modelo.fit(datosEntrenamiento, epochs=5, steps_per_epoch= math.ceil(NumEjentrena/TamayoLote))

#Mostrar Perdidad
import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de Perdida")
plt.plot(historial.hitory["loss"])