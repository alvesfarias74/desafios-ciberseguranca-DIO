# Projeto: Simulação de Ataque de Brute Force com Medusa no Kali Linux

Este projeto apresenta a documentação detalhada de uma auditoria de segurança prática, focada em ataques de força bruta. Utiliza-se um ambiente controlado para explorar vulnerabilidades em serviços de rede e aplicações web, visando o aprendizado de técnicas de pentest e a proposição de medidas de mitigação.

## 1. Configuração do Ambiente Laboratorial
Realiza-se a preparação do cenário de testes utilizando o software de virtualização **VirtualBox**. Configura-se uma rede interna do tipo *host-only* para isolar o tráfego. Utiliza-se o **Kali Linux** como estação atacante e o **Metasploitable 2** como o alvo vulnerável que contém diversos serviços propositalmente expostos.

![Interface de inicialização do Metasploitable 2](.\testes.invasao-medusa\images\img%20(1).png)

## 2. Reconhecimento de Rede e Conectividade
Inicia-se a fase de reconhecimento com a identificação do endereço IP da máquina alvo através do comando `ip a` no terminal do Metasploitable 2. Em seguida, executa-se o comando `ping` no Kali Linux para validar a comunicação bidirecional entre as máquinas, garantindo que o alvo está alcançável na rede interna.

![Identificação do endereço IP do alvo](.\testes.invasao-medusa\images\img%20(3).png)
**

![Validação de conectividade via comando Ping](.\testes.invasao-medusa\images\img%20(4).png)
**

## 3. Varredura de Portas e Serviços (Fingerprinting)
Utiliza-se a ferramenta **Nmap** para realizar uma varredura abrangente no IP alvo. O comando identifica as portas TCP abertas e tenta determinar as versões dos serviços em execução, como FTP (porta 21), SSH (porta 22), HTTP (porta 80) e SMB (porta 445). Esta etapa é crucial para definir os vetores de ataque subsequentes.

![Resultado da varredura de serviços com Nmap](.\testes.invasao-medusa\images\img%20(5).png)
**

## 4. Exploração do Serviço FTP
Após a detecção do serviço FTP, tenta-se um acesso manual que resulta em falha, confirmando a necessidade de uma abordagem automatizada. Procede-se com a criação de listas de usuários e senhas (*wordlists*) customizadas utilizando comandos de redirecionamento de texto no terminal. Por fim, valida-se o acesso administrativo ao servidor de arquivos após a descoberta das credenciais corretas.

![Falha na tentativa de autenticação manual](.\testes.invasao-medusa\images\img%20(6).png)
**

![Geração de wordlists para o ataque de força bruta](.\testes.invasao-medusa\images\img%20(7).png)
**

![Confirmação de acesso bem-sucedido ao serviço FTP](.\testes.invasao-medusa\images\img%20(8).png)
**

## 5. Força Bruta em Formulário Web (DVWA)
Direciona-se o ataque para a aplicação **DVWA (Damn Vulnerable Web Application)**. Analisa-se o tráfego HTTP através das ferramentas de desenvolvedor do navegador para capturar os parâmetros exatos do formulário de login (usuário, senha e botão de submissão). Com esses dados, configura-se o **Medusa** para testar as combinações de credenciais contra a página de autenticação, identificando as contas válidas.

![Captura e análise de parâmetros HTTP no navegador](.\testes.invasao-medusa\images\img%20(12).png)
**

![Execução do Medusa contra o formulário web da DVWA](.\testes.invasao-medusa\images\img%20(10).png)
**

## 6. Enumeração e Password Spraying em SMB
Executa-se o utilitário `enum4linux` para extrair informações detalhadas do protocolo SMB, o que permite listar usuários legítimos presentes no sistema alvo. Com a lista de usuários em mãos, aplica-se a técnica de **password spraying** utilizando o Medusa; nesta técnica, testa-se uma única senha comum contra múltiplos usuários para evitar o bloqueio de contas. A eficácia é comprovada ao listar os compartilhamentos de rede disponíveis através do `smbclient`.

![Início do processo de enumeração de usuários SMB](.\testes.invasao-medusa\images\img%20(15).png)
**

![Lista de usuários identificados pelo enum4linux](.\testes.invasao-medusa\images\img%20(17).png)
**

![Ataque de Password Spraying resultando em sucesso](.\testes.invasao-medusa\images\img%20(19).png)
**

![Visualização dos diretórios compartilhados via SMB](.\testes.invasao-medusa\images\img%20(20).png)
**

---

**Este desafio de projeto foi realizado como parte do Bootcamp de Cibersegurança da DIO em parceria com a Riachuelo.**
```
