from django.contrib import admin
from .models import Ghost, Feeding, Toy

# Register your models here
admin.site.register(Ghost)
admin.site.register(Feeding)
admin.site.register(Toy)