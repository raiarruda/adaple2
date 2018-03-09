from django.contrib import admin

from embed_video.admin import AdminVideoMixin

# Register your models here.

from .models import db_edp, db_habilidades, db_edp_aluno, db_recursos
from .forms import form_edp

admin.site.register(db_edp)
admin.site.register(db_habilidades)
admin.site.register(db_edp_aluno)
admin.site.register(db_recursos)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
