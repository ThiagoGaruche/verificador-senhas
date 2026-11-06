# 🔑 Verificador de Força e Vazamento de Senhas

Um script em Python projetado para avaliar a segurança de senhas de duas formas complementares: **cálculo de entropia matemática** e **checagem contra vazamentos de dados públicos**.

---

## 🚀 Funcionalidades

- **📐 Entropia Estimada:** Calcula a quantidade de bits de entropia com base no tamanho da senha e na diversidade dos tipos de caracteres utilizados (letras minúsculas, maiúsculas, números e símbolos).
- **🏷️ Classificação da Senha:** Categoriza automaticamente a força da senha como *Fraca*, *Razoável*, *Forte* ou *Muito Forte*.
- **🔍 Checagem de Vazamentos:** Integração com a API do *Have I Been Pwned* para verificar se a senha já foi exposta em incidentes de segurança.
- **🙈 Entrada Segura:** Utiliza o módulo `getpass` para que a senha digitada não seja exibida na tela do terminal.

---

## 🛡️ Como Funciona o k-Anonimato (k-Anonymity)

A sua senha **nunca sai do seu computador**. Para preservar a privacidade e a segurança total do usuário, o script opera da seguinte maneira:

1. Gera o hash **SHA-1** da senha digitada localmente.
2. Envia à API do *Have I Been Pwned* **apenas os 5 primeiros caracteres** desse hash (o prefixo).
3. A API responde com uma lista de todos os sufixos de hashes conhecidos que começam com esse mesmo prefixo.
4. O script compara o restante do hash (o sufixo) **localmente na sua máquina**.

> 💡 **Resultado:** A API nunca descobre qual foi a senha verificada, mantendo o anonimato e o sigilo completo das suas credenciais.

---

## 📦 Instalação

### Pré-requisitos
- Python 3.x instalado.

---

## Aviso ❗

Nunca digite senhas reais em ferramentas em que você não confia. Leia o código antes de usar.
