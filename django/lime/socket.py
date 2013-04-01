from socketio.namespace import BaseNamespace

import logging
logger = logging.getLogger('lime.socket')

class LimeNamespace(BaseNamespace):
    name = '/lime'
    def on_changed(self, newValue):
        logger.info('new value: %s' % newValue)
        # TODO: Write the actual data to the database
        # TODO: Notify other listeners of data change?

    def on_connected(self):
        self.emit('value',{'my-status':0,'her-status':1})
        # TODO: Read the actual data from the database
