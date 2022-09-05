from django.contrib import admin
from Users.models import Base_User,Teacher,Student


admin.site.register(Base_User)
admin.site.register(Teacher)
admin.site.register(Student)


# Register your models here.
