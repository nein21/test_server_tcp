# test_server_tcp
Servidor tcp

    El servidor  permitira que se establesca una conexion y recibir
    cualquier cantidad de mensajes sin cerrar la conexion hasta
    que el cliente decida cerrar la conexion enviando la palabra
    desconexion en mayusculas 

## Iniciar cliente y servidor
    -Servidor: se posicionara en la carpeta principal del proyecto ya sea
    desde una terminal cmd o terminal del ide (visualcode, pycharm) de
    desarrollo y se ejecutara el siguiente comando "python main.py"

    -Cliente: en una segunda terminal ya sea cmd o terminal del ide
    (visualcode, pycharm) de desarrollo se ejecutara el siguiente comando
    "python cliente.py"

    -el tener cliente y servidor ejecutando se ya se puede realizar el 
    envio de mensajes a traves de cliente, cada que se envie un mensaje 
    el servidor respondera el mismo texto pero en mayusculas

    -el cliente siempre estara esperando un texto para enviarlo
    al servidor, si se envia la palabra "DESCONEXION" el servidor
    cerrara la conexion con el cliente y cliente dejara de trabajar.
    se necesitara ejecutar de nuevo el cliente para poder enviar
    mensajes al servidor

    -en la carpeta log se generara un log para cliente y servidor
    alli se registraran los errores y mensajes enviados y la respuesta

### Ejemplos
    1.- Por favor, introduce el mensaje: hola mundo
        Mensaje Enviado: hola mundo
        Respuesta Servidor: HOLA MUNDO

    2.- Por favor, introduce el mensaje: DESCONEXION
        Mensaje Enviado: DESCONEXION
        Respuesta Servidor: DESCONEXION
 


