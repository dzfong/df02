from django.db import models

# Create your models here.
# 


# 自定义图书模型管理器类
class BookInfoManager(models.Manager):
	''' 图书模型管理器 '''
	# 1、改变查询的结果集
	def all(self):
		# 1、调用父类的all， 获取所有数据
		books = super().all()		# 这是一个 QuerySet
		# 2、对数据进行过滤
		books = books.filter(isDelete=False)
		# 3、 返回books
		return books

	# 2、封装函数： 操作模型类对应的数据表(增删改查)
	def create_book(self, btitle, bpub_date):
		# 创建一个图书对象 
		# book = BookInfo()
		# 每一个模型类的对象都有一个模型类 model ; 即使模型类的名称改变了，也不影响封装的函数
		# 创建一个模型类对象
		model_class = self.model
		book = model_class()
		book.btitle = btitle
		book.bpub_date = bpub_date
		# 保存到数据库
		book.save()
		# 返回对象
		return book



# 一类
# 图书类
class BookInfo(models.Model):
	'''
		图书模型类
	'''

	# 书名，字符串类型，长度20
	btitle = models.CharField('书名',max_length=20)
	# 出版日期, 日期类型
	bpub_date = models.DateField()
	# 阅读量
	bread = models.IntegerField(default=0)
	# 评论量
	bcomment = models.IntegerField(default=0)
	# 删除标记
	isDelete = models.BooleanField(default=False)

	# 重写 str 方法 ; 后台管理里面直接显示 图书名称 btitle
	def __str__(self):
		return self.btitle

	# 自定义一个函数 比如归类, 可以在后天添加自定义类
	def title(self):
		return self.btitle
	# title在后台显示的别名
	title.short_description = '自定义书名'



	## 增加类方法 （通常不会放在这里，这里是定义类，而不是操作方法；一般会放在 图书模型管理器中）
	# @classmethod
	# def create_book(cls, btitle, bpub_date):
	# 	# 1、创建一个图书对象
	# 	obj = cls()
	# 	obj.btitle = btitle
	# 	obj.bpub_date = bpub_date
	# 	# 2、 保存进数据库
	# 	obj.save()
	# 	# 3、 返回obj
	# 	return obj


	#  实例图书模型管理器
	objects = BookInfoManager()


	class Meta():
		''' 元选项： 改名等用处 '''
		# 指定BookInfo生成的数据表名为 bookinfo，而不是 booktest_bookinfo 
		db_table = 'bookinfo'
		# 后台表显示的别名
		verbose_name_plural = '图书'
		# 后台表数据的别名
		verbose_name = '图书列表'
		# 排序
		ordering = ['id'] 



# 多类
# 英雄人物类
class HeroInfo(models.Model):
	'''
		英雄人物模型表

		名 		hname
		性别	hgender
		年龄	hage
		备注	hcomment
		关系属性 book 建立图书类和英雄人物类之间的一对多关系
	'''

	choices = [
		('male', '男'),
		('female', '女')	
	]


	# 名称
	hname = models.CharField('名称',max_length=20,unique=True)
	# 性别，bool类型，指定默认值，False 代表男
	hgender = models.CharField(verbose_name='性别',max_length=10,choices=choices,default='male')	

	# 定义关系属性，一类的类名
	# 关系属性对应表的字段名 格式： 关系属性名_id  表名  hbook_id
	# 2.0版本后 一定要设置参数  on_delete ，不然会报错
	hbook = models.ForeignKey('BookInfo', verbose_name='书名' , on_delete=models.CASCADE)				# h.hbook = b  b是BookInfo()类属性;
	# 备注
	hcomment = models.TextField(verbose_name='介绍')
	# 删除标记
	isDelete = models.BooleanField('标记',default=False)

	# 重写 str 方法 ; 后台管理里面直接显示 英雄名称 hname
	def __str__(self):
		return self.hname



#
class AreaInfo(models.Model):
	'''地区模型类'''
	# 地区名称
	atilte = models.CharField(max_length=20,db_column='title')
	# 关系属性，代表当前地区的父级地区
	# 自关联
	aparent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)






class PicTest(models.Model):
	''' 上传图片 '''
	gpic = models.ImageField(upload_to='booktest')