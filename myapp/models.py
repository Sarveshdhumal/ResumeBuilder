from django.db import models

STATE_CHOICE = (
 ('Berlin','Berlin'),
 ('Bavaria','Bavaria'),
 ('Lower Saxony','Lower Saxony'),
 ('Baden-Württemberg','Baden-Württemberg'),
 ('Rhineland-Palatinate','Rhineland-Palatinate'),
 ('Saxony','Saxony'),
 ('Thuringia','Thuringia'),
 ('Hessen','Hessen'),
 ('North Rhine-Westphalia','North Rhine-Westphalia'),
 ('Saxony-Anhalt','Saxony-Anhalt'),
 ('Brandenburg','Brandenburg'),
 ('Mecklenburg-Vorpommern','Mecklenburg-Vorpommern'),
 ('Hamburg','Hamburg'),
 ('Schleswig-Holstein','Schleswig-Holstein'),
 ('Saarland','Saarland'),
 ('Bremen','Bremen'),
)

class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 locality = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pin = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE, max_length=50)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
 profile_image = models.ImageField(upload_to='profileimg', blank=True)
 my_file = models.FileField(upload_to='doc', blank=True)


