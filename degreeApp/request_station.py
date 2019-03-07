import requests as Req
import json
class ReqTemperature(object):
        def __init__(self):
                self.req=self.get_json('http://api.openweathermap.org/data/2.5/weather?q=Celaya,MX&APPID=e2ec39a79a2caf34b8498cfffd14c560')
        
        def get_json(self,url):
                response=Req.get(url)
                text=response.content
                return json.loads(text)
        def kelvin_to_celcius(self,kelvinGrdes):
                return kelvinGrdes-273.15

        def get_tmin(self):
                return self.kelvin_to_celcius(float(self.req['main']['temp_min']))

        def get_tmax(self):
                return self.kelvin_to_celcius(float(self.req['main']['temp_max']))
