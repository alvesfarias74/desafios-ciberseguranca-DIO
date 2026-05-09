# Projeto: Simulação de Malware de Captura de Dados e Medidas de Proteção

Este projeto apresenta o desenvolvimento e a análise de malwares simulados (Ransomware e Keylogger) para fins estritamente educacionais. O objetivo é compreender a mecânica de captura e sequestro de dados em um ambiente 100% controlado, permitindo a identificação de vulnerabilidades e a implementação de estratégias de defesa eficazes.

## 1. Introdução e Conceitos de Malware
Explora-se a definição e o funcionamento básico de softwares maliciosos, com foco em como essas ameaças exploram brechas técnicas e falhas humanas para comprometer sistemas.

## 2. Construção do Ambiente e Ransomware
Realiza-se a configuração de um ambiente seguro para a execução de scripts em **Python**. No cenário de Ransomware, desenvolvem-se funções capazes de criptografar arquivos de teste, simulando o sequestro de informações, e funções de descriptografia para restaurar o acesso aos dados, acompanhadas de uma mensagem de "resgate".

## 3. Desenvolvimento de Keylogger Local
Desenvolve-se um script (`keylogger.pyw`) utilizando a biblioteca `pynput` para monitorar e registrar eventos do teclado. 
- **Lógica de Captura:** O script identifica teclas alfanuméricas e mapeia teclas especiais (como Space, Enter e Backspace) para garantir que o log gerado seja legível.
- **Filtro de Ruído:** Implementa-se uma estrutura para ignorar teclas modificadoras (Shift, Ctrl, Alt) que não contribuem diretamente para a captura de texto corrido no arquivo `log.txt`.

## 4. Evolução para Keylogger Invisível e Remoto
Aprimora-se a ferramenta para aumentar sua furtividade e capacidade de exfiltração de dados:
- **Execução Furtiva:** Utiliza-se a extensão `.pyw` para permitir que o script seja executado em segundo plano, sem a exibição de janelas de console para o usuário.
- **Exfiltração via SMTP:** No script `keylogger_email.py`, implementa-se o uso das bibliotecas `smtplib` e `email.mime` para enviar os dados capturados automaticamente para um e-mail pré-configurado.
- **Assincronismo:** Utiliza-se a classe `Timer` da biblioteca `threading` para realizar o envio periódico dos logs (ex: a cada 60 segundos) sem interromper a captura das teclas em tempo real.

## 5. Exportação de Dados e Análise em Ambiente Controlado
Realiza-se o teste final do script, validando a recepção remota das informações capturadas e a integridade dos dados exportados, simulando o ciclo completo de um ataque de captura de dados.

## 6. Estratégias de Defesa e Prevenção
Documentam-se as medidas essenciais para mitigar os riscos apresentados pelos malwares estudados:
- **Soluções Técnicas:** Utilização de Antivírus atualizados, Firewalls ativos e técnicas de *Sandboxing* para análise de arquivos suspeitos.
- **Segurança de Aplicação:** Boas práticas no desenvolvimento de código e gerenciamento de permissões de sistema.
- **Fator Humano:** Conscientização do usuário final para evitar o download de executáveis de fontes não confiáveis e o reconhecimento de ataques de engenharia social.

---

**Este desafio de projeto integra o Bootcamp de Cibersegurança da DIO realizado em parceria com a Riachuelo.**
```