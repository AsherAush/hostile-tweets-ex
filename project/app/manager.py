import fetcher
import processor



class Manager:
    def _init_(self):
        # מופע למחלקה שיוצרת חיבור עם המונגו
        self.fetcher = fetcher.Connection()

    # פונקציהה שמבצעת את עיבוד הטקסט וכו, מחזירה גייסון
    def get_process(self):
        df = self.fetcher.get_data_frame()
        processor = TextProcessor(df)
        processed_df = processor.get_df()


        # יצירת רשימה של מילונים של ציוצים מעובדים
        for item in result:
            print(item)
            print("-------------------------")