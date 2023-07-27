class Player:

	def __init__(self, color, x, y):
		self.color = color
		self.x = x
		self.y = y


	def leagall_movement(self, new_x, new_y):
		raise NotImplemented

	def check_if_free_movement(self, new_x, new_y current_board):
		current_soldier = current_board[new_x][new_y]
		if current_soldier:
			if current_soldier.color == self.color:
				print("the place is not avaliable")
				return False
			# add the eaten soldier to anywhere?
			return True
		return True

	def check_movement(self, new_x, new_y, current_board):
		return self.leagall_movement(new_x, new_y) and self.check_if_free_movement(new_x, new_y, current_board)

	def move(self, new_x, new_y, current_board):
		if self.check_movement(new_x, new_y, current_board):
			current_board[self.x][self.y] = None
			self.x = new_x
			self.y = new_y
			current_board[self.x][self.y] = self
		else:
			pass
			# todo
		