
# Bienvenido al repositorio del Proyecto-Wawas :D

![Banner Wawas](https://raw.githubusercontent.com/OscarCampohermoso/Proyecto-Wawas/static/images/readme/readme1.png)

## Contenido <!-- omit in toc -->

En el directorio `/contenido` encontrará un listado de las partes del README para facilitar su comprensión.

- [Acerca del proyecto](#Acerca-del-proyecto)

  - [Introducción](#Introducción)
  - [Objetivo del proyecto](#Objetivo-del-proyecto)
  - [Descripción del proyecto](#Descripción-del-proyecto)

- [Estado del proyecto](#Estado-del-proyecto)

- [Instalación](#Instalación)

- [Tecnologías utilizadas](#Tecnologías-utilizadas)

- [Colaboracion deseada](#Colaboracion-deseada)

- [Preguntas frecuentes](#Preguntas-frecuentes)

- [Contactos](#Contactos)

------

## Acerca del proyecto

La funcionalidad y el objetivo del proyecto se explicaran a continuación.

### Introducción

El presente proyecto está dirigido a facilitar a los dueños de perros, la adquisición de servicios de cuidado para su mascota, a través de un sistema web para la empresa de mascotas "WAWAS. En Bolivia este sistema ofrecería una alternativa extra a la única opción actual, que es el contacto por Facebook o al WhatsApp, herramientas que aunque pueden funcionar, creemos que con un sistema las reservas de las citas y el contacto con el cuidador será de gran ayuda.

### Objetivo del proyecto

Desarrollar un sistema web para la empresa “WAWAS” que permita al usuario acceder a los servicios que ofrece la empresa, como ser: adopción, atención veterinaria, hotelería, entre otros. La sección de noticias facilitará la comunicación entre las personas que anuncien la noticia y las que estén interesadas. De la misma manera, el sistema proveerá la información suficiente para que el usuario se sienta seguro y en confianza en relación con el servicio por el cual desee optar.

### Descripción del proyecto

El presente proyecto está dirigido al desarrollo de un sistema web para la empresa mencionada, se enfoca en la interacción con el usuario, de forma en la que este consiga la información que está buscando y a la vez pueda acceder a los servicios de la empresa desde cualquier lugar por medio de la aplicación.

El sistema de Información tendrá la siguiente funcionalidad:
- Permitir el inicio de sesión a los usuarios, cuidadores y administradores.

- Permitir a los usuarios crear una cuenta y registrarse.

- Brindar información a los usuarios sobre los servicios que ofrece la empresa.

- Permitir a los usuarios visualizar y publicar en la sección las noticias.

- Permitir a los administradores gestionar la sección de noticias.

![Modelo BPMN del proceso de la sección de noticias del sistema](https://raw.githubusercontent.com/OscarCampohermoso/Proyecto-Wawas/static/images/readme/readme2.png)

**Figura 1:** Modelo BPMN del proceso de la sección de noticias del sistema.

- Permitir a los usuarios comunicarse con la empresa, por medio de un formulario de contactos, para poder dejar sus comentarios, recomendaciones o dudas.

- Permitir al administrador gestionar las citas realizadas por los usuarios.

- Permitir a los cuidadores registrarse, para poder ofrecer sus servicios como cuidador.

- Permitir a los usuarios sacar citas de los diferentes servicios que ofrece la empresa.

![Caso de uso sobre como sacar una cita en el sistema](https://raw.githubusercontent.com/OscarCampohermoso/Proyecto-Wawas/static/images/readme/readme3.png)

**Figura 2:** Caso de uso sobre como sacar una cita en el sistema

---

## Estado del proyecto

El proyecto actualmente se encunetra finalizado (08/11/2022). Pero esta abierto a sugerencias y modificaciones que generen cambios positivos hacia el proyecto.

![Sección servicios funcional](https://raw.githubusercontent.com/OscarCampohermoso/Proyecto-Wawas/static/images/readme/readme4.png)

**Figura 3:** Sección servicios funcional, listo para sacar una cita.

---

## Instalación

Debe tener instalado un editor de código fuente, como por ejemplo, Visual Studio Code [Visual Studio Code](https://code.visualstudio.com/) y el software de [Git](https://git-scm.com/downloads). Luego debe abrir un archivo en el editor de código

Copie la direccion del respositorio para clonarlo, utilice el comando *git clone*. 

```yaml
git clone https://github.com/OscarCampohermoso/Proyecto-Wawas.git
```
A continuación, debe crear un entorno virtual para el maejo adecuado. Y activarlo

```yaml
python -m venv env
.\env\Scripts\activate
```
Si es necesario actualice la versión del pip.
```yaml
python -m pip install --upgrade pip
```
Y luego instale los requerimientos que son necesarios para este proyecto.
```yaml
pip install -r requirements.txt
```
Realice las migraciones necesarias, si se lo pide el programa.
```yaml
python manage.py makemigrations
python manage.py migrate 
```
Y listo, ya puede contribuir al desarrollo de mejoras para el sistema.
Prueba el siguiente comando para visualizarlo en la red.
```yaml
python manage.py runserver
```

---

## Tecnologías utilizadas

Se desarrolló el backend del Sistema de Información basado en el modelo MVT (Modelo Vista Template) pero sigue muy de cerca el patrón de diseño MVC (Modelo Vista Controlador).

La aplicación Web se desarrolló en [Django](https://www.djangoproject.com/), un framework de desarrollo web de código abierto, escrito en Python, y priorizando las Clases Basadas en Vistas que nos proporciona Django.

Y para el frontend, además, se utilizo [Bootstrap](https://getbootstrap.com/), que es una biblioteca multiplataforma o conjunto de herramientas de código abierto para diseño de sitios y aplicaciones web.

## Colaboracion deseada
Estamos abiertos a recibir sugerencias que ayuden a la mejora del sistema.

Sugerencias aún no implementadas:

- Una sugerencia previa nos hablaba de implementar un tracking con los cuidadores de mascotas registrados en nuestro sistema, para que de esta forma el dueño de la mascota pueda estar pendiente de donde se encuentra su mascota en todo momento.

- Otra sugerencia nos hablaba de implementar un videochat entre los cuidadores y los clientes quienes son dueños de la mascota, y que este habilitado las 24 hrs.

---

## Preguntas frecuentes

> ¿Existe un limite de citas que se puede sacar en un día?

**Respuesta:**
Para controlar el flujo de citas y evitar el aglomeramiento de usuarios maliciosos. El sistema cuenta con un control sobre las citas por día. Es decir, un usuario solo puede sacar **3 citas por día.**

---

## Contactos
#### Ante cualquier duda, contactanos :D

- Campohermoso Berdeja Oscar (Líder del proyecto)
  - +591 76281889
  - oscar.campohermoso@ucb.edu.bo

- Gutiérrez Sandoval María Fernanda 
  - maria.gutierrez.s@ucb.edu.bo
  - 71544312

- Martínez Acarapi Fabiola Alejandra 
  - fabiola.martinez@ucb.edu.bo
  - 60699379

- Quiroga Perez Andrea 
  - andrea.quiroga@ucb.edu.bo
  - 67096298

---
