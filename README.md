# Service B
Serviço assíncrono em Docker que consome informações do RabbitMQ e insere no S3 AWS.

Para execução deste serviço deverá ser utilizado Docker conforme passos abaixo para criação dos containers.

----------------------------------------------------------------------------------------------
1- Criar container rabbitmq (Se executou os passos da outra ponta (https://github.com/rogeriolopes16/ServiceA) não será necessário executar este):

docker run -d --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management

Acessar: http://localhost:15672/

-----------------------------------------------------------------------------------------------

2 - Criar container Serviço

Baixar Imagem Docker: docker pull rogeriol16/serviceb

Criar container: docker run -d --name container_serviceb --link rabbitmq rogeriol16/serviceb

-----------------------------------------------------------------------------------------------

Após subir os containes, o serviço estará ativo "escutando" o RabbitMQ e assim que receber algum notificação fará captura e inclusão no S3 AWS.

OBSERVAÇÃO: Existe o serviço da outra ponta, onde faz o input das notificações navegador e insere no RabbitMQ, que pode ser verificado atraves do repositório abaixo:

https://github.com/rogeriolopes16/ServiceA
