#-*- coding:utf8 -*-

# TextBox for SFML Python binding

import sfml as sf
import base

class TextBox(base.BaseComponent):
	def __init__(self, name, size, shadowtext="Type here"):
		base.BaseComponent(self, name)
		self.events.update({
			'OnFocus': None,
			'OnBlur': None,
		})
		self.shadowtext = shadowtext
		self.x_rect = sf.RectangleShape()
		self.x_rect.size = size
		self.focused = False
		self.hovered = False
		self.font_color = sf.Color.BLACK
		self.shadow_color = sf.Color(200, 200, 200)

		self.text = ""

		self.fontsize = 10
		self.forefont = None
		self.shadowfont = None

		self._run_event('OnCreate')

	def set_position(self, position):
		self.x_rect.position = position

	def set_outline(self, thickness=0, color=sf.Color.WHITE):
		self.x_rect.outline_color = color
		self.x_rect.outline_thickness = float(thicnkess)

	def set_color(self, font=sf.Color.BLACK, back=sf.Color.WHITE):
		self.x_rect.fill_color = back
		self.font_color = font

	def set_forefont(self, font):
		self.forefont = font

	def set_shadowfont(self, font):
		self.shadowfont = font

	def set_font_size(self, size):
		self.fontsize = size

	def _draw(self, target):
		# Overloading BaseComponent abstract '_draw' method
		target.draw(self.x_rect)

		if not self.focused and self.text == '':
			shadow = sf.Text(self.shadowtext)
			shadow.font = self.shadowfont # sf.Font.from_file("./font/eurof56.ttf")
			shadow.character_size = self.fontsize
			shadow.color = self.shadow_color
			shadow.position = sf.Vector2(self.x_rect.global_bounds.left + 5, self.x_rect.global_bounds.top + 5)
			target.draw(shadow)
		if self.text != "":
			x_text = sf.Text(self.text)
			x_text.font = self.forefont
			x_text.character_size = self.fontsize
			x_text.color = self.font_color
			x_text.position = sf.Vector2(self.x_rect.global_bounds.left + 5, self.x_rect.global_bounds.top + 5)
			target.draw(x_text)

		self._run_event('OnDraw')

	def focus(self):
		self.focused = True
		self._run_event('OnFocus')

	def blur(self):
		self.focused = False
		self._run_event('OnBlur')

	def handle_event(self, event):
		# Overloading BaseComponent abstract 'handle_event' method
		if type(event) == sf.TextEvent:
			if self.focused:
				if event.unicode >= 32 and event.unicode < 127:
					self.text += chr(event.unicode)
				elif event.unicode == 8:
					if len(self.text) > 0:
						self.text = self.text[:-1]
		elif type(event) == sf.MouseMoveEvent:
			self.hovered = self.x_text.global_bounds.contains(event.position)
		elif type(event) == sf.MouseButtonEvent:
			if self.hovered:
				if event.released and event.button == sf.Mouse.LEFT:
					self.focus()
			else:
				if event.released:
					self.blur()

