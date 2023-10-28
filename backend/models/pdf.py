from mongo_engine import db

class PDF(db.Document):
    id = db.StringField(required=True)
    name = db.StringField(required=True)
    language = db.StringField(required=True)
    summary = db.StringField(required=True)
    url = db.StringField(required=True)
    category = db.StringField(required=True)

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
    def add(cls, args):
        try:
            pdf = cls(**args).save()
            return {"error": False, "data": pdf}
        
        except Exception as e:
            print(e)
            return None