from flask import Flask,jsonify
import utls

app = Flask(__name__)

@app.route("/catalogy", methods=["GET"])
def get_cato():
    rows = utls.get_news_by_id("SELECT * FROM catalogy")
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "url": r[2],

        })
    return jsonify({"catalogy": data})

@app.route("/news", methods=["GET"])
def getNews():
    rows = utls.get_news_by_id("SELECT * FROM news")
    data=[]
    for r in rows:
        data.append({
            "id":r[0],
            "subject":r[1],
            "description":r[2],
            "image":r[3],
            "original_url": r[4]
        })
    return jsonify({"news":data})


@app.route("/new/<int:new_id>", methods=["GET"])
def getNewsById(new_id):
    pass
@app.route("/new/add", methods=["POST"])
def insertNews():
    pass

if __name__ == "__main__":
    app.run()