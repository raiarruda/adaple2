from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import db_edp, db_habilidades, db_edp_aluno, db_recursos
from embed_video.fields import EmbedVideoField

# t= translate, w= writing...
skills_choice = (('t', 'tradução'), ('w', 'escrita'),
                 ('r', 'leitura'), ('l', 'escuta'), ('s', 'fala'))


class BootstrapAuthenticationForm(AuthenticationForm):

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Usuário'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Senha'}))


class form_edp(forms.ModelForm):
    nome = forms.CharField(label='Nome',  required=True)
    objetivo_pedagogigo = forms.CharField(
        label='O que aprender? ',  required=True, widget=forms.Textarea)
    habilidades = forms.ModelMultipleChoiceField(queryset=db_habilidades.objects.all(),
                                                 label='Quais habilidades envolvidas?', required=True, widget=forms.CheckboxSelectMultiple)
    atividades = forms.CharField(label='O que fazer? ',  required=True, widget=forms.Textarea)
    metodologia = forms.CharField(label='Como fazer? ',  required=True, widget=forms.Textarea)

    class Meta:
        model = db_edp

        fields = ('nome', )


class form_add_recursos_edp(forms.ModelForm):
    class Meta:
        model=db_recursos
        fields = ('texto','video',)


class form_edp_aluno(forms.ModelForm):
    class Meta:
        model = db_edp_aluno
        fields = ('resposta', 'resposta_video',)
