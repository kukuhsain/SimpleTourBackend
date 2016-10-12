from google.appengine.ext import ndb
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing

class Note(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def add(cls, user, title, content):
        parent = user.key
        note = cls(parent=parent, title=title, content=content)
        note.put()
        return note

    @classmethod
    def get_all_by_specific_user(cls, user):
        ancestor = user.key
        notes = cls.query(ancestor=ancestor).fetch()
        return notes

    @classmethod
    def get_some_by_specific_user(cls, user, amount):
        ancestor = user.key
        notes = cls.query(ancestor=ancestor).fetch(amount)
        return notes

    @classmethod
    def update(cls, user, note_id, title, content):
        note = cls.get_by_id(int(note_id))
        if note:
            note.title = title
            note.content = content
            note.put()
            return note
        else:
            return False

    @classmethod
    def delete(cls, note_id):
        note = cls.get_by_id(int(note_id))
        if note:
            note.key.delete()
            return True
        else:
            return False
