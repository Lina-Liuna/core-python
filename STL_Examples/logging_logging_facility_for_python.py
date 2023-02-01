# This module defines functions and classes which implement a flexible event logging system for applications and libraries.
# The key benefit of having the logging API provided by a standard library module is that all python module can
# participate in logging, so your application log can include your own messages integrated with messages from thrid-party modules

import logging

test_logger = logging.getLogger()
test_logger.setLevel('INFO')
test_logger.setLevel('DEBUG')
logging.warning('watch out!')
logging.info('Good Morning, From Lina Liu')
logging.debug('dig into details')
logging.error('There is no eggs in refrigerator!')

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

