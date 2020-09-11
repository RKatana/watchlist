import os
from app import create_app
from flask_script import Manager,Server

ENVIRON = os.environ.get('ENVIRON')
app = create_app(ENVIRON)
manager = Manager(app)
manager.add_command('serve', Server)

if __name__ == '__main__':
    manager.run()