from .app import db

class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))

	def __init__(self, title: str) -> None:
		self.title = title

	def __repr__(self):
		return f'<Task id={self.id} task="{self.title}">'
