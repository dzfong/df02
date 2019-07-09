from django.contrib import admin
from  django.urls import path
from . import views


# 应用命名空间
app_name = 'booktest'

# 应用的urls文件
urlpatterns = [
	path('', views.index),				# 配置应用的首页面的url
	path('welcome/', views.welcome, name = 'welcome'),	# 配置应用的其他页面的url
	path('books/', views.books),
	path('books/<int:bid>/', views.detail),
	path('create/', views.create, name = 'cre'),
	path('delete<int:bid>/', views.delete, name='delete'),
	path('showarg<int:num>/', views.show_arg),
	path('login/', views.login),
	path('login_check/', views.login_check, name ='log'),
	path('web', views.search, name='search'),			# 查询
	path('rev/', views.rev, name='rev'),			# 重定向到 error/100/200
	path('error/<int:a>/<int:b>/', views.error, name='loose'),
	path('page/<int:page>',views.page),		# 默认值设置，需要设置俩个URL
	path('page/', views.page),					# 默认值设置
	path('extends', views.extends, name='extends'),		# 模板继承
	path('cookie_set/', views.cookie_set, name='cookie'),
	path('set_session', views.set_session),
	path('get_session', views.get_session),
	path('change_pwd', views.change_pwd),
	path('change_pwd_action', views.change_pwd_action, name='pwd'),	#密码处理
	path('verify_code/', views.verify_code),					# 验证码
	path('upload_pic', views.upload_pic),
	path('upload_handle', views.upload_handle, name='upload_handle'),
	path('show_books/', views.show_books),						# 分页展示的默认页
	path('show_books/<int:pindex>/', views.show_books, name='showpage'),	# 分页展示
	path('csstest/', views.csstest),						# 样式表测试
	path('default', views.default, name='default'),			# 首页布局
	path('mobile',views.mobile, name='moblie'),				# 移动布局测试
	path('rem', views.rem, name="rem"),						# 移动首页
	path('jquerytest', views.jquerytest),					# jquery 测试
	path('jsontest', views.jsontest),						# ajax请求处理
]	