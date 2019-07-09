from django.http import HttpResponse


class BlockedIPSMiddleware(object):
	'''中间件类'''

	EXCLUDE_IPS = ['192.168.18.4']


	# 新版本的中间件设置 ：中间件类必须接受一个get_response参数
	def __init__(self, get_response):
		''' 服务器重启之后，接收第一个请求时调用'''
		self.get_response = get_response

	def __call__(self, request):
		''' 调用函数或类，其实调用的就是__call__方法。 '''
		return self.get_response(request)



	def process_view(self, request, view_func, *view_args, **view_kwargs):
		''' 视图函数调用之前会调用 '''

		# 获取客户端浏览器ip地址
		user_ip = request.META['REMOTE_ADDR']

		# 判断客户端ip地址是否在禁止列表中
		if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
			return HttpResponse('<h1>禁止访问此网站</h1>')
