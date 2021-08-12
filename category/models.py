from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from datetime import date, timedelta
from django.conf import settings
from join.choices import *
import django_filters

# Create your models here.

#대여 기능 : ManyToManyField 사용 -> CustomUser와 외래키로 연결
from join.models import CustomUser

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

    #detail models
    borrows = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name = 'borrow')
    wishes = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name = 'wish')
    
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

#유저가 빌린 책 
class UserBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='대출회원')
    book = models.ManyToManyField(BookClassInfo)
    rent_start = models.DateField("대출일")
    rent_end = models.DateField("실제 반납일")
    return_status = models.BooleanField("반납여부")
    return_date = models.DateField("반납일", blank=True, null=True)
    #sent_overdue_email = models.BooleanField("연체알림여부", default=False)

    def __str__(self):
        return "{} - {}".format(self.user,self.book)

    @property #Get,set 대신 사용
    def check_overdue(self):
        return self.rent_end < date.today() #연체될 시

    @classmethod #연체할시 1일씩 증가 
    def get_overdue_dates(cls): #클래스의 매개변수
        return cls.objects.filter(rent_end=date.today()+timedelta(days=1))

    # class Meta:
    #     ordering = ['-rent_start']