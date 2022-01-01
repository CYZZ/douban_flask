import sqlite3

from flask import Flask, render_template

app = Flask(__name__)


# 路由路径不能重复，用户只能通过唯一路径进行访问特定的函数
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/about.html")
def about():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    cur.close()
    return render_template("about.html", movies=datalist)


# 评分
@app.route("/domain.html")
def domain():
    score = []  # 评分
    num = []    # 统计
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score, count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    cur.close()
    cur.close()
    return render_template("domain.html", score=score, num=num)


@app.route("/blog.html")
def blog():
    return render_template("blog.html")


if __name__ == '__main__':
    app.run()
