from django import forms
from .models import PTFdados
"""
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Calculo
        fields = ["ad_solo", "agregado", "quantidade"]
"""


class PTFform(forms.ModelForm):
    class Meta:
        model = PTFdados
        fields = ["escolha", "SBICS", "OLD", "LAT", "LON", "MUN", "GEOCOD",
                  "T_ARE", "AGRO", "AFIN", "SILT", "ARG", "SOLO", "C_ORG" ] #"B_TT", "B_PC"]
