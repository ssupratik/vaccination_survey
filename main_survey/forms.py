from django.forms import ModelForm
from .models import UserDetails


class SurveyForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'


# ID_PROOF_CHOICES = (
#     (1,"Aadhaar Card"), (2,"Voter Card"), (3,"Passport"), (4,"Driving License"),
#     (5,"Pan Card")
# )

# class SurveyForm(forms.Form):

#     person_title = forms.ChoiceField(choices=(('Mr', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')), label='Title')
#     full_name = forms.CharField()
#     date_of_birth = forms.DateField()
#     id_proof = forms.ChoiceField(choices=ID_PROOF_CHOICES)
#     mobile_no = forms.CharField()
#     id_proof_no = forms.CharField()

#     """ Residential address """
#     flat_bulding = forms.CharField(label='House no. and bldg. name')
#     road_no = forms.CharField(label='Road no./name')
#     area_and_landmark = forms.CharField(label='Area and landmark')
#     district = forms.CharField()
#     ward = forms.CharField()
#     block = forms.CharField()

#     """ Vaccination Details """
#     vaccination_status = forms.ChoiceField(
#         choices=(('Y', 'Vaccinated'), ('N', 'Not Vaccinated')),
#         label='Choice of account',
#         widget=forms.RadioSelect)
#     date_of_second_dose = forms.DateField(label='Date for second dose if first dose taken')
#     registration_id = forms.CharField(label='Registration id in CoWIN portal (if any)')
#     reason = forms.CharField(label='If not vaccinated reason')

    # layout = Layout(
    #     Fieldset("User Details",
    #              Row(Span2('person_title'), Span10('full_name')),
    #              Row(Column('date_of_birth',
    #                         'mobile_no'),
    #                  Column('id_proof',
    #                         Row('id_proof_no')))),
    #     Fieldset("Address",
    #              Row('flat_bulding', 'road_no'),
    #              Row('area_and_landmark'),
    #              Row('district', 'block', 'ward')),
    #     Fieldset("Vaccination Details",
    #              Row('vaccination_status', 'date_of_second_dose', 'registartion_id'),
    #              Row('reason'))
    # )
