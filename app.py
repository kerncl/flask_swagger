from flask import render_template
import connexion
# from connexion.resolver import RestyResolver
from connexion.resolver import MethodViewResolver

from pathlib import Path

SWAGGER_PATH = Path(__file__).parent.joinpath('swagger.yml')

app = connexion.App(__name__, specification_dir='./')
app.add_api(SWAGGER_PATH)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)