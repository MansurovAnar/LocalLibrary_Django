from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

	# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)


#Defining the admin Class
class AuthorAdmin(admin.ModelAdmin):
	pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	pass
		
		