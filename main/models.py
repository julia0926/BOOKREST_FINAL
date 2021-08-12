from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from datetime import date, timedelta
from django.conf import settings
from join.choices import *

# Create your models here.

#기본적인 책 정보 
class BookClassInfo(models.Model):
    title = models.CharField("책제목", max_length=45)
    image = models.ImageField("책표지", blank=True,null=True)
    author = models.CharField("저자", max_length=45)
    price = models.IntegerField("가격",null=True)
    publisher = models.CharField("출판사", max_length=45)
    pubdate = models.DateField("출판일",null=True)
    stock = models.SmallIntegerField("재고", default=5)
    department = models.CharField("수업개설학과", max_length=30)
    class_name = models.CharField("수업명", max_length=30)
    professor = models.CharField("교수", max_length=30)
    # semester = models.CharField("개설학기", max_length=30,null=True)
    # class_code = models.CharField("과목코드", max_length=7,null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return "{} - {}".format(self.title,self.class_name)

#물리적인 책 각각의 상태
class BookWhere(models.Model):
    STATUS = [
        ('보관','보관'),
        ('대출','대출')
    ]
    book_status = models.CharField(choices=STATUS, max_length=5)
    book_info_id = models.ForeignKey(BookClassInfo, on_delete=models.CASCADE) #ManyToOne

    #대출
    def rent_book(self, user): #매개변수
        rent_start = date.today()
        rent_end = date.today() - timedelta(month=3)
        rent_info = self.UserBook_set.create(user=user, rent_start=rent_start,rent_end=rent_end,return_status=False)
        self.rent_info=rent_info
        self.save()

    #반납
    def return_book(self):
        self.rent_info.return_status=True
        self.rent_info.return_date = date.today()
        self.rent_info.save()
        self.rent_info=None
        self.save()

    def check_overdue(self):
        return self.rent_info.rent_end < date.today()