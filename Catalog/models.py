from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=100, help_text='Book Genre')

	def __str__(self):
		""""String for representing Genre"""
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the fil
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=100, help_text='Book summary')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 char ISBN number')

	genre = models.ManyToManyField(Genre, help_text='Select a genre for book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])
				

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)

	LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

	status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
#class Meta:
#	ordering = ['due_back']  		
	def __str__(self):
		return f'{self.id,} ({self.book.title})'

class Author(models.Model):
	"""docstring for Author"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField(null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
	lang_code = models.CharField(max_length=3, default='AZE')
	lang_name = models.CharField(max_length=20)

	def __str__(self):
		return self.lang_code
		





		
