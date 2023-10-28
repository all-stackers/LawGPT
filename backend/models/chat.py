from mongo_engine import db
import datetime

class Chat(db.Document):
    title = db.StringField(required=True)
    language = db.StringField(required=True)
    summary = db.StringField(required=True)
    tags = db.StringField(required=True)
    # pdf = db.FileField(required=True)
    # user_id = db.StringField(required=True)
    date = db.DateTimeField(default=datetime.datetime.utcnow)
    messages = db.ListField(db.DictField(), default=[])
    index_id = db.StringField(required=False)
    chat_history = db.ListField(default=[])
    
    meta = {'collection': 'chats'}

    @classmethod
    def add(cls, title, language, summary, tags, random_number, engine_chat_history):
        try:
            document = cls(title=title, language=language, summary=summary, tags=tags, index_id=random_number, chat_history=engine_chat_history)
            document.save()
            return {"error": False, "data": document}
        except Exception as e:
            print(e)
            return {"error": True, "message": str(e)}
    
    @classmethod
    def add_message(cls, index_id, message):
        try:
            document = cls.objects.get(index_id=index_id)
            document.messages.append(message)
            document.save()
            return {"error": False, "data": document}
        except Exception as e:
            print(e)
            return {"error": True, "message": str(e)}
        
    @classmethod
    def get_chat_index_id(cls, index_id):
        try:
            document = cls.objects.get(index_id=index_id)
            return {"error": False, "data": document}
        
        except Exception as e:
            print(e)
            return {"error": True, "message": str(e)}

