from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_database(app):
	with app.app_context():
		if not path.exists(path.abspath("storage.db")):
			db.create_all()

def create_app():
	app = Flask(__name__, template_folder='templates', static_folder='static',)
	app.config.from_pyfile('config.py')

	print(app.config)

	from .models import Task

	db.init_app(app)
	create_database(app)

	@app.route('/', methods=['GET', 'POST'])
	def index():
		if request.method == 'POST':
			new_task = request.form.get('new-task')

			if new_task != '':
				task = Task(new_task)
				db.session.add(task)
				db.session.commit()
				print('[+] Tarefa ADD')

		return render_template('index.html')

	return app
