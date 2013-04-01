from socketio.namespace import BaseNamespace
from models import Person

import logging
logger = logging.getLogger('lime.socket')

class LimeNamespace(BaseNamespace):
    name = '/lime'
    def on_changed(self, newValue):
        logger.info('new value: %s' % newValue)
        self.person.status = (newValue == 1)
        self.person.save()
        # TODO: Notify other listeners of data change?

    def on_connected(self, userid):
        self.person = Person.objects.get(id=userid)
        logger.info('user %d connected' % userid)
        self.emit('value', {
            'my-status': self.person.status + 0,
            'her-status': self.person.loves.status + 0
        })
