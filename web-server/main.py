import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #Instancia de FastAPI

@app.get('/list') #Funcion decorada: Cada que se obtenga la ruta '/list' se ejecutara la siguiente funcion
def get_list():
    return [2,3,4,5,6,7,8,9,0] #Devolvera una lista de nuemros 

@app.get('/', response_class=HTMLResponse) #Funcion decorada: Cada que se obtenga la ruta '/' tendra una respuesta de tipo HTMl
def get_main():
    #Esto es para que pueda soportar una solicitud HTML y funcione la pagina
    return """    
        <h2>Helloo</h2>
        <p>parapara</p>
        <!-- img src="quico.jpg" width="300" height="200"> -->
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()