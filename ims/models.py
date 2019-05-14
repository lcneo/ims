# from django.db import models
from ims.models_struct import *
from ims.db import execute,add_del_update
# Create your models here.
# class user(models.Model):
#	 u_name = models.CharField(max_length=10)
#	 u_password = models.CharField(max_length=255)
#	 class Meta:
#		 db_table='user'

class m_user(field_user):
	"""
	user model
	"""
	def __init__(self, account:str, password:str):
		self.account = account
		self.password = password

	#获取帐号的密码
	def get_password(self):
		sql = """SELECT * FROM user WHERE account='{account}'
		""".format(account=self.account)
		req = execute(sql)
		if req:
			req = req[0][2]
		return req


	#查找账号是否存在
	def find_account(self)->bool:
		""" 存在:True
			不存在:Flase
		"""
		sql = """SELECT * FROM user WHERE account='{account}'
		""".format(account=self.account)
		if execute(sql):
			req = True
		else:
			req = False
		return req

	#修改密码
	def update_password(self)->bool:
		"""将密码修改为类变量中的值"""
		sql = """
		UPDATE user SET password='{pw}' WHERE account='{ac}' 
		""".format(pw=self.password, ac=self.account)
		return add_del_update(sql)

	def add_account(self)->bool:
		"""将类变量中的帐号添加"""
		sql = """INSERT INTO user(account, password) VALUES("{ac}","{pw}")""".format(ac=self.account, pw=self.password)
		return add_del_update(sql)

	def del_account(self)->bool:
		"""从数据库中删除类变量中的帐号"""
		sql = """DELETE  FROM user WHERE account='{account}'
		""".format(account=self.account)
		return add_del_update(sql)

	def account_list()->list:
		"""返回数据库中所有的帐号"""
		sql = "SELECT * FROM user"
		req = execute(sql)
		aclist = []
		if req:
			for ac in req:
				aclist.append(ac[1])
		else:
			aclist = None
		return aclist


class m_collage(field_collage):
	"""docstring for m_collage"""
	def __init__(self, collage_no, collage_name, dean, tel, address):
		self.collage_no = collage_no
		self.collage_name = collage_name
		self.dean = dean
		self.tel = tel
		self.address = address
		
	def add_collage(self)->bool:
		""""""
		sql = """INSERT INTO collage(collage_no, collage_name, dean, tel, address) VALUES ("{collage_no}","{collage_name}","{dean}","{tel}","{address}")""".format(collage_no = self.collage_no
																									,collage_name = self.collage_name
																									,dean = self.dean
																									,tel = self.tel
																									,address = self.address)
		return add_del_update(sql)

	def del_collage(self):
		sql = """DELETE  FROM collage WHERE collage_no='{collage_no}'
		""".format(collage_no=self.collage_no)
		return add_del_update(sql)

	def update_collage(self, change_no=None):
		origin_no = self.collage_no
		if change_no:
			self.collage_no = change_no
		sql = """UPDATE collage SET collage_no = "{collage_no}", collage_name = "{collage_name}", dean = "{dean}", tel="{tel}", address = "{address}" WHERE collage_no = "{origin_no}" """.format(collage_no = self.collage_no
																									,collage_name = self.collage_name
																									,dean = self.dean
																									,tel = self.tel
																									,address = self.address
																									,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM collage WHERE (collage_no LIKE "%{search_str}%") or (collage_name LIKE "%{search_str}%") or (dean LIKE "%{search_str}%") or (tel LIKE "%{search_str}%") or (address LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM collage"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ("collage_no", "collage_name", "dean", "tel", "address")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("collage_no", "collage_name", "dean", "tel", "address")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

class m_department(field_department):
	"""docstring for m_collage"""
	def __init__(self, department_no, name, tro_num, class_num, collage_no):
		self.department_no = department_no
		self.name = name
		self.tro_num = tro_num
		self.class_num = class_num
		self.collage_no = collage_no

		
	def add_department(self)->bool:
		""""""
		sql = """INSERT INTO department(department_no, name, tro_num, class_num, collage_no) VALUES ("{department_no}", "{name}", {tro_num}, {class_num}, "{collage_no}")""".format(department_no = self.department_no
																									,name = self.name
																									,tro_num = self.tro_num
																									,class_num = self.class_num
																									,collage_no = self.collage_no)
		return add_del_update(sql)

	def del_department(self):
		sql = """DELETE  FROM department WHERE department_no='{department_no}'
		""".format(department_no=self.department_no)
		return add_del_update(sql)

	def update_department(self, change_no=None):
		origin_no = self.department_no
		if change_no:
			self.department_no = change_no
		sql = """UPDATE department SET department_no = "{department_no}", name = "{name}", tro_num = {tro_num}, class_num={class_num}, collage_no = "{collage_no}" WHERE department_no = "{origin_no}" """.format(department_no = self.department_no
																									,name = self.name
																									,tro_num = self.tro_num
																									,class_num = self.class_num
																									,collage_no = self.collage_no
																									,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM department WHERE (department_no LIKE "%{search_str}%") or (name LIKE "%{search_str}%") or (tro_num LIKE "%{search_str}%") or (class_num LIKE "%{search_str}%") or (collage_no LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM department"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ( "department_no", "name", "tro_num", "class_num", "collage_no")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("department_no", "name", "tro_num", "class_num", "collage_no")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]
class m_class(field_class):
	"""docstring for m_collage"""
	def __init__(self, class_no, class_name, class_size, professional, department_no):
		self.class_no = class_no
		self.class_name = class_name
		self.class_size = class_size
		self.professional = professional
		self.department_no = department_no

		
	def add_class(self)->bool:
		""""""
		sql = """INSERT INTO class(class_no, class_name, class_size, professional, department_no) VALUES ("{class_no}", "{class_name}", "{class_size}", "{professional}", "{department_no}")""".format(class_no = self.class_no
																									,class_name = self.class_name
																									,class_size = self.class_size
																									,professional = self.professional
																									,department_no = self.department_no)
		return add_del_update(sql)

	def del_class(self):
		sql = """DELETE  FROM class WHERE class_no='{class_no}'
		""".format(class_no=self.class_no)
		return add_del_update(sql)

	def update_class(self, change_no=None):
		origin_no = self.class_no
		if change_no:
			self.class_no = change_no
		sql = """UPDATE class SET class_no = "{class_no}", class_name = "{class_name}", class_size = {class_size}, professional="{professional}", department_no = "{department_no}" WHERE class_no = "{origin_no}" """.format(class_no = self.class_no
																									,class_name = self.class_name
																									,class_size = self.class_size
																									,professional = self.professional
																									,department_no = self.department_no
																									,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM class WHERE (class_no LIKE "%{search_str}%") or (class_name LIKE "%{search_str}%") or (class_size LIKE "%{search_str}%") or (professional LIKE "%{search_str}%") or (department_no LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM class"
		return execute(sql)
	def req2dic(value:tuple)->dict:
		key = ("class_no", "class_name", "class_size", "professional", "department_no")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("class_no", "class_name", "class_size", "professional", "department_no")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

class m_tro(field_tro):
	"""docstring for m_collage"""
	def __init__(self, tro_no, tro_name, tro_size, department_no):
		self.tro_no = tro_no
		self.tro_name = tro_name
		self.tro_size = tro_size
		self.department_no = department_no
		
	def add_tro(self)->bool:
		""""""
		sql = """INSERT INTO tro(tro_no, tro_name, tro_size, department_no) VALUES ("{tro_no}","{tro_name}",{tro_size},"{department_no}")""".format(tro_no = self.tro_no
																									,tro_name = self.tro_name
																									,tro_size = self.tro_size
																									,department_no = self.department_no)
		return add_del_update(sql)

	def del_tro(self):
		sql = """DELETE  FROM tro WHERE tro_no='{tro_no}'
		""".format(tro_no=self.tro_no)
		return add_del_update(sql)

	def update_tro(self, change_no=None):
		origin_no = self.tro_no
		if change_no:
			self.tro_no = change_no
		sql = """UPDATE tro SET tro_no = "{tro_no}", tro_name = "{tro_name}", tro_size = {tro_size}, department_no="{department_no}" WHERE tro_no = "{origin_no}" """.format(tro_no = self.tro_no
																									,tro_name = self.tro_name
																									,tro_size = self.tro_size
																									,department_no = self.department_no
																									,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM tro WHERE (tro_no LIKE "%{search_str}%") or (tro_name LIKE "%{search_str}%") or (tro_size LIKE "%{search_str}%") or (department_no LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM tro"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ("tro_no", "tro_name", "tro_size", "department_no")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("tro_no", "tro_name", "tro_size", "department_no")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

class m_student(field_student):
	"""docstring for m_collage"""
	def __init__(self, student_no, student_name, gender, birthplace, class_no):
		self.student_no = student_no
		self.student_name = student_name
		self.gender = gender

		self.birthplace = birthplace
		self.class_no = class_no

	def add_student(self)->bool:
		""""""
		sql = """INSERT INTO student(student_no, student_name, gender, birthplace, class_no) VALUES ("{student_no}", "{student_name}", "{gender}", "{birthplace}", "{class_no}")""".format(student_no=self.student_no
																																								,student_name=self.student_name
																																								,gender=self.gender
																																							
																																								,birthplace=self.birthplace
																																								,class_no=self.class_no)
		return add_del_update(sql)

	def del_student(self):
		sql = """DELETE  FROM student WHERE student_no='{student_no}'
		""".format(student_no=self.student_no)
		return add_del_update(sql)

	def update_student(self, change_no=None):
		origin_no = self.student_no
		if change_no:
			self.student = change_no
		sql = """UPDATE student SET student_no = "{student_no}", student_name = "{student_name}", gender = "{gender}", birthplace="{birthplace}", class_no = "{class_no}" WHERE student_no = "{origin_no}" """.format(student_no=self.student_no
																																								,student_name=self.student_name
																																								,gender=self.gender
																																								
																																								,birthplace=self.birthplace
																																								,class_no=self.class_no
																																								,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM student WHERE (student_no LIKE "%{search_str}%") or (student_name LIKE "%{search_str}%") or (gender LIKE "%{search_str}%")  or (birthplace LIKE "%{search_str}%") or (class_no LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM student"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ("student_no", "student_name", "gender", "birthplace", "class_no")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("student_no", "student_name", "gender", "birthplace", "class_no")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

class m_teacher(field_teatcher):
	"""docstring for m_collage"""
	def __init__(self, teacher_no, teacher_name, gender, post, tro_no):
		self.teacher_no = teacher_no
		self.teacher_name = teacher_name
		self.gender = gender
		self.post = post
		self.tro_no = tro_no
		
	def add_teacher(self)->bool:
		""""""
		sql = """INSERT INTO teacher(teacher_no, teacher_name, gender, post, tro_no) VALUES ("{teacher_no}", "{teacher_name}", "{gender}", "{post}", "{tro_no}")""".format(teacher_no = self.teacher_no
																									,teacher_name = self.teacher_name
																									,gender = self.gender
																									,post = self.post
																									,tro_no = self.tro_no)
		return add_del_update(sql)

	def del_teacher(self):
		sql = """DELETE  FROM teacher WHERE teacher_no='{teacher_no}'
		""".format(teacher_no=self.teacher_no)
		return add_del_update(sql)

	def update_teacher(self, change_no=None):
		origin_no = self.teacher_no
		if change_no:
			self.teacher_no = change_no
		sql = """UPDATE teacher SET teacher_no = "{teacher_no}", teacher_name = "{teacher_name}", gender = "{gender}", post="{post}", tro_no = "{tro_no}" WHERE teacher_no = "{origin_no}" """.format(teacher_no = self.teacher_no
																									,teacher_name = self.teacher_name
																									,gender = self.gender
																									,post = self.post
																									,tro_no = self.tro_no
																									,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM teacher WHERE (teacher_no LIKE "%{search_str}%") or (teacher_name LIKE "%{search_str}%") or (gender LIKE "{search_str}") or (post LIKE "%{search_str}%") or (tro_no LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM teacher"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ("teacher_no", "teacher_name", "gender", "post", "tro_no")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("teacher_no", "teacher_name", "gender", "post", "tro_no")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

class m_course(field_course):
	"""docstring for m_collage"""
	def __init__(self, course_no, course_name, period, credit, teacher_no):
		self.course_no = course_no
		self.course_name = course_name
		self.period = period
		self.credit = credit
		self.teacher_no = teacher_no
		
	def add_course(self)->bool:
		""""""
		sql = """INSERT INTO course(course_no, course_name, period, credit, teacher_no) VALUES ("{course_no}", "{course_name}", {period}, {credit}, "{teacher_no}")""".format(course_no = self.course_no
																									,course_name = self.course_name
																									,period = self.period
																									,credit = self.credit
																									,teacher_no = self.teacher_no)
		return add_del_update(sql)

	def del_course(self):
		sql = """DELETE  FROM course WHERE course_no='{course_no}'
		""".format(course_no=self.course_no)
		return add_del_update(sql)

	def update_course(self, change_no=None):
		origin_no = self.course_no
		if change_no:
			self.course_no = change_no
		sql = """UPDATE course SET course_no = "{course_no}", course_name = "{course_name}", period = {period}, credit = {credit}, teacher_no = "{teacher_no}" WHERE course_no = "{origin_no}" """.format(course_no = self.course_no
																									,course_name = self.course_name
																									,period = self.period
																									,credit = self.credit
																									,teacher_no = self.teacher_no
																									,origin_no = origin_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM course WHERE (course_no LIKE "%{search_str}%") or (course_name LIKE "%{search_str}%") or (period LIKE "%{search_str}%") or (credit LIKE "%{search_str}%") or (teacher_no LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM class"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ("course_no", "course_name", "period", "credit", "teacher_no")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("course_no", "course_name", "period", "credit", "teacher_no")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

class m_source(field_source):
	"""docstring for m_collage"""
	def __init__(self, student_no, course_no, source):
		self.student_no = student_no
		self.course_no = course_no
		self.source = source
		
	def add_source(self)->bool:
		""""""
		sql = """INSERT INTO source(student_no, course_no, source) VALUES ("{student_no}", "{course_no}", "{source}")""".format(student_no = self.student_no
																									,course_no = self.course_no
																									,source = self.source)
		return add_del_update(sql)

	def del_source(self):
		sql = """DELETE  FROM source WHERE student_no='{student_no}' AND course_no="{course_no}"
		""".format(student_no=self.student_no, course_no=self.course_no)
		return add_del_update(sql)

	def update_source(self):

		sql = """UPDATE source SET source = "{source}" WHERE student_no = "{student_no}" AND course_no="{course_no}" """.format(source=self.source, student_no=self.student_no, course_no=self.course_no)
		return add_del_update(sql)

	def search(search_str:str)->tuple:
		sql = """SELECT * FROM source WHERE (student_no LIKE "{search_str}") or (course_no LIKE "{search_str}") or (source LIKE "%{search_str}%")""".format(search_str=search_str)
		return execute(sql)

	def list_all():
		sql = "SELECT * FROM source"
		return execute(sql)

	def req2dic(value:tuple)->dict:
		key = ("student_no", "course_no", "source")
		return dict(zip(key, value))

	def req2list(values:tuple)->list:
		def req2dic(value:tuple)->dict:
			key = ("student_no", "course_no", "source")
			return dict(zip(key, value))
		return [dict(req2dic(value)) for value in values]

if __name__ == '__main__':	
	# m_user("admin","123456")
	# print(m_user("admin","123456").get_password())
	# print(m_user("admin", "123").find_account())
	# print(m_user.account_list())
	# print(m_user("neoo","1233").del_account())
	# print(m_user("neo","neoneoneo").update_password())
	# print(m_user("No","1233").add_account())
	# print(m_user.get_password("neo"))
	# c = m_collage("7","北京大学","老bai","1234422","12331")
	# print(c.add_collage())
	# print(c.update_collage("9"))
	# print(m_collage.search("2"))
	# md = m_department("306","信息安全系", 0, 1, "3")
	# print(md.add_department())
	# print(md.del_department())
	# print(md.update_department())
	# print(m_department.list_all())
	# c = m_class("30202", "自动化二班", 0, "自动化", "302")
	# c.add_class()
	# print(c.update_class()
	# print(m_class.list_all())
	# t = m_tro("30102", "信息安全教研室", 1, "301")
	# print(t.add_tro())
	# print(t.del_tro())
	# print(t.update_tro())
	# print(m_tro.search("30102"))
	# s = m_student("30102002","小明", "女", "2019-05-01 00:00:00", "北京", "30102")
	# print(m_student.list_all())
	# print(s.add_student())
	# t = m_teacher("10101102","大明", "男", "教研室主任", "10101")
	# print(t.add_teacher())
	# print(t.update_teacher())
	# print(m_teacher.search("1"))
	# print(m_teacher.list_all())
	# print(t.del_teacher())
	# print(s.del_student())
	# print(s.update_student())
	# c = m_course("000002","线性带数", 5, 36, "10101101")
	# print(c.add_course())
	# print(c.del_course())
	# print(c.update_course())
	# print(m_course.search("36"))
	# print(c.del_collage())
	# s = m_source("10101001","000001",40)
	# print(s.add_source())
	# print(s.del_source())
	# print(s.update_source())
	t0 = m_collage.list_all()[0]
	t = m_collage.list_all()
	# print(m_collage.req2dic(t0))
	print(m_collage.req2list(t))
	# print(m_collage.list_all())


