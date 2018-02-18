from flask import render_template
from news_aggregator.engine import *
from news_aggregator.database_config import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db = SQLAlchemy(app)

@app.route("/")
def main():
    db.create_all()
    return render_template("index.html")


if __name__ == "__main__":
        app.run(host='0.0.0.0')
