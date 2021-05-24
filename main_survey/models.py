from django.db import models
from django.db.models.deletion import CASCADE


"""

    person_title = forms.ChoiceField(choices=(('Mr', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')), label='Title')
    full_name = forms.CharField()
    date_of_birth = forms.DateField()
    id_proof = forms.ChoiceField(choices=ID_PROOF_CHOICES)
    mobile_no = forms.CharField()
    id_proof_no = forms.CharField()

    flat_bulding = forms.CharField(label='House no. and bldg. name')
    road_no = forms.CharField(label='Road no./name')
    area_and_landmark = forms.CharField(label='Area and landmark')
    district = forms.CharField()
    ward = forms.CharField()
    block = forms.CharField()

    vaccination_status = forms.ChoiceField(
        choices=(('Y', 'Vaccinated'), ('N', 'Not Vaccinated')),
        label='Choice of account',
        widget=forms.RadioSelect)
    date_of_second_dose = forms.DateField(label='Date for second dose if first dose taken')
    registration_id = forms.CharField(label='Registration id in CoWIN portal (if any)')
    reason = forms.CharField(label='If not vaccinated reason')

"""
class DistrictDetailsMaster(models.Model):
    district_name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key= True)

    def __str__(self):
        return self.district_name


class BlockDetailsMaster(models.Model):
    block_name = models.CharField(max_length=50)
    district_id = models.ForeignKey(DistrictDetailsMaster, on_delete=CASCADE)
    id = models.IntegerField(primary_key= True)

    def __str__(self):
        return self.block_name


class WardDetailsMaster(models.Model):
    ward_name = models.CharField(max_length=50)
    district_id = models.ForeignKey(DistrictDetailsMaster, on_delete=CASCADE)
    block_id = models.ForeignKey(BlockDetailsMaster, on_delete=CASCADE)
    id = models.IntegerField(primary_key= True)

    def __str__(self):
        return self.ward_name


class UserDetails(models.Model):
    ''' Survey details of user'''
    person_title = models.CharField(max_length=5)
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=50)
    id_proof = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=12)
    id_proof_no = models.CharField(max_length=20)
    
    address = models.CharField(max_length=100)
    ward = models.ForeignKey(WardDetailsMaster, on_delete=CASCADE)
    block = models.ForeignKey(BlockDetailsMaster, on_delete=CASCADE)
    district = models.ForeignKey(DistrictDetailsMaster, on_delete=CASCADE)
    
    VACCINATION_STATUS = [('Yes', 'Vaccinated'),
        ('No', 'Not Vaccinated')]
    vaccination_status = models.CharField(max_length=3, choices=VACCINATION_STATUS,
        default='No')
    date_of_second_dose = models.DateField(max_length=50)
    registration_id = models.CharField(max_length=20)
    reason = models.CharField(max_length=100)


