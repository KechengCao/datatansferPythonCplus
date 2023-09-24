import os

from __init__ import blueprint
from main import create_app


application = create_app(os.getenv("BOILERPLATE_ENV") or "dev")
application.register_blueprint(blueprint)
application.app_context().push()

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5001)