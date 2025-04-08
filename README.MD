# Proyecto Flask: Formulario de Contacto

Este proyecto es una aplicación web desarrollada con **Python 3.9.2** y **Flask 3.1.0**, que permite a los usuarios enviar mensajes a través de un formulario de contacto. La aplicación procesa los datos enviados y muestra una página de confirmación.

## Requisitos

- **Python**: 3.9.2
- **Flask**: 3.1.0 (última versión disponible al 13 de noviembre de 2024) ([pypi.org](https://pypi.org/project/Flask/))

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Crear un entorno virtual** (recomendado):
   ```bash
   python3 -m venv env
   ```

3. **Activar el entorno virtual**:

   En Windows:
   ```bash
   env\Scripts\activate
   ```

   En macOS/Linux:
   ```bash
   source env/bin/activate
   ```

4. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

   Asegúrate de que `requirements.txt` contenga:
   ```
   Flask==3.1.0
   ```

## Uso

1. **Ejecutar la aplicación**:
   ```bash
   flask run
   ```
   La aplicación estará disponible en [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Navegar por las rutas**:
   - `/`: Página de inicio.
   - `/about`: Información sobre la aplicación.
   - `/services`: Servicios ofrecidos.
   - `/news`: Noticias y actualizaciones.
   - `/contact`: Formulario de contacto.

3. **Enviar un mensaje**:
   - Accede a `/contact`.
   - Completa los campos: Nombre, Correo Electrónico y Mensaje.
   - Haz clic en "Enviar".
   - Serás redirigido a `/success`, donde se mostrará un mensaje de agradecimiento.

## Estructura del Proyecto

```
/tu_repositorio
│
├── /templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── news.html
│   ├── contact.html
│   └── success.html
│
├── /static
│   ├── /css
│   ├── /js
│   └── /images
│
├── app.py
├── requirements.txt
└── README.md
```

## Contribuciones

1. Haz un **fork** del repositorio.
2. Crea una rama para tu contribución:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza los cambios y verifica las pruebas.
4. Commit de tus cambios:
   ```bash
   git commit -am "Añadir nueva funcionalidad"
   ```
5. Sube los cambios:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
6. Crea un **Pull Request** con una descripción detallada.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.