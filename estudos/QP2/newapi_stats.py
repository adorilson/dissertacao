#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Escopo:
    CLASSE = 'Classe'
    METODO = 'Metodo'
    CAMPO = 'Campo'
    CASTING = 'Casting'
    XML = 'XML'

casting = {}
classes = {}
metodos = {}
campos = {}
xml = {}

def print_item(item):
    print(item['api'], ';', item['escopo'], ';', item['descricao'], ';', item['qtd'])

def print_aux(escopo):
    for i in escopo.items():
        print_item(i[1])    

def print_resultado():
    print_aux(casting)
    
    print_aux(classes)
    
    print_aux(metodos)
    
    print_aux(campos)
    
    print_aux(xml)
    
def get_escopo(l):
    if l[:5]=='Class': # View vem de arquivo XML, mas é associada a classe TextureView
        return Escopo.CLASSE
    elif l[:4]=='Call':
        # chamadas a construtores dos objetos são consideradas como classes
        if 'new ' in l: # tem que ser com o espaço após new, pq existem métodos com new no nome
            return Escopo.CLASSE
        else:
            return Escopo.METODO
    elif l[:4]=='Cast':
        return Escopo.CASTING
    elif l[:5]=='Field':
        return Escopo.CAMPO
    elif 'android:' in l:
        return Escopo.XML
    elif 'Attribute' in l:
        return Escopo.XML
    elif '<vector>' in l:
        return Escopo.XML
    elif l[:4]=='View':
        return Escopo.XML
    else:
       raise Exception('Escopo inesperado: ' + l)

def get_api(l):
    try:
        # para situação que a descrição é algo como
        # Call requires API level 23 (...
        # ou
        # ... requires API level 21 ( ...
        s = 'API level '
        index = l.index(s)
    except ValueError:
        # para situações em que a descrição é algo como
        # ... older than API 17 ( ...
        s = 'than API '
        index = l.index(s)
    
    api = l[index+len(s):index+len(s)+2]
    return int(api)

def get_descricao(l):
    try:
        inicio = l.index('`')+1
        if inicio==1 or l[:9]=='Attribute':
            fim = l.index('`', inicio)
            descricao = l[inicio:fim]
        else:    
            fim = len(l)-2
            descricao = l[inicio:fim]
            if descricao[:3]=='new':
                descricao = descricao[4:]
        return descricao
    except ValueError:
        ## É casting...
        fim = l.index('requires')-1
        return l[5:fim]
        
        

arquivo = sys.argv[1]
arquivo = open(arquivo)
linhas = arquivo.readlines()

def atualize(escopo, item):
    descricao = item['descricao']
    if escopo.get(descricao):
        escopo[descricao]['qtd'] = escopo[descricao]['qtd'] + 1  
    else:
        escopo[descricao] = item

# pre-processando as ocorrencias
for l in linhas:
    api = get_api(l)
    escopo = get_escopo(l)
    #print(escopo, l)
    descricao = get_descricao(l)
    item = {
        'api': api,
        'escopo': escopo,
        'descricao': descricao,
        'qtd': 1
    }
    if escopo==Escopo.CASTING:
        atualize(casting, item)
    elif escopo==Escopo.METODO:
        atualize(metodos, item)
    elif escopo==Escopo.CLASSE:
        atualize(classes, item)
    elif escopo==Escopo.CAMPO:
        atualize(campos, item)
    elif escopo==Escopo.XML:
        atualize(xml, item)
         
arquivo.close()

# contabilizando métodos juntos com suas classes
metodos_para_excluir = []
for key in metodos:
    classe = key[:key.index('#')]
    if classe in classes:
        classes[classe]['qtd'] = classes[classe]['qtd'] + metodos[key]['qtd']
        metodos_para_excluir.append(key)
    

# excluindo os metodos que foram contabilizados com as classes...
for m in metodos_para_excluir:
    del metodos[m]

# contabilizando campos juntos com suas classes
campos_para_excluir = []
for key in campos:
    classe = key[:key.index('#')]
    if classe in classes:
        classes[classe]['qtd'] = classes[classe]['qtd'] + campos[key]['qtd']
        campos_para_excluir.append(key) 
    

# excluindo os campos que foram contabilizados com as classes...
for m in campos_para_excluir:
    del campos[m]


print_resultado()
