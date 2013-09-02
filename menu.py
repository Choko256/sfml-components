#-*- coding:utf8 -*-

# Menu bar for SFML

import sfml as sf
import base as b

class MenuItem(b.BaseComponent):
	def __init__(self, name, label, position=(0,0)):
		b.BaseComponent.__init__(self, name)
		self._label = label
		self._children = []
		self._checked = False
		self._on_click = None
		self._opened = False
		self._hovered = False
		self._itm = sf.Text(self._label)
		self._itm.position = position

	def __str__(self):
		return self._label

	def _draw(self, target):
		if self._hovered:
			self._itm.color = sf.Color(150, 50, 0)
		else:
			self._itm.color = sf.Color.BLACK
		target.draw(self._itm)

	def handle_event(self, event):
		if type(event) is sf.MouseMoveEvent:
			self._hovered = self._itm.global_bounds.contains(event.position)

class MenuBarPosition:
	POSITION_TOP = 0xA0
	POSITION_BOTTOM = 0xA1
	POSITION_LEFT = 0xA2
	POSITION_RIGHT = 0xA3

class MenuBar(b.BaseComponent):
	def __init__(self, name, position=MenuBarPosition.POSITION_TOP, size=35):
		b.BaseComponent.__init__(self, name)
		self.events.update({
			'OnClick': None,
		})
		self._items = []
		self._position = position
		self._size = size
		self._fill_color = sf.Color(153, 153, 153)

	def _draw(self, target):
		if self._position in [ MenuBarPosition.POSITION_TOP, MenuBarPosition.POSITION_LEFT ]:
			pos = (0, 0)
			if self._position == MenuBarPosition.POSITION_TOP:
				bar = sf.RectangleShape(sf.Vector2(target.width, self._size))
			elif self._position == MenuBarPosition.POSITION_LEFT:
				bar = sf.RectangleShape(sf.Vector2(self._size, target.height))
		elif self._position == MenuBarPosition.POSITION_BOTTOM:
			pos = (0, target.height - self._size)
			bar = sf.RectangleShape(sf.Vector2(target.width, self._size))
		elif self._position == MenuBarPosition.POSITION_RIGHT:
			pos = (target.width - self._size, 0)
			bar = sf.RectangleShape(sf.Vector2(self._size, target.height))
		else:
			raise Exception("Bad Menu bar position value: Expected one of MenuBarPosition constant values.")
		bar.position = pos
		bar.fill_color = self._fill_color
		target.draw(bar)

		for itm in self._items:
			target.draw(itm)

	def handle_event(self, event):
		pass
