

class Foco:
    def __init__(self):
        #Datos de configuracion
        self.ACCESS_ID = '7k8nmm5r8je8xkfa3x8s'
        self.ACCESS_KEY = '120a7baeabcc40d2b1a25072547fcf22'

        #Servidor
        self.ENDPOINT = 'https://openapi-ueaz.tuyaus.com'

        self.USERNAME = 'DesinGlasssmartwindows@gmail.com'
        self.PASSWORD = 'DesinGlass0119*'

        self.DEVICE_ID = '60450132500291b103a0'

        from tuya_connector import TuyaOpenAPI

        self.openapi = TuyaOpenAPI(self.ENDPOINT,self.ACCESS_ID, self.ACCESS_KEY)
        self.openapi.connect()

    def Estado(self):
        # v1.0/iot-03/devices/60450132500291b103a0/specification" 

        respuesta = self.openapi.get("/v1.0/iot-03/devices/{}/specification".format(self.DEVICE_ID))
        return respuesta

    def Estatus(self):
        respuesta = self.openapi.get("/v1.0/iot-03/devices/{}/status".format(self.DEVICE_ID))
        return respuesta

    def OnOff(self, Estado):
        command = {"commands":[{"code":"switch_led","value":Estado}]} 
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)
    
    def Color(self, R, G, B, S, L):
        lista = self.convensor(R,G,B)
        H = lista[0]
        #S = 255 #lista[1]
        #V = 255 #lista[2]'''

        '''print(H)
        print(type(H))
        print(S)
        print(V)'''
        #from RerNeuuronalColor1 import ColorIA

        #H = ColorIA.Prueba(R,G,B)
        #S = S
        #V = L 

        command = {"commands":[{"code":"colour_data","value":{"h":H,"s":S, "v":L}}]} 
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)

    def Color2(self,R,G,B,S,L):
        from InteligenciaArtificial import IA2
        cosa = IA2()
        Conv = int(cosa.Calcular(R=G, G=R, B=B))
        print(Conv)

        H = int(Conv)

        command = {"commands":[{"code":"colour_data","value":{"h":H,"s":S, "v":L}}]} 
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)

    def Color2_2(self,R,G,B,S,L):
        from InteligenciaArtificial import IA2_2
        cosa = IA2_2()
        Conv = int(cosa.Completo(R=G, G=R, B=B))
        print(Conv)

        H = int(Conv)

        command = {"commands":[{"code":"colour_data","value":{"h":H,"s":S, "v":L}}]} 
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)

    def Color3(self,H,S,L):
        command = {"commands":[{"code":"colour_data","value":{"h":H,"s":S, "v":L}}]} 
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)

    def convensor(self, R, G, B):
        r = R / 255.0
        g = G / 255.0
        b = B / 255.0

        minimo = min(r,g,b)
        maximo = max(r,g,b)
        diferencia = maximo - minimo

        #Valor de h
        if minimo == maximo:
            h = 0
        elif maximo == r:
            h = (60 * ((g - b)/diferencia) + 360) % 360
        elif maximo == g:
            h = (60 * ((b - r)/diferencia) + 120) % 360
        elif maximo == b:
            h = (60 * ((r - g)/diferencia) + 240) % 360

        #Valor de s
        if maximo == 0:
            s = 0
        else:
            s = (diferencia / maximo) * 100

        #Valor de v
        v = maximo * 100

        Lista = [int(h),int(s),int(v)]

        return Lista

    def LuzBlanca(self, Luz):
        if Luz == 1:
            Valor = "colour"
        else:
            Valor = "white"

        command = {"commands": [{"code":"work_mode", "value":Valor}]}
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)

    def Brillo(self, Brillo):
        command = {"commands": [{"code":"bright_value", "value":Brillo}]}
        self.openapi.post("/v1.0/iot-03/devices/{}/commands" .format(self.DEVICE_ID), command)

    def valores(self):
        Estatus = self.Estatus()
        Lista = Estatus['result']
        #print(len(Lista))
        Memoria = []
        for i in Lista:
            accion = i['code']
            valor = i['value']

            pre = []
            pre.append(accion)
            pre.append(valor)

            Memoria.append(pre)

        #print(Memoria)

        #for e in Memoria:
        #    print("{} : {}".format(e[0],e[1]))
        return Memoria



cosa = Foco()
#cosa.OnOff(True)

#cosa.OnOff(False)

#cosa.Color2(0,255,0,255,255)

#cosa.LuzBlanca(0)

#cosa.Brillo(25)

#cosa.Color(0,0,0,0,80)
#print(cosa.convensor(0,0,255)) #100,50,255 #255,120,30

#print(cosa.Estado())

#cosa.valores()
