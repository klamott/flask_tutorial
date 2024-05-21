import os

from flask import Flask


# Application Factory
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    # welcome page
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    # Register 'init-db' command with app
    from . import db
    db.init_db_to_app(app)

    from . import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    return app