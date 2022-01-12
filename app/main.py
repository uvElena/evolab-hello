from app import create_app, Configuration
from models import db


if __name__ == '__main__':
    app = create_app(Configuration)
    with app.app_context():
        import view
        db.create_all()
    app.run(port=5001, host='0.0.0.0')
