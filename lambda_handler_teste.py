
# coding: utf-8

# In[ ]:


import json
import codecs
#from bs4 import BeautifulSoup
from urllib.request import urlopen
from io import StringIO
#from __future__ import print_function # Python 2/3 compatibility
import boto3
import io

def lambda_handler(event, context):
     # TODO implement
    #get = urlopen("https://br.search.yahoo.com/search?fr=mcafee&type=E211BR885G10&p=gogle")
    
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    # Define data
 
    data = {
            'numeroID':'0026087-34.2000.8.26.0053',
            'numero_processo':'0026087-34.2000.8.26.0053',
            'valor_causa':'R$ 4.886.228,30',
            'classe':'Procedimento Comum Cível',
            'juiz':'Wellington Urbano Marinho',
            'partes':'Reqte:Adolpho Onofre Galliano Advogado: Tiago Henrique dos Santos Gois Reqdo:Prefeitura de São Paulo Reqdo:DEPARTAMENTO ESTADUAL DE TRÂNSITO DE SÃO PAULO - DETRAN',
            'ultima_movimentacao':'03/09/2019 Recebidos os Autos do Distribuidor local\n\t\t\t\n\t\t \n\t\t \n\t\t\n\n\t\t\t"A tramitação se dará nos incidentes digitais em andamento, onde prosseguirá com peticionamento eletrônico. Os autos ficarão à disposição em cartório para eventual consulta pelo prazo de 30 dias a contar da movimentação do recebimento nesta  Unidade.'
        }  
   
     # Create an S3 client
    s3 = boto3.resource('s3')
    file_name = '0026087-34.2000.8.26.0053'
    bucket = 'processosjson'
    
    obj = s3.Object(bucket, file_name)
    obj.put(Body=json.dumps(data))
    
    #path="https://br.search.yahoo.com/search?fr=mcafee&type=E211BR885G10&p=gogle"
    #file=codecs.open(path,"rb")
    #file1=file.read()
    #file1=str(file1)
    
    #with open(file1, "rb") as f:
    #    s3.upload_fileobj(f, bucket, file1)

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('processos')
    
    #Insert the Object
    
    table.put_item(
        Item={
            'numeroID':'0026087-34.2000.8.26.0053',
            'numero_processo':'0026087-34.2000.8.26.0053',
            'valor_causa':'R$ 4.886.228,30',
            'classe':'Procedimento Comum Cível',
            'juiz':'Wellington Urbano Marinho',
            'partes':'Reqte:Adolpho Onofre Galliano Advogado: Tiago Henrique dos Santos Gois Reqdo:Prefeitura de São Paulo Reqdo:DEPARTAMENTO ESTADUAL DE TRÂNSITO DE SÃO PAULO - DETRAN',
            'ultima_movimentacao':'03/09/2019 Recebidos os Autos do Distribuidor local\n\t\t\t\n\t\t \n\t\t \n\t\t\n\n\t\t\t"A tramitação se dará nos incidentes digitais em andamento, onde prosseguirá com peticionamento eletrônico. Os autos ficarão à disposição em cartório para eventual consulta pelo prazo de 30 dias a contar da movimentação do recebimento nesta  Unidade.'
        }  
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }

