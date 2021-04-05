import sqlite3 as sql

class Clients:

    connection = None

    def __init__(self):
        self.connection = sql.connect('db.db')

    def IsInBase(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT user_course, user_group FROM users WHERE id_user_vk = ?;', (str(defID).lower(),))
            data = cur.fetchall()
            if (len(data) > 0):
                return (True)
            else:
                return (False)
        except Exception as ex:
            return(False)

    def FindByid(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT user_group, user_course, user_role, doc_page FROM users WHERE id_user_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data)
        except Exception as ex:
            return(False)

    def GetMenuFlag(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT in_menu FROM users WHERE id_user_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data[0])
        except Exception as ex:
            return(False)

    def GetDocsFlag(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT in_docs FROM users WHERE id_user_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data[0])
        except Exception as ex:
            return(False)

    def GetUserRole(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT user_role FROM users WHERE id_user_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data[0])
        except Exception as ex:
            return(False)

    def GetDocPage(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT doc_page FROM users WHERE id_user_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data[0])
        except Exception as ex:
            return(False)

            
    def UpdateCourse(self, defID, newcourse):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET user_course = ? WHERE id_user_vk = ?;', (newcourse.lower(), str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def UpdateDocPage(self, defID, newdocpage):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET doc_page = ? WHERE id_user_vk = ?;', (newdocpage.lower(), str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def AddNewUser(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('INSERT INTO users (id_user_vk) VALUES ( ? );',(str(defID).lower(),))
            self.connection.commit()
            return(True)
        except Exception as ex:
            return(False)

    def UpdateGroup(self, defID, newgroup):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET user_group = ? WHERE id_user_vk = ?;', (newgroup.lower(), str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def UpdateDocPage(self, defID, newdocpage):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET doc_page = ? WHERE id_user_vk = ?;', (newdocpage.lower(), str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def UpdateDocsFlag(self, defID, newdocsflag):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET in_docs = ? WHERE id_user_vk = ?;', (newdocsflag, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def UpdateMenuFlag(self, defID, newmenuflag):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET in_menu = ? WHERE id_user_vk = ?;', (newmenuflag, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def UpdateRole(self, defID, role):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE users SET user_role = ? WHERE id_user_vk = ?;', (role.lower(), str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def DeleteFromTable(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('DELETE FROM users WHERE id_user_vk = ?;',(str(defID).lower(),))
            self.connection.commit()
            return(True)
        except Exception as ex:
            return(False)

class DocsWork:

    connection = None

    def __init__(self):
        self.connection = sql.connect('db.db')

    def IsInBase(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT is_1course, is_2course, is_3course, is_4course, is_7group, is_8group, is_9group, is_10group, is_11group FROM docs WHERE id_doc_vk = ?;', (str(defID).lower(),))
            data = cur.fetchall()
            if (len(data) > 0):
                return (True)
            else:
                return (False)
        except Exception as ex:
            return(False)

    def IsInBaseByName(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT is_1course, is_2course, is_3course, is_4course, is_7group, is_8group, is_9group, is_10group, is_11group FROM docs WHERE doc_name = ?;', (str(defID),))
            data = cur.fetchall()
            if (len(data) > 0):
                return (True)
            else:
                return (False)
        except Exception as ex:
            return(False)

    def SetDoc1Course(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_1course = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc2Course(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_2course = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc3Course(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_3course = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc4Course(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_4course = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc7Group(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_7group = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc8Group(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_8group = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc9Group(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_9group = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc10Group(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_10group = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def SetDoc11Group(self, defID, state):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET is_11group = ? WHERE id_doc_vk = ?;', (state, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return (False)

    def FindIDByName(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT id_doc_vk FROM docs WHERE doc_name = ?;',(str(defID),))
            data = cur.fetchall()
            return(data[0])
        except Exception as ex:
            return(False)

    def FindByid(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT is_1course, is_2course, is_3course, is_4course, is_7group, is_8group, is_9group, is_10group, is_11group FROM docs WHERE id_doc_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data)
        except Exception as ex:
            return(False)

    def FindDocsByCourseAndGroup(self, course, group):
        try:
            sql_question = 'SELECT id_doc_vk FROM docs WHERE ' + course + ' = 1 AND ' + group + ' = 1;'
            #sql_question = str('SELECT id_doc_vk FROM docs WHERE ') + str(course) + str(' = 1;')
            cur = self.connection.cursor()
            cur.execute(sql_question)
            data = cur.fetchall()
            return(data)
        except Exception as ex:
            return(ex)

    def FindDocsForAdmin(self):
        try:
            #sql_question = 'SELECT id_doc_vk FROM docs WHERE ' + course + ' = 1 AND ' + group + ' = 1;'
            #sql_question = str('SELECT id_doc_vk FROM docs WHERE ') + str(course) + str(' = 1;')
            cur = self.connection.cursor()
            cur.execute('SELECT id_doc_vk FROM docs;')
            data = cur.fetchall()
            return(data)
        except Exception as ex:
            return(ex)

    def AddNewDoc(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('INSERT INTO docs (id_doc_vk) VALUES ( ? );',(str(defID).lower(),))
            self.connection.commit()
            return(True)
        except Exception as ex:
            return(False)

    def UpdateDocName(self, defID, newdocname):
        try:
            cur = self.connection.cursor()
            cur.execute('UPDATE docs SET doc_name = ? WHERE id_doc_vk = ?;', (newdocname, str(defID).lower()))
            self.connection.commit()
            return (True)
        except Exception as ex:
            return(False)

    def GetDocName(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('SELECT doc_name FROM docs WHERE id_doc_vk = ?;',(str(defID).lower(),))
            data = cur.fetchall()
            return(data[0])
        except Exception as ex:
            return(ex)

    def DeleteFromTable(self, defID):
        try:
            cur = self.connection.cursor()
            cur.execute('DELETE FROM docs WHERE id_doc_vk = ?;',(str(defID).lower(),))
            self.connection.commit()
            return(True)
        except Exception as ex:
            return(False)