
# 模板包 封装好的。不用分步骤去使用模板文件
#  redirect 网页跳转包
#  render 是渲染
#  reverse 反向解析
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
# 导入加载模板文件包
from django.template import loader
# 导入定义模板上下文的包
from django.template import RequestContext
# 导入模型类包
from .models import BookInfo, BookInfoManager, PicTest
# 时间包
from datetime import date
# 重定向包
from django.http import HttpResponseRedirect
# 路径分离
from django.urls import resolve
# 导入配置项
from django.conf import settings
# 分页包
from django.core.paginator import Paginator

# Create your views here.


#=================================================
#
#	基础篇
#	
#==================================================



# 1、定义视图函数，和M 和T 进行交互
# 2、进行url配置， 建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
# 就是普通的函数，但是必须有个 request 参数
def index(request):
	'''
		进行处理，请求和返回，和M 和T 进行交互
	'''
	# HttpResponse 必须要导入库
	# return HttpResponse("hello world")

	# # 使用模板文件
	# # 1、加载模板文件,	返回模板对象
	# temp = loader.get_template('booktest/index.html')

	# # 2、定义模板上下文， 给模板文件传递数据
	# # 需要导入包。 RequestContext
	# # 第一个参数是request 第二个参数是 传递的数据 是个字典，键值队
	# context = RequestContext(request, {'':''})

	# # 3、模板渲染 ： 产生标准的html内容
	# res_html = temp.render(context)
	
	# # 4、返回给浏览器
	# return HttpResponse(res_html)
	
	return render(request, 'booktest/index.html', {'content': 'hello world!','list': list(range(1,10))})


# /csstest
def csstest(request):
	''' css样式测试 '''
	return render(request, "booktest/csstest.html")

# /default
def default(request):
	''' 首页布局  '''
	return render(request, "booktest/default.html")

# /mobile
def mobile(request):
	''' 移动布局 '''
	return render(request, "booktest/mobile.html")

# /rem
def rem(request):
	''' 移动首页 '''
	return render(request, "booktest/rem.html")

# /jquerytest
def jquerytest(request):
	''' 移动首页 '''
	return render(request, "booktest/jquerytest.html")

# /jsontest
def jsontest(request):
	''' ajax请求处理 ---返回json数据 '''
	return JsonResponse({'res':1})

# /bootstrap
def bootstrap(request):
	''' bootstrap的实例 '''
	return render(request, "booktest/bootstrap.html")


# 由于导入了 render 包，模板文件就不用像index那么去写。 直接调用
def welcome(request):

	http_list = [
		'<h1>完整的URL地址:&nbsp;<span style="color:red">%s</span></h1>' % request.get_raw_uri(),
		'<h1>完整路径:&nbsp;<span style="color:red">%s</span></h1>' % request.get_full_path(),
	]

	return HttpResponse(http_list)




# 查找书籍列表
def books(request):

	# 获取图书列表, 通过model获取
	books = BookInfo.objects.all()

	return render(request, 'booktest/books.html', {'books': books })


# 查找图书相关英雄信息
def detail(request, bid):

	# 根据bid查询图书信息
	book = BookInfo.objects.get(id=bid)

	# 查询和book关联的英雄信息
	heros = book.heroinfo_set.all()

	# 使用模板 传递数据
	return render(request, 'booktest/detail.html', {'book': book, 'heros':heros})



#  新增页面
def create(request):
	''' 新增一本图书 '''

	# 1、创建BookInfo对象
	# b = BookInfo()
	# b.btitle = '新流星蝴蝶剑'
	# b.bpub_date = date(1990,1,1)
	# # 2、保存进数据库
	# b.save()
	# # 3、返回应答, 让浏览器再访问 /books
	# # return HttpResponse('OK')
	
	b = BookInfo.objects.create_book('笑傲江湖', '1990-1-14')
	# 网页重定向
	return HttpResponseRedirect('/books')



def delete(request, bid):
	''' 删除点击的图书 '''

	# 1、通过bid获取图书对象
	book = BookInfo.objects.get(id=bid)
	# 2、删除
	book.delete()
	# 3、重定向，让浏览器还是访问 /books
	return HttpResponseRedirect('/books')
	


# 捕获url参数
def show_arg(request, num):
	return HttpResponse(num)



# 查询
# 
def search(request):
	''' 通过url中的get属性查询 '''
	search = request.GET.get('query')
	return HttpResponse('<h1>{}</h1>'.format(search))



# 默认值设置
def page(request, page=100):
	return HttpResponse('<h1>{}</h1>'.format(page))




# 继承母版
def extends(request,):
	context = {	
		'age': 18,
		'books': ['html', 'python', 'django', 'css', 'javascript'],
		'turorial':{
			'title':'html',
			'author':'chan',
			'price': 99.00
		},
		'empty': '空的列表',
		'value': 100,
		'teacher':{
			'english':{
				'type': 'us'
			},
		},
	}
	return render(request, 'booktest/extends.html', context=context)








#================================================
#
#
#	反向解析  (动态地址)
#	
#================================================
#
# 用到三个包，一个重定向redireect  一个反向解析 reverse  一个路径分离 resolve




# 反向解析
# 从首页跳转到 /error/
def error(request, a, b):
	sum = a + b
	return HttpResponse('<h1 style="color:red;"">{}</h1>'.format(request.path))


# 反向解析重定向
# /rev  重定向到 /error/100/200
def rev(request):
	# 获取路径 
	path = request.path
	# 路径分离 得到项目urls.py中应用名namespace
	current_namespace = resolve(path).namespace
	# 获取完整的url
	url = reverse('{}:loose'.format(current_namespace), kwargs={'a':100, 'b':200})
	return redirect(url)







#============================================================================
#
#		登录页面
#		
#============================================================================
#
#



# 装饰器函数
def login_required(view_func):
	''' 登录判断装饰器 '''
	def wrapper(request, *view_args, **view_kwargs):
		# 判断用户是否登录
		if request.session.has_key('islogin'):
			# 用户已登录, 调用对应的视图
			return view_func(request,*view_args, **view_kwargs)
		else:
			# 用户未登录，跳转到首页
			return redirect('/login')

	return wrapper




# /login
def login(request):
	'''显示登录页面'''
	# 判断用户是否登录
	if request.session.has_key('islogin'):
		# 用户已登录，跳转到修改密码页面
		return redirect('/change_pwd')
	else:
		# 用户登录
		# 获取cookie username
		if 'username' in request.COOKIES:
			# 获取记住的用户名
			username = request.COOKIES['username']
		else:
			username = ''

		return render(request, 'booktest/login.html', {'username': username})



# 登录检验跳转
def login_check(request):
	'''登录校验视图'''

	# 1、 获取提交的用户名和密码
	# print(type(request.POST))
	# print(request.POST)
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')

	# 2、 获取用户输入的验证码 
	user_vcode = request.POST.get('vcode')
	# 获取sessin中保存的验证码
	session_vcode = request.session.get('verifycode')
	# 进行验证码校验
	if user_vcode != session_vcode:
		# 不正确，跳转到登录页面
		return redirect("/login")

	# 3、 进行登录的校验
	# 根据用户名和密码查找数据库
	# 模拟： admin 123
	if username == 'admin' and password == '123':
		# 用户名和密码正确，跳转到修改密码页面
		response =  redirect('/change_pwd')
		# 判断是否需要记住用户名
		if remember == 'on':
			# 设置cookie 过期时间
			response.set_cookie('username', username, max_age=7*24*3600)
		# 记住用户登录状态
		# 只有session中有 islogin， 就认为用户已登录
		request.session['islogin'] = True
		# 设置session过期时间，关闭浏览器就过期
		request.session.set_expiry(0)
		# 记住用户登录名
		request.session['username'] = username
		return response	
	else:
		# 不正确，跳转到登录页面
		return redirect("/login")



#
# 登录后跳转修改密码界面
# 装饰器 判断用户是否登录。
@login_required
def change_pwd(request):
	''' 修改密码 '''
	return	render(request, 'booktest/change_pwd.html')



# /change_pwd_action   别名 pwd
## 修改密码处理
# 装饰器 判断用户是否登录。
@login_required
def change_pwd_action(request):
	''' 模拟密码处理 '''
	# 1、获取新密码
	pwd = request.POST.get('pwd')
	# 获取用户名
	username = request.session.get('username')
	# 2、实际开发的时候：修改对应数据库中的内容
	# 3、返回一个应答
	return HttpResponse('%s修改密码为：%s'%(username,pwd))









#=======================================================================================================
#
# cookie  session
# 
# =====================================================================================================
# 




# /cookie_set
def cookie_set(request):
	''' 
		设置cookie信息
	'''
	response = HttpResponse("设置cookie，在表头查看")
	# 设置一个cookie信息，名字为name,值为value
	# max_age=14*24*3600 设置多少秒过期； expires = datetime.now() + timedelta(days=14) 两周过期
	response.set_cookie('name', 'value')		
	#  返回response . request.COOKIES 读取cookie
	print(request.COOKIES)
	return response



# /set_session
def set_session(request):
	'''
		设置session
	'''
	request.session['username'] = 'admin'
	request.session['age'] = 18
	return HttpResponse('设置session')



# /get_session
def get_session(request):
	'''
		读取session
	'''
	username = request.session['username']
	age = request.session['age']
	return HttpResponse(username+':'+str(age))









# ========================================================================================
#
##   验证
#
#=========================================================================================

# 验证码
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

def verify_code(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('c:\Windows\Fonts\msyh.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, -2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    buf = BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')



#=================================
#
#
#	上传图片
#	
#=================================
#导入2个包		一个settings  一个视图模型
#
#
# https://docs.djangoproject.com/zh-hans/2.2/topics/http/file-uploads/

def upload_pic(request):
	'''显示上传图片页面'''

	return render(request,'booktest/upload_pic.html')



def upload_handle(request):
	''' 上传图片处理 '''

	#1、获取上传文件的处理对象(根据字典里的名字获取)
	pic = request.FILES['pic']
	# print(pic.name)		# 打印名称
	# pic.chunks()			# 分块返回内容

	#2、创建一个文件用来保存
	# 通过引入的settings拿到配置项，拼出路径
	save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT, pic.name)

	with open(save_path, 'wb') as f:
		#3、获取上传文件的内容并写到创建的文件中
		for content in pic.chunks():
			f.write(content)
	
	#4、在数据库中保存上传记录
	PicTest.objects.create(gpic='booktest/%s'%pic.name)

	#5、返回
	return HttpResponse("ok")






# ===============================
# 
# 	分页
# 	
# ===============================
#  导包 from django.core.paginator import Paginator
#  
#  https://docs.djangoproject.com/zh-hans/2.2/topics/cache/
#  

# /show_books 
# 前端访问的时候，需要传递页码
# 默认页码为1，在urls中需要定义 show_books/ ；show_books/<int:pindex>/
def show_books(request, pindex=1):
	'''分页显示'''

	# 1、查询所有书籍的名称
	books = BookInfo.objects.all()

	# 2、分页，每页显示5条数据
	p = Paginator(books, 5)
	
	# 3、获取第pindex页的内容
	# page是Page类的实例对象

	page = p.page(pindex)

	# 返回
	return render(request, 'booktest/show_books.html', {'page':page})

