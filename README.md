# LerProcesso

Essa API tem por função receber um arquivo HTML de processo jurídicos, processa-lo, armazena-lo e devolver os dados em forma JSON.

Vide arquivos anexos dos programas e imagens de exemplos das funcionalidades e ferramentas.

ATENÇÂO: A API não está finalizada e está habilitada somente para teste na função GET. Ou seja, ainda não está funcional conforme a descrição acima. Segue abaixo o endpoint para execução da API e retorno.

O programa LerProcesso.py retrata o crawler para leitura de arquivo html, leitura dos dados do processo e disponibilização em formato JSON.

O programa lambda_handler_teste.py retrata o programa de teste de tratamento e inserção dos dados. Consiste em gravar os dados de processo no DynamoDB, estruturação dos dados em formato JSON, gravação do arquivo JSON no bucket S3 e resposta dos dados do processo também em formato JSON.

Endpoint para teste:  https://iweujy4w98.execute-api.us-east-1.amazonaws.com/getV1
