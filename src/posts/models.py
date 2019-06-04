from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now = True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)


	def __init__(self, arg):
		super(Post,models.Model).__init__()
		self.arg = arg

	def __str__(self):
		return self.title

