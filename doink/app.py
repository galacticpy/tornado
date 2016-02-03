import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")
        
class DisplayHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/display.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/display", DisplayHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()