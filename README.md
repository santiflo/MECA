# MECA

## Descripción: Desarrollar una herramienta web que permita desplegar contenido multimedia en formato de exposición digital con el fin de favorecer la participación de la comunidad de Potrerito en la preservación de su patrimonio cultural.

Esta herramienta permitirá que sus historias y sus registros están organizados y unidos de una manera estructural que pueda elegir el usuario, ya que no se requerirá la creación de una nueva página o plataforma para mostrar el avance y la historia que se ha ido realizando todos estos años, dando así el espacio para que su recorrido sea agradable y esté a disposición de todas las personas con el interés de estas comunidades. 

Por ende este proyecto utilizó la tecnología de React,  javascript , Css , Html para el Front-end y Python(flask) para el Back-end y MySQL como motor de base de datos.

## Primeros pasos con React para ejecutar el proyecto. Aunque el proyecto estará en la web y se podrá usar libremente.

## Requisitos: Se debe tener si se desea instalar:

### Node.JS	
Node instalado en su máquina. Podrá encontrar los pasos en Cómo instalar Node.js y crear un entorno de desarrollo local. (Tambien se puede ver https://www.cursosgis.com/como-instalar-node-js-y-npm-en-4-pasos/#:~:text=Para%20comprobar%20que%20se%20nos,la%20versi%C3%B3n%206.14.8). )
El paquete de líneas de create-react-app comando create-react-app para crear el código de texto estándar para su aplicación React. Si está usando npm < 5.2, es posible que deba instalar create-react-app como dependencia global.
Igualmente NPM, en el caso de no descargar automáticamente se debe hacer ya que es muy importante

### MySQL
Es necesario tener una base de datos MySQL

### Python


## Instalación 

### Node.JS
Puedes instalarlo desde npm O también clonando el repositorio `$ git clone url` 
Link del repositorio: https://github.com/jeisongarces19/Proyecto-React-Meca

#### Scripts disponibles

Cuando se obtenga el proyecto tendrá una carpeta con archivos y carpetas. Debería ir a la consola o terminal, en el caso de usar alguna plataforma de edición como Visual studio usar la terminal propia de la herramienta. 

En el proyecto usted puede ejecutar:

##### ‘npm start’

Ejecuta la aplicación en modo desarrollador. Donde podrá visualizar el proyecto cuando se termine de ejecutar. 

Abra en su navegador web la siguiente URL “http://localhost:3000“

El modo desarrollador le permite actualizar la página web de manera inmediata a medida que realiza cambios en el código.

##### ‘npm test’

Ejecuta el modo de prueba de manera interactiva.

##### ‘npm run build’

Permite construir su aplicación para producción en el fichero ‘build’. Empaquetando de manera correcta React y optimiza la compilación para obtener un mejor rendimiento.

La compilación se minimiza y los nombres de archivo incluyen los hashes.

### MySQL
Crear una base de datos llamada 'MECA' en el gestor de base de datos MySQL, es necesario tener tanto los parametros de la conexion como sus credenciales
para que el back-end pueda almacenar los datos capturados de los usuarios

### Python
1) Para la instalación del backend es necesario configurar un ambiente para que se instalen las librerias de Flask, para ello puede hacer uso del comando 
'python3 -m venv env' el cual creara un entorno llamado 'env' el cual tendra una copia de python que actualmente tiene la maquina isntalada, con el fin de no 
instalar librerias quepuedan interferir con la maquina.
2) Seguido se debe clonar el repositorio: https://github.com/santiflo/MECA
4) Ubicarse en el repositorio clonado MECA
3) Ejecutar el comando 'pip install -r requirements.txt'
4) Crear un archivo llamado config.py con la siguiente informacion en la raiz del proyecto:
	
 	import os

	secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

	DEBUG = True
	# Remplazar los parametros con las credenciales de la base de datos MySQL
	#<nombre_usuario> = nombre de usuario de la base de datos
	#<contrasena> = Contrasena de la base de datos
	#<end_point> = Ruta web o direccion ip la cual se encuentra alojada la base de datos
	SQLALCHEMY_DATABASE_URI = "mysql://<nombre_usuario>:<contrasena>@<end_point>/MECA"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

5) Para ejecutar el servidor ejecutar el comando 'py index.py' en la raiz del proyecto

### En nuestro caso como el proyecto se encuentra alojado en un dominio solo tendrá que acceder al URL para ver la página web. En el caso de querer levantar también el proyecto. Se debe tener acceso a un dominio y un espacio compatible con React. Ya dependerá de sus gustos y posibilidades. Puede usar AWS, ISS, Plataformas e incluso servidores gratuitos o del mismo react, etc.



## Como se encuentra construido el Front-end:

- App.js= opcines con Switch y llamado de ventanas con Route. se export default App;

- - index.js= Aqui se llama a la aplicacion la cual seria App.s 

- Constantes.s = Aqui es donde coloco donde esta ubicada la aplicacion en cuestion del Backup- Aqui esta local y es http://localhost/api-php-react-main por php C:\xampp\htdocs\api-php-react-main

- Nav.js= Aqui es la navegacion manual que puede hacer el usuario. Es como el headers de la pagina. Donde decimos con un NavLink onClick a que pagina queremos ir. por el cual podemos agregar bibliografia, comentarios, soporte y ayuda, etc.  Es como el menu de la pagina. Tambien aqui se pone el orden de como aparece el menu.

- Footer= Es el pie de página, la cual es una sección ubicada debajo del texto principal o cuerpo. Normalmente se utiliza como espacio para el número de página y en este caso informacion de la empresa y de los creadores al igual que de la fundacion.


## Como se encuentra construido el back-end: El back-end esta basado en un patron de diseño MVC, aunque la vista se encuentra separada ya que se tiene un servidor aparte para hacer el consumo de los servicios ofrecidos por el back-end

- Models/: Directorio que contiene los modelos de cada uno de los objetos
- Controllers/: Contiene la rutas disponibles para ser consumidas por el front-end
- requirements.txt: Las librerias necesarias para que funcione el proyecto
- index.py: El archivo principal para configurar el puerto y ejecutar el back-end 
- confing.py: archivo que debe ser creado para configurar la conexion con la base de datos
- app.py: El archivo principal del proyecto donde se llaman las librerias utlizadas, se llaman los modelos de cada uno de los objetos y los controladores de 
los objetos


#README AUTOMATICO DE REACT:

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
