# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:23:00 2024

@author: Poko
"""

ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"



def mid(cadena):
    estado = 0
    estados_aceptados = [1]
    delta = {0:{'q': 1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 'o':1, 'p':1, 'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 'j':1, 'k':1, 'l':1, 'z':1, 'x':1, 'c':1, 'v':1,'b':1, 'n':1, 'm':1, 'Q': 1, 'W':1, 'E':1, 'R':1, 'T':1, 'Y':1, 'U':1, 'I':1, 'O':1, 'P':1, 'A':1, 'S':1, 'D':1, 'F':1, 'G':1, 'H':1, 'J':1, 'K':1, 'L':1, 'Z':1, 'X':1, 'C':1, 'V':1,'B':1, 'N':1, 'M':1},1:{'q': 1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 'o':1, 'p':1, 'a':1, 's':1, 'd':1, 'f':1, 'g':1, 'h':1, 'j':1, 'k':1, 'l':1, 'z':1, 'x':1, 'c':1, 'v':1,'b':1, 'n':1, 'm':1, 'Q': 1, 'W':1, 'E':1, 'R':1, 'T':1, 'Y':1, 'U':1, 'I':1, 'O':1, 'P':1, 'A':1, 'S':1, 'D':1, 'F':1, 'G':1, 'H':1, 'J':1, 'K':1, 'L':1, 'Z':1, 'X':1, 'C':1, 'V':1,'B':1, 'N':1, 'M':1, '0':1, '1':1, '2':1, '3':1, '4':1, '5':1, '6':1, '7':1, '8':1,'9':1}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
# A = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0912345678'
# AA = '4Q33'
# AAA = ''
# output = mid(AA)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mnum(cadena):
    estado = 0
    estados_aceptados = [2, 3]
    delta = {0:{'-':1, '0':3, '1':2, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':2}, 1:{'1':2, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':2}, 2:{'0':2, '1':2, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':2}, 3:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
# B = '-1234567890123456789'
# BB = '-'
# BBB = '023'
# output = mnum(B)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mvar(cadena):
    estado = 0
    estados_aceptados = [3]
    delta = {0:{'v':1}, 1:{'a':2}, 2:{'r': 3}, 3:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    
# C = 'var'
# CC = 'v'
# CCC = 'r'
# output = mvar(CCC)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mconst(cadena):
    estado = 0
    estados_aceptados = [5]
    delta = {0:{'c':1}, 1:{'o':2}, 2:{'n':3}, 3:{'s':4}, 4:{'t':5}, 5:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# D = 'const'
# DD = 'cons'
# DDD = 'ns'
# output = mconst(DDD)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mcall(cadena):
    estado = 0
    estados_aceptados = [4]
    delta = {0:{'c':1}, 1:{'a':2}, 2:{'l':3}, 3:{'l':4}, 4:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# E = 'call'
# EE = 'ca'
# EEE = 'opl'
# output = mcall(EEE)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mbegin(cadena):
    estado = 0
    estados_aceptados = [5]
    delta = {0:{'b':1}, 1:{'e':2}, 2:{'g':3}, 3:{'i':4},4:{'n':5}, 5:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# F = 'begin'
# FF = 'be'
# FFF = 'opl'
# output = mbegin(F)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mend(cadena):
    estado = 0
    estados_aceptados = [3]
    delta = {0:{'e':1}, 1:{'n':2}, 2:{'d':3}, 3:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# G = 'end'
# GG = 'ca'
# GGG = 'opl'
# output = mend(G)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mif(cadena):
    estado = 0
    estados_aceptados = [2]
    delta = {0:{'i':1}, 1:{'f':2}, 2:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# H = 'if'
# HH = 'i'
# HHH = 'opl'
# output = mif(H)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mthen(cadena):
    estado = 0
    estados_aceptados = [4]
    delta = {0:{'t':1}, 1:{'h':2}, 2:{'e':3}, 3:{'n':4}, 4:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# I = 'then'
# II = 'th'
# III = 'opl'
# output = mthen(I)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mwhile(cadena):
    estado = 0
    estados_aceptados = [5]
    delta = {0:{'w':1}, 1:{'h':2}, 2:{'i':3}, 3:{'l':4}, 4:{'e':5}, 5:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# J = 'while'
# JJ = 'wh'
# JJJ = 'opl'
# output = mwhile(J)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mdo(cadena):
    estado = 0
    estados_aceptados = [2]
    delta = {0:{'d':1}, 1:{'o':2}, 2:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# K = 'do'
# KK = 'd'
# KKK = 'opl'
# output = mdo(K)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def modd(cadena):
    estado = 0
    estados_aceptados = [3]
    delta = {0:{'o':1}, 1:{'d':2}, 2:{'d':3}, 3:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# L = 'odd'
# LL = 'od'
# LLL = 'opl'
# output = modd(L)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mop(cadena):
    estado = 0
    estados_aceptados = [1]
    delta = {0:{'+':1, '-':1, '*':1, '/':1}, 1:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# M = '+'
# MM = 'ca'
# MMM = 'opl'
# output = mop(M)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def msim(cadena):
    estado = 0
    estados_aceptados = [1, 2, 3]
    delta = {0:{'>':1, '=':2, '<':3}, 1:{'=':2}, 2:{}, 3:{'>':2, '=':2}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# N = '<>'
# NN = '=<'
# NNN = 'opl'
# output = msim(N)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def msigasig(cadena):
    estado = 0
    estados_aceptados = [2]
    delta = {0:{':':1}, 1:{'=':2}, 2:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# O = ':='
# OO = '='
# OOO = 'opl'
# output = msigasig(OO)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def msignop(cadena):
    estado = 0
    estados_aceptados = [1]
    delta = {0:{',':1, ';':1, '#':1}, 1:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# P = ';'
# PP = ',;'
# PPP = 'opl'
# output = msignop(P)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mparen(cadena):
    estado = 0
    estados_aceptados = [1]
    delta = {0:{'(':1, ')':1}, 1:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# Q = '('
# QQ = ')'
# QQQ = 'opl'
# output = mparen(Q)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def meb(cadena):
    estado = 0
    estados_aceptados = [1]
    delta = {0:{' ':1, '\n':1, '\t':1}, 1:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# R = ' '
# RR = ')'
# RRR = 'opl'
# output = meb(R)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')

def mprocedure(cadena):
    estado = 0
    estados_aceptados = [9]
    delta = {0:{'p':1}, 1:{'r':2}, 2:{'o':3}, 3:{'c':4}, 4:{'e':5}, 5:{'d':6}, 6:{'u':7}, 7:{'r':8}, 8:{'e':9}, 9:{}}
    for caracter in cadena:
        if caracter in delta[estado].keys():
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_aceptados:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
# S = 'procedure'
# SS = 'proc'
# SSS = 'opl'
# output = mprocedure(SS)
# if output == ESTADO_TRAMPA:
#     print ('Estado trampa')
# if output == ESTADO_FINAL:
#     print ('Estado aceptado')
# if output == ESTADO_NO_FINAL:
#     print('Estado no aceptado')


#Lista de tokens posibles
TOKENS_POSIBLES = [("num", mnum),("var", mvar),("const", mconst), ("call", mcall),("begin", mbegin), ("end", mend), ("if", mif), ("then",mthen), ("while", mwhile), ("do", mdo), ("odd", modd), ("op", mop), ("simbolo", msim), ("asignacion", msigasig), ("signop", msignop), ("parentesis", mparen), ("procedure", mprocedure), ("id", mid), ("espacio_blanco", meb)]



#Aca comenzamos a definir el lexer
def lexer(codigo_fuente):
    tokens = [] # lista de tokens que devuelve el lexer
    posicion_actual = 0 # hasta donde va el lexema
    while posicion_actual < len(codigo_fuente): 
        TOKENS_DETECTADOS =[]
        TOKENS_MOMENTANEOS = []
        todos_trampa = False
        comienzo_lexema = posicion_actual
        while not todos_trampa and posicion_actual <= len(codigo_fuente):
            cadena_actual = codigo_fuente[comienzo_lexema:posicion_actual + 1]    
            todos_trampa = True
            TOKENS_DETECTADOS = TOKENS_MOMENTANEOS
            TOKENS_MOMENTANEOS =[]
            for (tipo_token, automata) in TOKENS_POSIBLES:
                estado = automata(cadena_actual)
                if estado == ESTADO_FINAL:
                    todos_trampa = False
                    TOKENS_MOMENTANEOS.append(tipo_token)
                    break
                elif estado == ESTADO_NO_FINAL:
                    todos_trampa = False      
            
            posicion_actual +=1

        print(f"DEBUG: tokens detectados = {TOKENS_DETECTADOS} cadena {cadena_actual} comienzo lexema: {comienzo_lexema} posicion actual {posicion_actual}"  )
        if len(TOKENS_DETECTADOS) == 0:
            raise Exception("ERROR: No se encontro token: " + cadena_actual)

        posicion_actual -=1
        cadena_actual = codigo_fuente[comienzo_lexema:posicion_actual]
        tipo_token = TOKENS_DETECTADOS[0]
        token = (tipo_token, cadena_actual)
        tokens.append(token)
    return tokens



#prueba del lexer
output = lexer("var variable1")
print(output)


#prueba para mostrar que da error si hay un caracter no valido
output = lexer("var vari¨able1")
print(output)