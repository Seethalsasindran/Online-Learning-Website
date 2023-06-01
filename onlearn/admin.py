from django.contrib import admin
from . models  import students,contact,newsletter,Subjects

# Register your models here.
class studentsAdmin(admin.ModelAdmin):
    list_display=("name","email")
   
admin.site.register(students,studentsAdmin)
admin.site.register(contact)
admin.site.register(newsletter)
admin.site.register(Subjects)
