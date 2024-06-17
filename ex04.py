"""Escreva um programa que verifique se um número inserido pelo usuário é par ou ímpar."""

numero = int(input("Informe um numero"))
resto = numero % 2

if resto == 0:
    print("Numero é Par")
else:
    print("Numero é impar")    