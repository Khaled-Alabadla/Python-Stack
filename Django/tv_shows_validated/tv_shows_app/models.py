from django.db import models

class ShowManager(models.Manager):
	def create_validator(self, postData, show_id=None):
		errors = {}

		title = postData.get('title', '').strip()

		if not title:
			errors['title'] = "Title is required."

		elif len(title) < 2:
			errors['title'] = "Title must be at least 2 characters long."

		elif Show.objects.filter(title=title).exclude(id=show_id).exists():
			errors['title'] = "A show with this title already exists."

		network = postData.get('network', '').strip()

		if not network:
			errors['network'] = "Network is required."

		if network and len(network) < 3:
			errors['network'] = "Network must be at least 3 characters long if provided."
		description = postData.get('description', '').strip()

		if description and len(description) < 10:
			errors['description'] = "Description must be at least 10 characters long "

		release_date = postData.get('release_date')

		if not release_date:
			errors['release_date'] = "Release date is required."

		if release_date:
			try:
				import datetime
				parsed_datetime = datetime.datetime.strptime(release_date, '%Y-%m-%d')
				if parsed_datetime.date() > datetime.date.today():
					errors['release_date'] = "Release date cannot be in the future."
			except ValueError:
				errors['release_date'] = "Release date must be in YYYY-MM-DD format."

		return errors
	
	def edit_validator(self, postData, show_id):
		errors = self.create_validator(postData, show_id=show_id)

		# title should be unique except for the current show
		title = postData.get('title', '').strip()
		if title and Show.objects.filter(title=title).exclude(id=show_id).exists():
			errors['title'] = "A show with this title already exists."
		return errors
	
	def add_show(self, postData):
		title = postData.get('title', '').strip()
		network = postData.get('network', '').strip()
		release_date = postData.get('release_date') or None
		description = postData.get('description', '').strip()
		return self.create(
			title=title,
			network=network,
			release_date=release_date,
			description=description,
		)
	
	def update_show(self, postData, show_id):
		show = self.get(id=show_id)
		show.title = postData.get('title', show.title).strip()
		show.network = postData.get('network', show.network).strip()
		rd = postData.get('release_date')
		show.release_date = rd or None
		show.description = postData.get('description', show.description).strip()
		show.save()
		return show
	
class Show(models.Model):
	title = models.CharField(max_length=255)
	network = models.CharField(max_length=255, blank=True)
	release_date = models.DateField(null=True, blank=True)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ShowManager()

	def __str__(self) -> str:
		return f"{self.title} ({self.network})"
