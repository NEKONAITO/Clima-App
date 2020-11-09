from django.shortcuts import render
import json
import urllib.request
# Create your views here.

# ---------------------------------------------------

def index(request):
    if request.method == 'POST':
        ciudad = request.POST['entrada']
        # BUSCA CIUDAD EN INPUT DE INDEX.HTML

        # API A JSON
        url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=e388302d7bbfeb525550c747d087ad8f').read()

        # JSON A DICCIONARIO
        data_dic = json.loads(url)

        data = {
            "codigo_pais": str(data_dic['sys']['country']),
            "coordenadas_pais": str(data_dic['coord']['lon']) + ' ' + str(data_dic['coord']['lat']),
            "temperatura": str(data_dic['main']['temp']) + 'k',
            "presion": str(data_dic['main']['pressure']),
            "humedad": str(data_dic['main']['humidity']),
        }
        print(data)
    else:
        data ={}
    return render(request, "main/index.html", data)

# ---------------------------------------------------