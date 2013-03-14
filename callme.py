# -*- coding: utf-8 -*-
import logging
from wobble import *

logging.basicConfig(level=logging.DEBUG)

service = WobbleService()
service.connect("dummy_api_key")
# service.get_notifications()
