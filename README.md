# Portfolio de Cibersegurança - Bootcamp DIO & Riachuelo

Este repositório reúne os projetos práticos desenvolvidos durante o **Bootcamp de Cibersegurança**, promovendo a exploração de técnicas de defesa e ataque em ambientes controlados. O foco principal é o entendimento técnico de vulnerabilidades para a construção de sistemas mais resilientes.

## Conteúdo do Repositório

O repositório está organizado em subdiretórios, cada um contendo sua própria documentação detalhada e arquivos de implementação:

### 1. Simulação de Ataque de Brute Force (Medusa)
Neste projeto, realiza-se a simulação de ataques de força bruta contra diversos serviços em um ambiente laboratorial composto por Kali Linux e Metasploitable 2.
- **Técnicas Exploradas:** Varredura de portas com Nmap, ataques ao protocolo FTP, força bruta em formulários web (DVWA) e *password spraying* em serviços SMB.
- **Ferramentas:** Kali Linux, Medusa, Nmap e Enum4linux.
- [Acesse a documentação completa aqui](./testes-de-invasao-medusa/README.md)

### 2. Simulação de Malwares e Captura de Dados (Python)
Este projeto foca no desenvolvimento e análise de malwares simulados utilizando a linguagem **Python** para fins estritamente educacionais. O objetivo é demonstrar como ameaças capturam ou sequestram dados e como implementar defesas reais.
- **Ransomware Simulado:** Implementa-se um script capaz de criptografar e descriptografar arquivos de teste, simulando o sequestro de dados e a geração de mensagens de resgate.
- **Keylogger e Exfiltração:** Desenvolve-se uma ferramenta de captura de teclas que opera de forma furtiva em segundo plano e realiza o envio automático dos logs capturados via e-mail (exfiltração remota).
- **Estratégias de Defesa:** Documentam-se medidas de proteção como o uso de antivírus, firewalls, técnicas de *sandboxing* e a importância da conscientização do usuário contra engenharia social.
- [Acesse a documentação completa aqui](./captura-de-dados/) *(ajuste o link conforme o nome da sua pasta)*

## Objetivos Alcançados
- Compreensão prática do funcionamento de ataques de força bruta e malwares (Ransomware/Keylogger).
- Identificação de como vulnerabilidades técnicas e brechas humanas são exploradas.
- Desenvolvimento de scripts em Python para simulação de ataques em ambientes controlados.
- Reflexão e documentação de estratégias de defesa e prevenção no mundo real.

---

**Este repositório foi desenvolvido como parte do Bootcamp de Cibersegurança da DIO em parceria com a Riachuelo.**
```
