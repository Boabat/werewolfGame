import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        self.render("index.html", list_info = {11, 22, 33})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

''' settings
'''
settings = {
    "template_path" : "views",            # html�ļ�
    "static_path": "static",              # ��̬�ļ�·����css��js��img��
    "static_url_prefix" : "/static/",     # ��̬�ļ�ǰ׺
}

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()