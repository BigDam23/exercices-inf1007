"""
Chapitre 11.1

Classes pour représenter un personnage.
"""

import utils

class Weapon:
	"""
	Une arme dans le jeu.

	:param name:      Le nom de l'arme
	:param power:     Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""

	UNARMED_POWER = 20
	
	# TODO: __init__
	def __init__(self, name : str, power : int, min_level : int):
	# TODO: Propriétés
		self.__name = name
		self.power = power
		self.min_level = min_level
  
	@property
	def name(self):
		return self.__name

	# TODO: use
	def use(self, user, opponent):
		# TODO: Caculer et appliquer le dommage en utilisant la méthode compute_damage
		#damage, crit = ...
		damage, crit = self.compute_damage(user, opponent)

		opponent.hp -= damage
		msg = ""
		if crit:
			msg += "Critical hit! "
		msg += f"{opponent.name} took {damage} dmg"
		return msg

	def is_usable_by(self,user):
		if user.level >= self.min_level:
			return True
		else:
			return False

	# TODO: compute_damage
	def compute_damage(self, user, opponent):
		return utils.compute_damage_output(user.level, self.power, user.attack, opponent.defense, 1/16, (0.85,1.00))
		
	# TODO: make_unarmed
	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)
		


class Character:
	"""
	Un personnage dans le jeu

	:param name:    Le nom du personnage
	:param max_hp:  HP maximum
	:param attack:  Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level:   Le niveau d'expérience du personnage
	"""
	
	# TODO: __init__
	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.__max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = None
		self.hp = max_hp
  
	@property
	def name(self):
		return self.__name

	@property
	def max_hp(self):
		return self.__max_hp

	@max_hp.setter
	def max_hp(self, value):
		self.__max_hp = value
		self.hp = self.hp
	
	@property
	def hp(self):
		return self.__hp

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)
	
	@property
	def weapon(self):
		return self.__weapon

	@weapon.setter
	def weapon(self, value):
		if value is None:
			value = Weapon.make_unarmed()
		if not value.is_usable_by(self):
			raise ValueError(Weapon)
		
		self.__weapon = value
			
		
	# TODO: Propriétés

	def apply_turn(self, opponent):
		msg = f"{self.name} used {self.weapon.name}\n"
		msg += self.weapon.use(self, opponent)
		return msg
