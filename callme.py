# -*- coding: utf-8 -*-
import logging
from wobble import *

logging.basicConfig(level=logging.DEBUG)

with WobbleService().connect('velroktestuser@example.com', 'VelrokTestUser') as service:
  service.topics_list()
  service.topic_set_archived('9-1363296224020-87760', 1)
