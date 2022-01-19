import flask
import flask_login
import flask_migrate
import flask_sqlalchemy

from config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)

login_mngr = flask_login.LoginManager(app)
login_mngr.login_view = 'login'
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import routes, models
