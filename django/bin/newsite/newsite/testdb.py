# -*- coding:utf-8 -*-

from django.http import HttpResponse
from TestModel.models import eaxm_db

def testdb(request):
	print('testdb')
	test1 = eaxm_db(name='runoob', address='adress1', phone='123456789')
	test1.save()
	return HttpResponse("<p>添加数据成功</p>")

def selectdb(request):
	print('selectdb')

	response = ""
	response1 = ""


	list = eaxm_db.objects.all()
	# response2 = eaxm_db.objects.filter(id = 1)
	# response3 = eaxm_db.objects.get(id = 1)

	# eaxm_db.objects.order_by('name')[0:2]

	# eaxm_db.objects.order_by("id")

	# eaxm_db.objects.filter(name = "runoob").order_by("id")

	for var in list:
		response1 += var.name + " "

	response = response1
	return HttpResponse("<p>" + response + "</p>")	

def updatedb(request):
	# test1 = eaxm_db.objects.get(id = 1)
	# test1.name = 'google'
	# test1.save()

	eaxm_db.objects.filter(name = 'runoob2').update(name = 'google2')

	return HttpResponse("<p>添加数据成功</p>")

def deldb(request):
	# test = eaxm_db.objects.get(id = 1)
	# test.delete()

	# eaxm_db.objects.filter(id = 2).delete()

	eaxm_db.objects.all().delete()

	return HttpResponse("<p>删除成功</p>")