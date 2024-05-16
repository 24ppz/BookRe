from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                        # 主页
    path('detail/', views.bookdetail, name='detail'),           # 详细页面
    path('addtocart/', views.addtocart, name='addtocart'),      # 添加到购物车
    path('getcartnum1/', views.getcartnum, name='getcartnum'),  # 添加到购物车
    path('showcart/', views.showcart, name='showcart'),         # 展示购物车
    path('addbooks1/', views.add_books, name='addbooks'),       # 书籍数目+1
    path('subbooks1/', views.sub_books, name='subbooks'),       # 书籍数目-1
    path('deletcart/', views.delcart, name='deletcart'),        # 删除购物车的商品
    path('cash_pay/', views.cash_payment, name='cash_pay'),     # 支付
    path('comment/',views.comment,name='comment'),              # 评论
    path('search/',views.search,name='search'),
    path('sortall/',views.sort_all,name='sortall')
]

app_name='index'
