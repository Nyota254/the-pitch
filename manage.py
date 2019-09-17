from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Pitch

app = create_app('production')
# app = create_app('test')

manager =   Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell
def create_shell_context():
    return {'db' : db}

if __name__=="__main__":
    manager.run()

