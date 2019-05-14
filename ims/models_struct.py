def check_type(value, type_class:type, length:int)->bool:
	"""
	检测数据类型
	"""
	if not isinstance(value, type_class):
		return False
	if not isinstance(value, str):
		value = str(value)
	if len(value) > length:
		return False
	return True

#字段封装 Package field
class field_user:
	"""
	user.account:str_16
	user.password:str_16
	"""
	def __init__(self, account:str, password:str):
		self.account = account
		self.password = password

	#Getter function
	@property
	def account(self):
		return self._account
	#Setter function
	@account.setter
	def account(self, value):
		if not check_type(value, str, 16):
			raise TypeError("user.account:str_16")
		self._account=value

	@property
	def password(self):
		return self._password
	@password.setter
	def password(self, value):
		if not check_type(value, str, 16):
			raise TypeError("user.password:str_16")
		self._password = value

class field_collage:
	"""
		collage.collage_no:str_1
		collage.collage_name:str_16
		collage.dean:str_6
		collage.tel:str_13
		collage.address:str_16	
	"""
	def __init__(self, collage_no, collage_name, dean, tel, address):
		self.collage_no = collage_no
		self.collage_name = collage_name
		self.dean = dean
		self.tel = tel
		self.address = address	

	@property
	def collage_no(self):
		return self._collage_no
	@collage_no.setter
	def collage_no(self, value):
		if not check_type(value, str, 1):
			raise TypeError("user.collage_no:str_1")
		self._collage_no = value

	@property
	def collage_name(self):
		return self._collage_name
	@collage_name.setter
	def collage_name(self, value):
		if not check_type(value, str, 16):
			raise TypeError("user.collage_name:str_16")
		self._collage_name = value

	@property
	def dean(self):
		return self._dean
	@dean.setter
	def dean(self, value):
		if not check_type(value, str, 6):
			raise TypeError("user.dean:str_6")
		self._dean = value
	@property
	def tel(self):
		return self._tel
	@tel.setter
	def tel(self, value):
		if not check_type(value, str, 13):
			raise TypeError("user.tel:str_13")
		self._tel = value
	@property
	def address(self):
		return self._address
	@address.setter
	def address(self, value):
		if not check_type(value, str, 16):
			raise TypeError("user.address:str_16")
		self._address = value

class field_department:
	"""
		department.department_no:str_3
		department.name:str_14
		department.tro_num:int_6
		department.class_num:int_6
		department.collage_no:str_1
	"""
	def __init__(self, department_no, name, tro_num, class_num, collage_no):
		self.department_no = department_no
		self.name = name
		self.tro_num = tro_num
		self.class_num = class_num
		self.collage_no = collage_no
		
	@property
	def department_no(self):
		return self._department_no
	@department_no.setter
	def department_no(self, value):
		if not check_type(value, str, 3):
			raise TypeError("user.department_no:str_3")
		self._department_no = value

	@property
	def name(self):
		return self._name
	@name.setter
	def name(self, value):
		if not check_type(value, str, 14):
			raise TypeError("user.name:str_14")
		self._name = value

	@property
	def tro_num(self):
		return self._tro_num
	@tro_num.setter
	def tro_num(self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.tro_num:int_6")
		self._tro_num = value

	@property
	def class_num(self):
		return self._class_num
	@class_num.setter
	def class_num(self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.class_num:int_6")
		self._class_num = value

	@property
	def collage_no(self):
		return self._collage_no
	@collage_no.setter
	def collage_no(self, value):
		if not check_type(value, str, 1):
			raise TypeError("user.collage_no:str_1")
		self._collage_no = value

class field_class:
	"""
		class.class_no:str_5
		class.class_name:str_8
		class.class_size:int_6
		class.professional:str_10
		class.department_no:str_3
	"""
	def __init__(self, class_no, class_name, class_size, professional, department_no):
		self.class_no = class_no
		self.class_name = class_name
		self.class_size = class_size
		self.professional = professional
		self.department_no = department_no

	@property
	def class_no(self):
		return self._class_no
	@class_no.setter
	def class_no(self, value):
		if not check_type(value, str, 5):
			raise TypeError("user.class_no:str_5")
		self._class_no = value

	@property
	def class_name(self):
		return self._class_name
	@class_name.setter
	def class_name(self, value):
		if not check_type(value, str, 8):
			raise TypeError("user.class_name:str_8")
		self._class_name = value

	@property
	def class_size(self):
		return self._class_size
	@class_size.setter
	def class_size(self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.class_size:int_6")
		self._class_size = value

	@property
	def professional(self):
		return self._professional
	@professional.setter
	def professional(self, value):
		if not check_type(value, str, 10):
			raise TypeError("user.professional:str_10")
		self._professional = value

	@property
	def department_no  (self):
		return self._department_no 
	@department_no .setter
	def department_no  (self, value):
		if not check_type(value, str, 3):
			raise TypeError("user.department_no:str_3")
		self._department_no = value

class field_tro:
	"""		
		tro.tro_no:str_5
		tro.tro_name:str_16
		tro.tro_size:int_6
		tro.department_no:str_3
	"""
	def __init__(self, tro_no, tro_name, tro_size, department_no):
		self.tro_no = tro_no
		self.tro_name = tro_name
		self.tro_size = tro_size
		self.department_no = department_no

	@property
	def tro_no  (self):
		return self._tro_no 
	@tro_no .setter
	def tro_no  (self, value):
		if not check_type(value, str, 5):
			raise TypeError("user.tro_no:str_5")
		self._tro_no = value

	@property
	def tro_name  (self):
		return self._tro_name 
	@tro_name .setter
	def tro_name  (self, value):
		if not check_type(value, str, 16):
			raise TypeError("user.tro_name:str_16")
		self._tro_name = value

	@property
	def tro_size  (self):
		return self._tro_size 
	@tro_size .setter
	def tro_size  (self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.tro_size:int_6")
		self._tro_size = value

	@property
	def department_no  (self):
		return self._department_no 
	@department_no .setter
	def department_no  (self, value):
		if not check_type(value, str, 3):
			raise TypeError("user.department_no:str_3")
		self._department_no = value

class field_student:
	"""
		student.student_no:str_8
		student.student_name:str_6
		student.gender:str_2
		student.birthday:str_30
		student.birthplace:str_50
		student.class_no:str_5
	"""
	def __init__(self, student_no, student_name, gender, birthday, birthplace, class_no):
		self.student_no = student_no
		self.student_name = student_name
		self.gender = gender
		self.birthday = birthday
		self.birthplace = birthplace
		self.class_no = class_no

	@property
	def student_no  (self):
		return self._student_no 
	@student_no .setter
	def student_no  (self, value):
		if not check_type(value, str, 8):
			raise TypeError("user.student_no:str_8")
		self._student_no = value

	@property
	def student_size  (self):
		return self._student_size 
	@student_size .setter
	def student_size  (self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.student_size:int_6")
		self._student_size = value

	@property
	def gender  (self):
		return self._gender 
	@gender .setter
	def gender  (self, value):
		if not check_type(value, str, 2):
			raise TypeError("user.gender:str_2")
		self._gender = value

	@property
	def birthday  (self):
		return self._birthday 
	@birthday .setter
	def birthday  (self, value):
		if not check_type(value, str, 30):
			raise TypeError("user.birthday:str_30")
		self._birthday = value

	@property
	def birthplace  (self):
		return self._birthplace 
	@birthplace .setter
	def birthplace  (self, value):
		if not check_type(value, str, 50):
			raise TypeError("user.birthplace:str_50")
		self._birthplace = value

	@property
	def class_no(self):
		return self._class_no
	@class_no.setter
	def class_no(self, value):
		if not check_type(value, str, 5):
			raise TypeError("user.class_no:str_5")
		self._class_no = value

class field_teatcher:
	"""		
		teacher.teacher_no:str_8
		teacher.teacher_name:str_6
		teacher.gender:str_2
		teacher.post:str_8
		teacher.tro_no:str_5
	"""
	def __init__(self, teacher_no, teacher_name, gender, post, tro_no):
		self.teacher_no = teacher_no
		self.teacher_name = teacher_name
		self.gender = gender
		self.post = post
		self.tro_no = tro_no

	@property
	def teacher_no  (self):
		return self._teacher_no 
	@teacher_no .setter
	def teacher_no  (self, value):
		if not check_type(value, str, 8):
			raise TypeError("user.teacher_no:str_8")
		self._teacher_no = value

	@property
	def teacher_name  (self):
		return self._teacher_name 
	@teacher_name .setter
	def teacher_name  (self, value):
		if not check_type(value, str, 6):
			raise TypeError("user.teacher_name:str_6")
		self._teacher_name = value

	@property
	def gender  (self):
		return self._gender 
	@gender .setter
	def gender  (self, value):
		if not check_type(value, str, 2):
			raise TypeError("user.gender:str_2")
		self._gender = value

	@property
	def post  (self):
		return self._post 
	@post .setter
	def post  (self, value):
		if not check_type(value, str, 8):
			raise TypeError("user.post:str_8")
		self._post = value

	@property
	def tro_no  (self):
		return self._tro_no 
	@tro_no .setter
	def tro_no  (self, value):
		if not check_type(value, str, 5):
			raise TypeError("user.tro_no:str_5")
		self._tro_no = value

class field_course:
	"""
		course.course_no:str_6
		course.course_name:str_16
		course.period:int_6
		course.credit:int_6
		course.teacher_no:str_8
	"""
	def __init__(self, course_no, course_name, period, credit, teacher_no):
		self.course_no = course_no
		self.course_name = course_name
		self.period = period
		self.credit = credit
		self.teacher_no = teacher_no

	@property
	def course_no  (self):
		return self._course_no 
	@course_no .setter
	def course_no  (self, value):
		if not check_type(value, str, 6):
			raise TypeError("user.course_no:str_6")
		self._course_no = value

	@property
	def course_name  (self):
		return self._course_name 
	@course_name .setter
	def course_name  (self, value):
		if not check_type(value, str, 16):
			raise TypeError("user.course_name:str_16")
		self._course_name = value

	@property
	def period  (self):
		return self._period 
	@period .setter
	def period  (self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.period:int_6")
		self._period = value

	@property
	def credit  (self):
		return self._credit 
	@credit .setter
	def credit  (self, value):
		if not check_type(value, int, 6):
			raise TypeError("user.credit:int_6")
		self._credit = value

	@property
	def teacher_no  (self):
		return self._teacher_no 
	@teacher_no .setter
	def teacher_no  (self, value):
		if not check_type(value, str, 8):
			raise TypeError("user.teacher_no:str_8")
		self._teacher_no = value

class field_source:
	"""
		source.student_no:str_8
		source.course_no:str_6
		source.source:int_3
	"""
	def __init__(self, student_no, course_no, source):
		self.student_no = student_no
		self.course_no = course_no
		self.source = source
		
	@property
	def student_no  (self):
		return self._student_no 
	@student_no .setter
	def student_no  (self, value):
		if not check_type(value, str, 8):
			raise TypeError("user.student_no:str_8")
		self._student_no = value

	@property
	def course_no  (self):
		return self._course_no 
	@course_no .setter
	def course_no  (self, value):
		if not check_type(value, str, 6):
			raise TypeError("user.course_no:str_6")
		self._course_no = value

	@property
	def source  (self):
		return self._source 
	@source .setter
	def source  (self, value):
		if not check_type(value, int, 3):
			raise TypeError("user.source:int_3")
		self._source = value

if __name__ == '__main__':
	pass
	# a = field_user("123", "123")
	# print(a.account)
	# print(check_type(123, int, 2))