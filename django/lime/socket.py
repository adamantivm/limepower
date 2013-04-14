from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin
from models import Person
import time

import logging
logger = logging.getLogger('lime.socket')

class LimeNamespace(BaseNamespace, BroadcastMixin):
    name = '/lime'
    def on_changed(self, newValue):
        logger.info('new value: %s' % newValue)
        self.person.status = (newValue == 1)
        self.person.last_updated = time.now()
        self.person.save()
        self.broadcast_event_not_me('value', {
            'her-status': self.person.status + 0,
            'my-status': self.person.loves.status + 0
        })

    def on_connected(self, *args):
        logger.debug('user %s connected' % self.request.user)
        if not self.request.user.is_authenticated():
            logger.debug('requesting login')
            self.emit('request_login')
        else:
            self.person = self.request.user
            self.emit('value', self._get_cur_value())

    def _get_cur_value(self):
        return {
            'my-status': self.person.status + 0,
            'her-status': self.person.loves.status + 0
        }
 
