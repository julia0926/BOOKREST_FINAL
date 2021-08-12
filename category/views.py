from django.core import paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from .models import BookClassInfo
from join.models import CustomUser
from django.core.paginator import Paginator

# 검색과 페이징
def category(request):
    
    books = BookClassInfo.objects.all()
    search = request.GET.get('search', '')
    sort_val = books

    if search:
        books = books.filter(title__icontains=search)
        sort_val = books

    major = request.GET.get('major', '')
    if major == "인문":
        major_list = BookClassInfo.objects.filter(department='인문융합자율학부')
        sort_val = major_list
    if major == "사회":
        major_list = BookClassInfo.objects.filter(department='사회융합자율학부')
        sort_val = major_list
    if major == "미컨":
        major_list = BookClassInfo.objects.filter(department='미디어콘텐츠융합자율학부')
        sort_val = major_list
    if major == "IT":
        major_list = BookClassInfo.objects.filter(department='IT융합자율학부')
        sort_val = major_list

    paginator = Paginator(sort_val, 9)
    page = request.GET.get('page', '') #몇번째 페이지인지 받아옴
    book_list = paginator.get_page(page) #posts


    return render(request, 'category.html', {'book_list':book_list, 'search':search, 'major':major})
    
#detail 페이지 구현
#detail page
def detail(request, id):
    book = get_object_or_404(BookClassInfo, id = id)
    return render(request, 'detail.html', {'book':book})

#borrow 기능
def borrow(request, id):
    if not request.user.is_active:
        return HttpResponse('로그인 해주세요')
    
    book = get_object_or_404(BookClassInfo, id = id)
    user = request.user

    if book.borrows.filter(id = user.id).exists():
        book.borrows.remove(user)
        book.stock += 1
        book.save()

    else:
        book.borrows.add(user)
        book.stock -= 1
        book.save()
        
        if book.stock == 0:
            return HttpResponse('재고가 없습니다.')
    return redirect('detail', id = book.id)

#찜하기
def wish(request, id):
    if not request.user.is_active:
        return HttpResponse('로그인 해주세요')
    
    book = get_object_or_404(BookClassInfo, id = id)
    user = request.user

    if book.wishes.filter(id = user.id).exists():
        book.wishes.remove(user)

    else:
        book.wishes.add(user)

    return redirect('detail', id = book.id)