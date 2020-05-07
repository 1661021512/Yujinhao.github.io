from flask import Flask, render_template
from pyecharts.charts import Bar
from pyecharts import options as opts
app = Flask(__name__)
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(["老番茄", "敬汉卿", "LexBurner",'中国BOY超级大猩猩', "共青团中央", "敖厂长", "翔翔大作战",'凉风Kaze','华农兄弟','指法芬芳张大仙'])
        .add_yaxis("Fans", [1103, 852, 813, 517, 560, 689,600,618,555,458])
        .set_global_opts(title_opts=opts.TitleOpts(title="B站优秀UP主"),
                         xaxis_opts=opts.AxisOpts(axislabel_opts=({"interval":"0"}))
                         )
    )
    return c
name = 'BiliBli'
ups = [
    {'title': '老番茄', 'fans': '1103万'},
    {'title': '敬汉卿', 'fans': '852万'},
    {'title': 'LexBurner', 'fans': '813万'},
    {'title': '中国BOY超级大猩猩', 'fans': '517万'},
    {'title': '共青团中央', 'fans': '560万'},
    {'title': '敖厂长', 'fans': '689万'},
    {'title': '翔翔大作战', 'fans': '600万'},
    {'title': '凉风Kaze', 'fans': '618万'},
    {'title': '华农兄弟', 'fans': '555万'},
    {'title': '指法芬芳张大仙', 'fans': '458万'},

]
@app.route('/')
def index():
    return render_template('index.html', name=name, ups=ups)
@app.route('/bar')
def bar1():
    bar = bar_base()
    return render_template('bar.html',
                           myechart=bar.render_embed(),
                           )
@app.route('/redu')
def heliu():
    return render_template('redutu.html')
if __name__ == '__main__':
    app.run(debug=True)

