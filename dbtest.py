from mongoengine import *

connect ('testdb' , host = '101.132.46.146' , port = 27017 )

class Students(Document):
    name = StringField()
    age = StringField()

#查询数据
# a = Students(name='zhangtao')
# a.save()

kingname_list = Students.objects(name='zhangtao')
for kingname in kingname_list:
    kingname.delete()