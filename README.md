# 💸 App de Extração de Transações

Este aplicativo foi desenvolvido em Python utilizando **Streamlit** para facilitar o controle e a organização de transações financeiras. Com uma interface simples e intuitiva, é possível inserir dados de transações, visualizar uma planilha e exportá-la em formato Excel.


## 📋 Funcionalidades

- **Inserção de Transações**: Permite inserir transações financeiras em um campo de texto, respeitando o formato especificado. Cada transação deve estar em uma linha e seguir o modelo: `31/10/2024 PIX_CRED RECEBIMENTO PIX 1234***** Nome Completo 49,00`.
- **Cálculo de Saldo Inicial**: O usuário pode inserir o saldo inicial a ser considerado na planilha.
- **Visualização das Transações**: As transações são exibidas em uma tabela interativa que facilita a análise e edição.
- **Exportação em Excel**: As transações podem ser exportadas para um arquivo `.xlsx` com apenas um clique.

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/ArkaNiightt/Projeto_Transacoes.git
   ```

2. Instale as dependências necessárias utilizando **pip**:
   ```sh
   pip install -r requirements.txt
   ```

3. Execute o aplicativo Streamlit:
   ```sh
   streamlit run app.py
   ```

## 📄 Formato das Transações

Cada transação deve ser inserida no seguinte formato:

```
DD/MM/AAAA TIPO_DOC DESCRIÇÃO VALOR
```

- **Data**: Formato `DD/MM/AAAA` (Ex: `31/10/2024`).
- **Tipo de Documento**: Código identificador da transação (Ex: `PIX_CRED`).
- **Descrição**: Informações adicionais da transação (Ex: `RECEBIMENTO PIX 123456789 Nome Completo`).
- **Valor**: Valor em formato brasileiro (Ex: `49,00`).

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para desenvolver o aplicativo.
- **Streamlit**: Framework usado para construir a interface gráfica.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **XlsxWriter**: Biblioteca para exportar os dados em formato `.xlsx`.
- **Regex**: Para analisar e extrair as partes das transações.

## 🎨 Layout

- O layout do aplicativo foi configurado para ser amigável e intuitivo, contando com elementos visuais como ícones e um banner no topo.
- A imagem do banner é carregada para oferecer uma identidade visual ao aplicativo.

## 📦 Estrutura do Projeto

```
project-root/
│
├── src/
│   └── images/
│       └── header_img.jpg   # Imagem usada como banner
├── app.py                    # Código principal do aplicativo
└── requirements.txt          # Dependências do projeto
```

## 📥 Exportar para Excel

Após adicionar as transações, você pode baixar a planilha gerada no formato `.xlsx` clicando no botão **"📥 Baixar planilha como XLSX"**. Esta funcionalidade facilita o compartilhamento e armazenamento das informações financeiras.

## ⚖️ Saldo Inicial

No menu lateral, insira o saldo inicial desejado. O valor deve ser no formato brasileiro (`ex: 150.342,05`). Este saldo será incluído nas transações para melhor controle financeiro.

## 📊 Planilha de Transações

Após a inserção das transações, você poderá visualizar todas as informações em uma tabela dinâmica que facilita a verificação e análise dos dados.

## 💼 Autor

App desenvolvido por [Seu Nome](https://github.com/seu_usuario) para facilitar o controle de transações financeiras, com foco em simplicidade e praticidade.

## 📜 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

**Organize suas finanças de forma prática e eficiente!** 💰✨

