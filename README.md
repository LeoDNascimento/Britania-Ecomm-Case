# 📊 Streamlit – Upload, Data Quality & Transformações

Este módulo é responsável pela **camada de apresentação e validação de dados** do projeto.  
Ele permite o upload de arquivos CSV, aplica **validações de Data Quality** e executa **transformações padronizadas**, liberando o envio dos dados **apenas quando todos os critérios são atendidos**.

---

## 🎯 Objetivo

- Receber arquivos CSV de pedidos
- Garantir **qualidade dos dados antes da ingestão**
- Padronizar informações conforme regras de negócio
- Evitar envio de dados inválidos para a API

---

## 🧱 Funcionalidades

### 📥 Upload de CSV
- Interface gráfica para seleção de arquivos `.csv`
- Leitura tolerante a formatos brasileiros/europeus:
  - Separador de colunas: `;`
  - Separador de milhar: `,`
  - Separador decimal: `.`

---

### ✅ Validações de Data Quality

As validações são executadas **em camadas**, interrompendo o fluxo ao primeiro erro identificado.

#### 1. Validação de Schema
Garante a presença **exata** das colunas esperadas:

| Coluna | Tipo esperado |
|------|--------------|
| id_pedido | int |
| cliente | str |
| valor | float |
| status | str |

- Detecta colunas ausentes
- Detecta colunas extras

---

#### 2. Validação de Tipos
Valida **linha a linha** se os dados podem ser convertidos para os tipos esperados.

Exemplo de erro reportado:
Linha 12: valor inválido na coluna 'valor'


---

#### 3. Validação de Domínio
Garante que o campo `status` esteja dentro do domínio permitido:

- PENDENTE / PENDING
- APROVADO / APPROVED
- CANCELADO / CANCELED / CANCELLED

Erros são exibidos com **número exato da linha**.

---

### Transformações de Dados

As transformações **só são executadas se todas as validações passarem**.

#### Transformações aplicadas:
- Padronização de `status` para **PT-BR e MAIÚSCULO**
- Conversão explícita de tipos:
  - `id_pedido` → `int`
  - `valor` → `float`
- Remoção de separadores de milhar
- Limpeza de espaços em campos textuais

---

###  Controle de Fluxo

- Se qualquer erro for encontrado:
  - O pipeline é interrompido
  - O botão de envio **não é exibido**
- O envio só é permitido quando os dados estão **100% válidos**

---

### Envio para API

Após validações e transformações:
- O botão **“Enviar pedidos para a API”** é exibido
- Os dados enviados já estão padronizados e prontos para ingestão

---

##  Estrutura de Pastas

```text
streamlit_app/
├── app.py
├── requirements.txt
├── README.md
│
├── data_quality/
│   ├── schema.py        # Definição do schema esperado
│   ├── validators.py   # Validações de Data Quality
│   └── transforms.py   # Transformações de dados
│
└── services/
    └── api_client.py   # Cliente para envio à API

