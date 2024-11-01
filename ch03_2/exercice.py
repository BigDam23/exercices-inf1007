#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	return voltage**2/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	# v1[0] et v2[0] pour accéder au X
	# v1[1] et v2[1] pour accéder au Y
	if v1[0]*v2[0]+v1[1]*v2[1] == 0:
		return True
	else:
		return False

def point_in_circle(point, circle_center, circle_radius):
	# TODO: Retourner vrai si le point est à l'intérieur du cercle, faux sinon.
	# point[0] et circle_center[0] pour accéder au X
	# point[1] et circle_center[1] pour accéder au Y
	x = point[0] + circle_center[0]
	y = point[1]  + circle_center[1]
	if math.sqrt(x**2+y**2) <= circle_radius:
		return True
	else:
		return False

def cash(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$, 25¢, 10¢ et 5¢ à remettre pour représenter la valeur. Il faut arrondir à la pièce de 5¢ près. Il faut remplir les variables twenties, tens, fives, ones, quarters, dimes et nickels avec le quantité de chaque dénomination.
	
	return twenties, tens, fives, ones, quarters, dimes, nickels

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres.
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(point_in_circle([-1, 1], [1, -1], 2))
	print(cash(137.38))
	print(format_base(-420, 16, "0123456789ABCDEF"))
