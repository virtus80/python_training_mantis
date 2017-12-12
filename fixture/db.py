import pymysql

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, nickname, company, address, home, work, mobile, "
                           "phone2, email, email2, email3 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, nickname, company, address, homephone, workphone, mobilephone, secondaryphone, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, nickname=nickname, company=company,
                            address=address, homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def clean_group(self, group):
        return Group(id=group.id, name=group.name.strip())

    def clean_contact(self, contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

    def destroy(self):
        self.connection.close()