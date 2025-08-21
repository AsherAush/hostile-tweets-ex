import fetcher
import processor
import  manager

#יצירת מוםע של פאסט API, ומופע של החיבור למונגו
app = FastAPI()
manager = Manager()


# יצירת ראוט בדיקה שהשרת עלה ורץ
@app.get("/")
def home():
    return {"message": "API is up and running!"}


# יצירת ראוט שמחזיר את כל הציוצים, ע"י הפעלת הפונקציה fetch_all
@app.get("/tweets")
def get_all_tweets():
    fetcher = MongoFetcher()
    return {"tweets": fetcher.fetch_all()}

# ראוט שמחזיר את כל הציוצים מעובדים
@app.get("/processed_tweets")
def get_processed():
    return manager.get_process()


if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",port=9000)