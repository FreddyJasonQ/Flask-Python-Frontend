from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        print(f"Nombre: {name}")
        print(f"Correo: {email}")
        print(f"Mensaje: {message}")

        return redirect(url_for('success', name=name))  # Usar `redirect` y `url_for`

    return render_template("contact.html")

@app.route('/success')
def success():
    # Mostrar un mensaje de éxito
    name = request.args.get('name')  # Obtener el nombre desde la URL
    return render_template("success.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
