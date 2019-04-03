# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:04:25 2019

@author: Rodrigo
"""

import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
import sqlite3

# conectando...
conn = sqlite3.connect('enel2.db')
#definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE enel (
        cpf     TEXT NOT NULL,
        UC TEXT 
        
);
""")

conn.close()


print('Tabela criada com sucesso.')



with open('cpf3.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for cpf in reader:
        if cpf[2] == 'RJ':
            
                driver = webdriver.PhantomJS('phantomjs.exe')
                driver.get('https://www.enel.com.br/pt/servico/consultar-numero-cliente.html')
                rio = driver.find_element_by_xpath('//*[@id="localizatorbuttons"]/div/a[1]')
                rio.click()
                driver.get('http://eneldistribuicao.com.br/rj/AgenciaVirtual.aspx')
                cliente = driver.find_element_by_xpath('//*[@id="ctl02"]/div[4]/div[3]/div[1]/a[4]')
                cliente.click()
                name = driver.find_element_by_xpath('//*[@id="firstname"]')
                name.send_keys(cpf[1])
                user = driver.find_element_by_xpath('//*[@id="contractnumber"]')
                user.send_keys(cpf[0])
                close_ = driver.find_element_by_xpath('/html/body/div[5]/div/button')
                close_.click()
                sleep(0.5)
                sign_in_button = driver.find_element_by_xpath('//*[@id="main"]/div/div/section/form/div/div[4]/input')
                sign_in_button.click()
                sleep(10)
                sel = Selector(text=driver.page_source)
                UC = sel.xpath('//*[@id="main"]/div/div/section/form/div/div[5]/ul/li/text()').extract_first()
                if UC:
                    UC = UC.strip()
                print (cpf[0],UC, "miliaciano ou favelado")
                conn = sqlite3.connect('enel2.db')
                cursor = conn.cursor()
                cursor.execute("""
                               INSERT INTO enel (cpf, UC)
                               VALUES (?,?)
                               """, (cpf[0],UC))
                conn.commit()
                print('Dados inseridos com sucesso.')

                conn.close()
                driver.quit()
            
        elif cpf[2] == 'GO':
            try:
                driver = webdriver.PhantomJS('phantomjs.exe')
                driver.get('https://www.eneldistribuicao.com.br/go/ConsultarUnidadeConsumidora.aspx')
                user = driver.find_element_by_xpath('//*[@id="CONTENT_consultaucgo_Documento"]')
                user.send_keys(cpf[0])
                sign_in_button = driver.find_element_by_xpath('//*[@id="CONTENT_consultaucgo_Enviar"]')
                sign_in_button.click()
                sleep(4)
                sel = Selector(text=driver.page_source)
                UC = sel.xpath('//*[@id="CONTENT_consultaucgo_gridUC_gridLblUC_0"]/text()').extract_first()
                if UC:
                    UC = UC.strip()
                print (cpf[0],UC, "roedor de pequi")
                conn = sqlite3.connect('enel2.db')
                cursor = conn.cursor()
                cursor.execute("""
                               INSERT INTO enel (cpf, UC)
                               VALUES (?, ?)
                               """, (cpf[0],UC))
                conn.commit()
                print('Dados inseridos com sucesso.')

                conn.close()
                driver.quit()
            except:
                pass
        else:
            try:
                driver = webdriver.PhantomJS('phantomjs.exe')
                driver.get('https://www.enel.com.br/pt-ceara/servico/consultar-numero-cliente.html')
                rio = driver.find_element_by_xpath('//*[@id="localizatorbuttons"]/div/a[2]')
                rio.click()
                driver.get('http://eneldistribuicao.com.br/ce/AgenciaVirtual.aspx')
                cliente = driver.find_element_by_xpath('//*[@id="ctl02"]/div[4]/div[3]/div[1]/a[4]')
                cliente.click()
                name = driver.find_element_by_xpath('//*[@id="firstname"]')
                name.send_keys(cpf[1])
                user = driver.find_element_by_xpath('//*[@id="contractnumber"]')
                user.send_keys(cpf[0])
                close_ = driver.find_element_by_xpath('/html/body/div[5]/div/button')
                close_.click()
                sleep(0.5)
                sign_in_button = driver.find_element_by_xpath('//*[@id="main"]/div/div/section/form/div/div[4]/input')
                sign_in_button.click()
                sleep(10)
                sel = Selector(text=driver.page_source)
                UC = sel.xpath('//*[@id="main"]/div/div/section/form/div/div[5]/ul/li/text()').extract_first()
                if UC:
                    UC = UC.strip()
                print (cpf[0],UC,"cabeça chata")
                conn = sqlite3.connect('enel2.db')
                cursor = conn.cursor()
                cursor.execute("""
                               INSERT INTO enel (cpf, UC)
                               VALUES (?, ?)
                               """, (cpf[0],UC))
                conn.commit()
                print('Dados inseridos com sucesso.')

                conn.close()
                driver.quit()
            except:
                 pass