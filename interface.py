import graphics as gf
import random as rd
from graphics import *

###
def criar_botao (place_holder, x1, y1, x2, y2):
    novo_botao = gf.Rectangle(gf.Point(x1, y1),gf.Point(x2, y2))
    novo_botao.setFill("white")
    novo_botao.draw(win)    
    texto = gf.Text(novo_botao.getCenter(), place_holder)
    texto.setSize(15)
    texto.draw(win)
    return novo_botao
    
def criar_entrada ( x1, y1, comprimento):
    entrada = gf.Entry(gf.Point(x1, y1), comprimento) 
    entrada.setSize(15)
    entrada.draw(win)
    return entrada

def criar_aviso_saida( x1, y1):
    saida = gf.Text(gf.Point(x1, y1), "")
    saida.setTextColor("red")
    saida.setSize(13)
    saida.draw(win)
    return saida
    
def titulo_principal(texto, x1, y1):
    tit_pri = gf.Text(gf.Point(x1, y1), texto)
    tit_pri.setFace("times roman")  
    tit_pri.setStyle("bold")
    tit_pri.setSize(25)
    tit_pri.draw(win)

def titulo_secundario(texto, x1, y1):
    tit_sec = gf.Text(gf.Point(x1, y1), texto)
    tit_sec.setFace("courier")
    tit_sec.setStyle("bold")
    tit_sec.setSize(25)
    tit_sec.draw(win)
    
def titulo_interno(texto, x1, y1):
    tit_sec = gf.Text(gf.Point(x1, y1), texto)
    tit_sec.setFace("courier")
    tit_sec.setStyle("bold")
    tit_sec.setSize(15)
    tit_sec.draw(win)
    
def criar_item_saida( x1, y1):
    saida = gf.Text(gf.Point(x1, y1), "")
    saida.setTextColor("black")
    saida.setSize(15)
    saida.draw(win)
    return saida
###        
def clique_botao(botao, onde_cliquei):
    if onde_cliquei.getX() >= botao.getP1().getX() and onde_cliquei.getX() <= botao.getP2().getX():
        if onde_cliquei.getY() >= botao.getP1().getY() and onde_cliquei.getY() <= botao.getP2().getY():
            return True
        
    return False

##Validações de entradas 
def check_input(var, saida_var):
    if len(var.getText()) == 0:
        saida_var.setText("Inválido")
        return False
    saida_var.setText("")
    return True

def check_numero(var, saida_var):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    var = var.getText()
    for letra in str(var):
        if letra not in numeros :
            saida_var.setText("Somente Numero")
            return False
    saida_var.setText("")
    return True

def check_preco(var, saida_var, preco_final):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    var = var.getText()
    preco = []
    if "," in var:
        preco = var.split(",")
    elif "." in var:
        preco = var.split(".")
    else :
        preco.append(var)    
    for i in range(len(preco)):
        for n in preco[i]:
            if n not in numeros:
                saida_var.setText("Somente numero!")
                return False
    preco_final = ""
    if len (preco) > 1:
        preco_final = preco[0] + "." + preco[1]
    else :
        preco_final = preco[0]
    saida_var.setText("")
    return preco_final

def check_repetido(var, saida_var):
    lista_arquivo_velho = ler_arquivo()
    var = var.getText()
    for x in lista_arquivo_velho:
        if x[0] == var or x[1] == var:
            saida_var.setText("Já registrado!")
            return False
    saida_var.setText("")
    return True
    
def check_existe(registrar_venda_id, registrar_venda_nome, saida_var):
    lista_arquivo_velho = ler_arquivo()
    venda_id = registrar_venda_id.getText()
    venda_nome = registrar_venda_nome.getText()
    
    for item in lista_arquivo_velho:
        if item[0] == venda_id or item[1] == venda_nome:
            saida_var.setText("")
            return True
    if len(venda_id) > 0 or len(venda_nome) > 0 :
        saida_var.setText("Item não encontrado")
        return False
    saida_var.setText("")
    return False

##
def ler_arquivo ():
    with open("planilhateste.csv", "r", encoding="utf-8") as arq:
        lista_dos_arquivos = arq.readlines()
    lista_arquivo_velho = []
    for linha in lista_dos_arquivos:
        linha_suja = linha.strip()
        linha_limpa = linha_suja.split(";")
        lista_arquivo_velho.append(linha_limpa)        
    return lista_arquivo_velho
               

def registrar_novo_item(nome_novo_produto, quantidade_novo_produto, preco_final, id_novo_produto):    
    lista_arquivo_velho = ler_arquivo()
     
    novo_item = [
         str(id_novo_produto.getText()).strip(),
         str(nome_novo_produto.getText()).strip(),
         str(quantidade_novo_produto.getText()).strip(),
         str(preco_final).strip()
        ]
        
    lista_arquivo_velho.append(novo_item)
    with open("planilhateste.csv", "w", encoding="utf-8") as arq:
        for linha in lista_arquivo_velho:
            linha_formatada = str(linha[0]) +";"+ str(linha[1]) +";"+ str(linha[2]) +";"+ str(linha[3]) +"\n"
            arq.write(linha_formatada)
    return True
    
    
def  mostrar_procurar_venda(registrar_venda_id, registrar_venda_nome, saida_mostrar_item):
    lista_arquivo_velho = ler_arquivo()
    venda_id = registrar_venda_id.getText()
    venda_nome = registrar_venda_nome.getText()
    
    for item in lista_arquivo_velho:
        if item[0] == venda_id or item[1] == venda_nome:
            if len(item[1]) > 75 :
                ponto = "..."
            else:
                ponto = ""
            saida_mostrar_item.setText(f"{item[1][:75]}{ponto}\nPreço:R${item[3]} Quantidade no estoque: {item[2]} ID:{item[0]}")
            return

    
def registrar_venda(registrar_venda_id, registrar_venda_nome, registrar_venda_quantidade, saida_venda_item):
    lista_arquivo_velho = ler_arquivo()
    venda_id = registrar_venda_id.getText()
    venda_nome = registrar_venda_nome.getText()
    venda_quantidade = registrar_venda_quantidade.getText()
    
    if len(venda_quantidade) < 1:
        saida_venda_item.setText("Quantidade inválida")
        return False
    else:
        saida_venda_item.setText("")
    
    for item in lista_arquivo_velho:
        if item[0] == venda_id or item[1] == venda_nome:
            if int(item[2]) < int(venda_quantidade):
                saida_venda_item.setText(f"Nâo tem {venda_quantidade} no estoque!")
                return
            else:
                item[2] = int(item[2]) -int(venda_quantidade)
                saida_venda_item.setText("Venda registrada.")

    with open("planilhateste.csv", mode="w", encoding="utf-8") as arq:
        for linha in lista_arquivo_velho:
            linha_formatada = str(linha[0]) +";"+ str(linha[1]) +";"+ str(linha[2]) +";"+ str(linha[3]) +"\n"
            arq.write(linha_formatada)
    return
def procurar_nome_similar_funcao(procurar_nome_similar, saida_procurar_nome_similar_um):
    procurar_nome = procurar_nome_similar.getText().strip()
    procurar_nome = procurar_nome.split()
    lista_arquivo_velho = ler_arquivo()
    
    sim_primeira = 0
    sim_segunda = 0
    sim_terceira = 0
    
    saida_primeira = ""
    saida_segunda = ""
    saida_terceira = ""
    
    for item in lista_arquivo_velho[1:]:
        item_lista = item[1].strip()
        
        item_lista = item_lista.split()
        em_comum = 0
        for string in item_lista:
            
            if string in procurar_nome:
                em_comum += 1
            
        if em_comum > sim_primeira:
            saida_terceira = saida_segunda
            saida_segunda = saida_primeira
            
            if len(item[1]) > 50 :
                ponto_1 = "..."
            else:
                ponto_1 = ""
                
            saida_primeira = f"{item[1][:50]}{ponto_1};Qtd:{item[2]}; ID:{item[0]}"
                
            sim_terceira = sim_segunda
            sim_segunda = sim_primeira
            sim_primeira = em_comum
                           
        elif em_comum > sim_segunda:
            saida_terceira = saida_segunda
            
            if len(item[1]) > 50 :
                ponto_2 = "..."
            else:
                ponto_2 = ""
                
            saida_segunda = f"{item[1][:50]}{ponto_2};Qtd:{item[2]}; ID:{item[0]}"
                
            sim_terceira = sim_segunda
            sim_segunda = em_comum
                
        elif em_comum > sim_terceira:
            
            if len(item[1]) > 50 :
                ponto_3 = "..."
            else:
                ponto_3 = ""
                
            saida_terceira  = f"{item[1][:50]}{ponto_3};Qtd:{item[2]}; ID:{item[0]}"         
            
            sim_terceira = em_comum
              
    output = f"{saida_primeira}\n{saida_segunda}\n{saida_terceira}"          
    saida_procurar_nome_similar_um.setText(output)
    return
    
def  gerar_lista_txt(nome_lista_txt, saida_gerar_lista):
    nome_lista = nome_lista_txt.getText()
    if len(nome_lista) < 1 :
        saida_gerar_lista.setText("Digite o nome do arquivo.")
        return False
    else:
        saida_gerar_lista.setText("")
        
    lista_arquivo = ler_arquivo()[1:]
    
    maior_len_id = len("ID")
    maior_len_nome = len("Nome")
    maior_len_quantidade = len("Quantidade")
    maior_len_preco = len("preco")
    
    for item in lista_arquivo:
        if len(item[0]) > maior_len_id:
            maior_len_id = len(item[0])
        
        if len(item[1]) > maior_len_nome:
            maior_len_nome = len(item[1])
            
        if len(item[2]) > maior_len_quantidade:
            maior_len_quantidade = len(item[2])
        
        if len(item[3]) > maior_len_preco:
            maior_len_preco = len(item[3])
    
    output = " " * (maior_len_id - len("id")) + " ID |" + " " * (maior_len_nome - len("nome")) + " Nome |" + " " * (maior_len_quantidade - len("quantidade"))
    output += " Quantidade |" + " " * (maior_len_preco - len("preco")) + " Preço" +"\n"
    
    for item in lista_arquivo:
        output += " " * (maior_len_id - len(item[0])) + f" {item[0]} |"
        output += " " * (maior_len_nome - len(item[1])) + f" {item[1]} |"
        output += " " * (maior_len_quantidade - len(item[2])) + f" {item[2]} |"
        output += " " * (maior_len_preco - len(item[3])) + f" {item[3]}\n" 

    with open(f"{nome_lista}.txt", mode="w", encoding="utf-8") as file:
        file.write(output)
    saida_gerar_lista.setText("Arquivo adicionado.")
    return True


def gerar_lista_gf(saida_gerar_gf):
    lista_arquivo = ler_arquivo()[1:]

    output = ""
    len_linha = 0 
    saida_gerar_gf.setText("")
    for index in range(len(lista_arquivo)):
        ponto = ""
        if len(lista_arquivo[index][1]) > 45 :
            ponto = "..."
        output_linha = "ID: " + (lista_arquivo[index][0]) + f" {lista_arquivo[index][1][:45]}{ponto} "+ f" Qtd: {lista_arquivo[index][2]}" 
        output += output_linha
        len_linha += len(output_linha)
        
        if  len_linha >= 30:
            output += "\n"
            len_linha = 0    
    
    saida_gerar_gf.setText(output)
    return saida_gerar_gf

#####
rd.seed()
win = gf.GraphWin("Janela do E-Commerce", 1536 , 864)
###
titulo_principal("Sistema de Gestão", 200, 30)
#
titulo_secundario("Registrar novo item", 260, 90)

titulo_interno ("Nome:", 120, 130)
nome_novo_produto = criar_entrada ( 250, 130, 15)
saida_nome_novo_produto = criar_aviso_saida ( 390, 130)


titulo_interno ("Quantidade:", 155, 160)
quantidade_novo_produto = criar_entrada ( 280, 160, 10)
saida_quantidade_novo_produto = criar_aviso_saida ( 400, 160)

titulo_interno ("Preço:", 125, 190)
preco_novo_produto = criar_entrada ( 220, 190, 10)
saida_preco_novo_produto = criar_aviso_saida ( 340, 190)

titulo_interno ("ID:", 125, 220)
id_novo_produto = criar_entrada (  220, 220, 10)
saida_id_novo_produto = criar_aviso_saida ( 340, 220)

botao_registrar_novo_item = criar_botao ("Registrar novo item", 250, 250, 450, 280)
saida_registrar_produto = criar_item_saida(340, 290)
##

titulo_secundario("Registrar venda do item", 260, 400)

titulo_interno ("Procurar por ", 120, 440)
titulo_interno ("ID:", 75, 480)
registrar_venda_id = criar_entrada ( 160, 480, 10)

titulo_interno ("ou por", 280, 480)
titulo_interno ("Nome:", 370, 480)
registrar_venda_nome = criar_entrada (470, 480, 10)

botao_procurar_item = criar_botao("Procurar Item", 550, 460, 675, 500)
saida_procurar_item = criar_aviso_saida ( 600, 510)
saida_mostrar_item = criar_item_saida( 400, 540)

titulo_interno ("Quantidade", 105, 600)
registrar_venda_quantidade = criar_entrada ( 250, 600, 10)

botao_registrar_venda = criar_botao("Registrar venda do item", 320, 580, 540, 620)
saida_venda_item = criar_item_saida( 450, 640)
##

titulo_secundario("Procurar Item", 1150, 90)
titulo_interno ("Nome:", 1000, 130)
procurar_nome_similar= criar_entrada ( 1110, 130, 13)
botao_procurar_nome_similar = criar_botao("Procurar por nome", 1200, 115, 1400, 145)
titulo_interno ("Resultados:", 1000, 160)
saida_procurar_nome_similar_um = criar_item_saida( 1175, 220)
##

titulo_secundario("Ver inventório", 1150, 300)

titulo_interno ("Gerar arquivo .txt (nome):", 1100, 350)
nome_lista_txt = criar_entrada (1300, 350, 10)
botao_gerar_lista = criar_botao("Gerar Arquivo", 1370, 335, 1500, 365)
saida_gerar_lista = criar_item_saida( 1300, 400)

botao_gerar_lista_gf = criar_botao("Gerar Lista", 1000, 380,  1150,  420)
saida_gerar_gf = criar_item_saida( 1170, 710)

while True:
    onde_cliquei = win.getMouse()
    #
    if clique_botao(botao_registrar_novo_item, onde_cliquei):
        if check_input(nome_novo_produto, saida_nome_novo_produto) and  check_input(quantidade_novo_produto, saida_quantidade_novo_produto) and check_input(preco_novo_produto, saida_preco_novo_produto) and check_input(id_novo_produto, saida_id_novo_produto):
            if (check_numero(quantidade_novo_produto, saida_quantidade_novo_produto)  and check_numero(id_novo_produto, saida_id_novo_produto)):
                preco_final = ""
                preco_final = check_preco(preco_novo_produto, saida_preco_novo_produto, preco_final)
                if preco_final != False:
                    if check_repetido(id_novo_produto, saida_id_novo_produto) and check_repetido(nome_novo_produto, saida_nome_novo_produto):
                        if registrar_novo_item(nome_novo_produto, quantidade_novo_produto, preco_final, id_novo_produto):
                            saida_registrar_produto.setText("Novo item registrado")
    else:
        saida_registrar_produto.setText("")
    #
    if clique_botao(botao_procurar_item, onde_cliquei):
        if check_existe(registrar_venda_id, registrar_venda_nome, saida_procurar_item):
            mostrar_procurar_venda(registrar_venda_id, registrar_venda_nome, saida_mostrar_item)
    else:
        saida_mostrar_item.setText("")

    if clique_botao(botao_registrar_venda, onde_cliquei):        
        if check_existe(registrar_venda_id, registrar_venda_nome, saida_procurar_item):
            if check_numero(registrar_venda_quantidade, saida_venda_item):
                registrar_venda(registrar_venda_id, registrar_venda_nome, registrar_venda_quantidade, saida_venda_item)
    else:
        saida_venda_item.setText("")
    #       
    if clique_botao(botao_procurar_nome_similar, onde_cliquei):
        procurar_nome_similar_funcao(procurar_nome_similar ,saida_procurar_nome_similar_um)
    #
    if clique_botao(botao_gerar_lista, onde_cliquei):
        gerar_lista_txt(nome_lista_txt, saida_gerar_lista)
    else:
        saida_gerar_lista.setText("")
    #
    if clique_botao(botao_gerar_lista_gf, onde_cliquei):
        gerar_lista_gf(saida_gerar_gf)
    