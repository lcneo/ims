class struct_account:
    """account模型"""

    def __init__(self, account: str, password: str):
        self.account = account
        self.password = password

    # Getter function
    @property
    def account(self) -> str:
        return self._account

    @account.setter
    def account(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Expected a int')
        self._account = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        if not isinstance(value, str):
            raise TypeError('Expected a int')
        self._password = value


# model collage
class struct_collage:
    """docstring for m_collage"""

    def __init__(self, collage_no: str, collage_name: str, dean: str, tel: str, address: str):
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
        if not isinstance(value, str):
            raise TypeError("collage_no char 1")
        if len(value) != 1:
            raise TypeError("collage_no char 1")
        self._collage_no = value

    @property
    def collage_name(self):
        return self._collage_name

    @collage_no.setter
    def collage_name(self, value):
        if not isinstance(value, str):
            raise TypeError("collage_name char 16")
        if len(value) > 16:
            raise TypeError("collage_name char 16")
        self._collage_name = value

    @property
    def dean(self):
        return self._dean

    @dean.setter
    def dean(self, value):
        if not isinstance(value, str):
            raise TypeError("dean char 6")
        if len(value) > 6:
            raise TypeError("dean char 6")
        self._dean = value

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        if not isinstance(value, str):
            raise TypeError("tel char 13")
        if len(value) > 13:
            raise TypeError("tel char 13")
        self._tel = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("address char 16")
        if len(value) > 16:
            raise TypeError("address char 16")
        self._address = value


class struct_department:
    """docstring for m_department"""

    def __init__(self, department_no: str, name: str, department_head: str, tro_num: int, class_num: int,
                 collage_no: struct_collage.collage_no):
        self.department_no = department_no
        self.name = name
        self.department_head = department_head
        self.tro_num = tro_num
        self.class_num = class_num
        self.collage_no = collage_no


class struct_no:
    """docstring for struct_no"""

    def __init__(self, class_no: str, class_name: str, class_size: int, class_monitor: str, professional: str,
                 department_no: str):
        self.class_no = class_no
        self.class_name = class_name
        self.class_size = class_size
        self.class_monitor = class_monitor
        self.professional = professional
        self.department_no = department_no

    @property
    def class_no(self):
        return self._class_no



if __name__ == '__main__':
    acc = struct_account("a", 'b')
    print(acc.id)



