import pymongo as p
class DB:
    client = p.MongoClient("mongodb+srv://suvenduc789:suvenduc789@cluster0.5hfi8pd.mongodb.net/?retryWrites=true&w=majority")
    db = client['victim']
    collection = db['vic_det']

    