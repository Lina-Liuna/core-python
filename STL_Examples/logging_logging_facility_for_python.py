# This module defines functions and classes which implement a flexible event logging system for applications and libraries.
# The key benefit of having the logging API provided by a standard library module is that all python module can
# participate in logging, so your application log can include your own messages integrated with messages from thrid-party modules

import logging

logging.warning('watch out!')
logging.info('Good Morning, From Lina Liu')
logging.debug('dig into details')
logging.error('There is no eggs in refrigerator!')