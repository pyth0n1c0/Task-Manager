from .app import db

class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(100))

	def __init__(self, task: str) -> None:
		self.task = task

	def __repr__(self):
		return f'<Task id={self.id} task="{self.task}">'
