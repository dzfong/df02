# 自定义过滤器
# 过滤器其实就是python函数

from django.template import Library

# 创建一个Library类的对象
register = Library()



def mod(num):
	'''判断num是否为偶数'''
	return num%2 == 0


# 用Library实例去注册它
register.filter('mm', mod)