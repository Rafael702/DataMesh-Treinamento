import json
import boto3

def lambda_handler(event, context):
    caminho_do_arquivo_local = "/tmp/arquivo.txt"
    nome_do_arquivo_local = "arquivo.txt"
    nome_do_s3 = "mugnos-it-s3-bucket-v2"
    
    #1 - Criar arquivo
    arquivo = open(caminho_do_arquivo_local, 'w')
    arquivo.write('linha 1 \n')
    arquivo.write('linha 2 \n')
    arquivo.write('linha 3 \n')
    arquivo.close()

    #3 - Realizar upload no s3
    s3 = boto3.client('s3')
    with open(caminho_do_arquivo_local, "rb") as f:
        s3.upload_fileobj(f, nome_do_s3, nome_do_arquivo_local)
