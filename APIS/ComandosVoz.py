import speech_recognition as sr

Escuchar = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Escuchando. . .')
        voz = Escuchar.listen(source)
        Escrito = Escuchar.recognize_google(voz)
        print(Escrito)
except:
    print('No hay Microfono')