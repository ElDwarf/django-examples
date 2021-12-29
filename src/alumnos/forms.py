from django.forms import ModelForm

from .models import Alumno


class AlumnoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for x in self.fields.keys():
            self.fields[x].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['curso'].widget.attrs.update({
                'class': 'form-select'
            })
        self.fields['status'].widget.attrs.update({
                'class': 'form-select'
            })

    class Meta:
        model = Alumno
        fields = ['first_name', 'last_name', 'curso', 'status', 'birthday']


class InscriptosForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['first_name', 'last_name', 'birthday']