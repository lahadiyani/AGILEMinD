from flask import Flask
from config.default import Config
from app.extension import db, migrate
import os

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static', template_folder='templates', subdomain_matching=False)
    
    # Load config dari class (default: Config)
    env = os.getenv('FLASK_ENV', 'development').lower()
    if env == 'production':
        from config.production import Config as ProdConfig
        app.config.from_object(ProdConfig)
    elif env == 'development':
        from config.development import Config as DevConfig
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(config_class)

    # Inisialisasi extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprint
    from app.routes.base_route import main
    from app.routes.agents_route import agents_api
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(agents_api, url_prefix='/api/agents')

    return app
