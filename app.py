from flask import Flask, render_template
from controllers.custom_pcs_controller import custom_pcs_blueprint
from controllers.components_controller import components_blueprint

app = Flask(__name__)

app.register_blueprint(custom_pcs_blueprint)
app.register_blueprint(components_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)