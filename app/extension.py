from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inisialisasi extension secara global (akan diikat ke app di create_app)
db = SQLAlchemy()
migrate = Migrate()