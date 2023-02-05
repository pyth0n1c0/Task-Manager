from flask import Flask, render_template, request, redirect, url_for, jsonify
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


	class TaskManager():
		@app.route('/')
		def index():
			data = {}
			all_tasks = Task.query.all()

			for task in all_tasks:
				data[str(task.id)] = task.title			

			return render_template('index.html', data=data)

		@app.route('/endpoint', methods=['POST'])
		def create():
			new_task = request.form.get('new-task')

			if new_task != '':
				task = Task(new_task)
				db.session.add(task)
				db.session.commit()
			return redirect(url_for('index'))
		
		@app.route('/endpoint', methods=['PUT'])
		def rename():
			...

		@app.route('/endpoint', methods=['DELETE'])
		def delete():	
			id = request.get_json()['task-id']
			task = Task.query.get(id)
			db.session.delete(task)
			db.session.commit()

			return jsonify( {'status': 'OK'} )

	return app
