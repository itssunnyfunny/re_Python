class ChaiUtils:
    @staticmethod
    def clean_indegredients(text):
        return   [item for item in text.split(",")]
    

raw = "water , milk , ginger , honey "

cleaned = ChaiUtils.clean_indegredients(raw)
print(cleaned)