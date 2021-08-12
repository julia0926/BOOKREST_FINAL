from django.db import models

# Create your models here.

#inquiry CRUD model : register ask
class QInquiry(models.Model):
    #인적사항
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    #문의 내용
    qtype = models.ManyToManyField('Qtype', blank=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    #기타
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Qtype(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

#inquiry Comment model : admin answer
class Answer(models.Model):
    def __str__(self):
        return self.text

    ask_id = models.ForeignKey(QInquiry, on_delete=models.CASCADE, related_name='answer')
    text = models.TextField()