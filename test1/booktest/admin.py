from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, PicTest

# Register your models here.




# 编辑页面关联对象（块的嵌入方式）
class BookStackedInline(admin.StackedInline):
	# 多类
	model = HeroInfo

	# 修改默认的3格空行为1格
	extra = 1 	


# 表格的嵌入方式
class BookTabularInline(admin.TabularInline):
	# 多类
	model = HeroInfo

	# 修改默认的3格空行为1格
	extra = 1 	




# 自定义模型管理类
# 通常是显示类名+Admin
# 继承自 admin.ModelAdmin
class BooInfoAdmin(admin.ModelAdmin):
	'''
		图书模型管理类
	'''
	#显示列表， 参数名称不可改变
	list_display = ['id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'isDelete', 'title']

	# 指定每页显示10行
	list_per_page = 10

	# 下方显示 删除框
	actions_on_bottom = True

	# 上方不显示 删除框
	actions_on_top = False

	# 列表页右侧过滤栏
	list_filter = ['btitle']

	# 列表页上方的搜索框
	search_fields = ['btitle']

	# 编辑页选项，显示字段顺序
	# fields = ['bpub_date','btitle']
	
	# 关联对象, 块
	# inlines = [BookStackedInline]
	# 关联对象, 表格
	inlines = [BookTabularInline]


class HeroInfoAdmin(admin.ModelAdmin):
	'''
		英雄模型管理类
	'''
	list_display = ['hname', 'hgender', 'hcomment', 'hbook', 'isDelete']


# 注册模型类
# 加入属性：要显示的自定义模型管理类
admin.site.register(BookInfo,BooInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(PicTest)
