from mongo_engine import db
from mongoengine import Document, StringField, IntField

class PDF(db.Document):
    pdf_name = StringField(required=True)
    original_file_cid = StringField(required=True)
    original_file_url = StringField(required=True)
    translated_file_cid = StringField(required=True)
    translated_file_url = StringField(required=True)
    chat_id = IntField(required=False)

    # pdf_name: db.StringField(required=True)
    # original_file_cid: db.StringField(required=True)
    # original_file_url: db.StringField(required=True)
    # translated_file_cid: db.StringField(required=True)
    # translated_file_url: db.StringField(required=True)
    # chat_id: db.IntField(required=False)

    @classmethod
    def get_all(cls):
        try:
            pdfs = cls.objects.all()
            return {"error": False, "data": pdfs}
        
        except Exception as e:
            print(e)
            return {"error": True, "message": "Error while fetching PDFs"}
    
    @classmethod
    def get_by_id(cls, id):
        try:
            pdf = cls.objects.get(id=id)
            return {"error": False, "data": pdf}
        
        except cls.DoesNotExist:
            return {"error": True, "message": "PDF not found"}
        
    @classmethod
    def add(cls, pdf_name, original_file_cid, original_file_url, translated_file_cid, translated_file_url, chat_id):
        try:
            pdf = cls(
                pdf_name=pdf_name,
                original_file_cid=original_file_cid,
                original_file_url=original_file_url,
                translated_file_cid=translated_file_cid,
                translated_file_url=translated_file_url,
                chat_id=chat_id
            )
            print(pdf)
            pdf.save()
            return {"error": False, "data": pdf}
        
        except Exception as e:
            print(e)
            return None