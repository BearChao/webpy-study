#encoding:utf-8
'''
Created on 2015年1月29日

@author: zynick
'''
import web
from pip._vendor.requests.certs import where

render = web.template.render('templates/')
db = web.database(dbn='sqlite',db='f:\data.db')

urls = (
    '/','index',
    '/add','add',
    '/del','delete'
)
app = web.application(urls,globals())

class index:
    def GET(self,):
        todos = db.select('todo')

        return render.index(todos)
class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo',title = i.title)
        raise web.SeeOther('/')
class delete:
    def POST(self):
        d = web.input()
        n = db.delete('todo',where="id="+d.id)
        raise web.SeeOther('/')
if __name__ == '__main__':

    app.run()