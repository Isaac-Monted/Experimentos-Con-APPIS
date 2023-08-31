import tensorflow as Tf
import matplotlib.pyplot as plp

class ColorIA:
    def __init__(self):
        self.features = [
            (255,0,0),
            (255,63,0),
            (255,127,0),
            (255,191,0),
            (255,255,0),
            (191,255,0),
            (127,255,0),
            (63,255,0),
            (0,255,0),
            (0,255,63),
            (0,255,127),
            (0,255,191),
            (0,255,255),
            (0,191,255),
            (0,127,255),
            (0,63,255),
            (0,0,255),
            (63,0,255),
            (127,0,255),
            (191,0,255),
            (255,0,255),
            (255,0,191),
            (255,0,127),
            (255,0,63)
        ]

        self.targets = [0,15,30,45,60,75,90,105,120,135,150,165,180,191,210,225,240,255,270,285,300,315,330,345]

        self.CapaEntrada = Tf.keras.layers.Dense(units=3, input_shape=[3])
        self.CapaOculta0 = Tf.keras.layers.Dense(units=6)
        self.CapaOculta1 = Tf.keras.layers.Dense(units=12)
        self.CapaOculta2 = Tf.keras.layers.Dense(units=12)
        self.CapaOculta3 = Tf.keras.layers.Dense(units=6)
        self.CapaSalida = Tf.keras.layers.Dense(units=1)

        self.Modelo = Tf.keras.Sequential([self.CapaEntrada,self.CapaOculta0,self.CapaOculta1,self.CapaOculta2,self.CapaOculta3,self.CapaSalida])

        self.Modelo.compile(
            optimizer=Tf.keras.optimizers.Adam(0.43954),
            loss='mean_squared_error'
        )#0.43954

        print('Inico de Entrenamiento . . .')
        self.historial = self.Modelo.fit(self.features, self.targets, epochs=3000, verbose=False)
        print('Modelo Entrenado')

        self.Modelo.save('Color7.h5')

    def Grafica(self):
        plp.xlabel('#Epoca')
        plp.ylabel('Magnitud de Perdida')
        plp.plot(self.historial.history['loss'])
        plp.show()
    
    def Prueba(self,R,G,B):
        resultado = self.Modelo.predict([(R,G,B)])
        resultado = resultado[0][0]
        print('El valor es = ',resultado)
        return resultado

class ColorIA2:
    def __init__(self):
        self.features = [
            (18),
            (40),
            (60),
            (84),
            (106),
            (104),
            (102),
            (100),
            (98),
            (152),
            (207),
            (262),
            (318),
            (296),
            (274),
            (251),
            (230),
            (232),
            (234),
            (236),
            (238),
            (183),
            (128),
            (72)
        ]

        self.targets = [0,15,30,45,60,75,90,105,120,135,150,165,180,191,210,225,240,255,270,285,300,315,330,345]

        self.CapaEntrada = Tf.keras.layers.Dense(units=1, input_shape=[1])
        self.CapaOculta0 = Tf.keras.layers.Dense(units=2)
        self.CapaOculta1 = Tf.keras.layers.Dense(units=4)
        self.CapaOculta2 = Tf.keras.layers.Dense(units=4)
        self.CapaOculta3 = Tf.keras.layers.Dense(units=2)
        self.CapaSalida = Tf.keras.layers.Dense(units=1)

        self.Modelo = Tf.keras.Sequential([self.CapaEntrada,self.CapaOculta0,self.CapaOculta1,self.CapaOculta2,self.CapaOculta3,self.CapaSalida])

        self.Modelo.compile(
            optimizer=Tf.keras.optimizers.Adam(0.1),
            loss='mean_squared_error'
        )#0.43954

        print('Inico de Entrenamiento . . .')
        self.historial = self.Modelo.fit(self.features, self.targets, epochs=1000, verbose=False)
        print('Modelo Entrenado')

        self.Modelo.save('Tono.h5')

    def Grafica(self):
        plp.xlabel('#Epoca')
        plp.ylabel('Magnitud de Perdida')
        plp.plot(self.historial.history['loss'])
        plp.show()
    
    def Prueba(self,Color):
        resultado = self.Modelo.predict([(Color)])
        resultado = resultado[0][0]
        print('El valor es = ',resultado)
        return resultado


cosa = ColorIA2()
cosa.Prueba(18)
cosa.Grafica()