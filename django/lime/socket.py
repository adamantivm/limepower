from socketio.namespace import BaseNamespace

class LimeNamespace(BaseNamespace):
    name = '/lime'
    def on_ping(self, msg):
        self.emit("pong", "was = %s" % msg)
