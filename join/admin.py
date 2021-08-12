from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm
from .models import CustomUser
# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm #생성
 
    #admin에서 어떤 필드 보여줄지 
    list_display = ('username', 'major', 'student_id','is_staff')
    list_filter = ('is_superuser','is_active')
    #admin에서 수정할 때 보이는 필드들
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Student info', {'fields': ( 'username','major', 'student_id', )}),
        ('Person info', {'fields': ('phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', )}),
    )
    #admin에서 유저모델 추가할 때 보이는 필드들
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'email','password1', 'password2',)
        }),
    )
    search_fields = ('departement','student_id')
    ordering = ('student_id',)


# Now register the new UserAdmin...
admin.site.register(CustomUser, UserAdmin)