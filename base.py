#-*- coding:utf8 -*-

# Base for all SFML Components
# Do not create directly a BaseComponent object

import sfml as sf
from abc import abstractmethod

class BaseComponent(sf.TransformableDrawable):
	def __init__(self, name):
		self.component_name = name
		self.events = {
			'OnCreate': None,
			'OnDraw': None,
		}

	def _run_event(self, name, args=None):
		if name in self.events:
			self.events[name](self, args)

	def draw(self, target, states):
		sf.TransformableDrawable.draw(self, target, states)
		states.transform *= get_transform()
		self._draw(self, target)

	@abstractmethod
	def _draw(self, target):
		pass

	@abstractmethod
	def handle_event(self, event):
		pass
