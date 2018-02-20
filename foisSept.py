#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

def tableMult(nb, max):
	i = 1
	while i <= max:
		print(i, "*", nb, "=", i*nb)
		i+=1

tableMult(9, 15)
