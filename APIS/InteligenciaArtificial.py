from keras.models import load_model

class IA:
    def __init__(self):
        self.Modelo = load_model('Color.h5')

        #Modelo.summary()
    def Calcular(self, G,R,B):
        resultado = self.Modelo.predict([(R,G,B)])
        resultado = resultado[0][0]
        #print('El valor es = ',resultado)
        return resultado

class IA2:
    def __init__(self):
        self.Modelo = load_model('Color6.h5')

        #Modelo.summary()
    def Calcular(self, R,G,B):
        resultado = self.Modelo.predict([(R,G,B)])
        resultado = resultado[0][0]
        #print('El valor es = ',resultado)
        return resultado

class IA2_2:
    def __init__(self):
        self.Modelo = load_model('Color6.h5')
        self.Cambio = load_model('Tono.h5')

        #Modelo.summary()
    def Calcular(self, R,G,B):
        resultado = self.Modelo.predict([(R,G,B)])
        resultado = resultado[0][0]
        #print('El valor es = ',resultado)
        return resultado

    def Calculo2(self, Valor):
        resultado = self.Cambio.predict([(Valor)])
        resultado = resultado[0][0]
        #print('El valor es = ',resultado)
        return resultado

    def Completo(self,R,G,B):
        Valor = int(self.Calcular(R,G,B))
        Respuesta = self.Calculo2(Valor)
        #print('El valor es = ',Respuesta)
        return Respuesta


#cosa =  IA()
#cosa.Calcular(0,0,0)

#cosa =  IA2_2()
#cosa.Completo(255,0,0)