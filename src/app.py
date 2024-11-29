import re
import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image

def parse_transaction(text):
    pattern = r"(\d{2}/\d{2}/\d{4})\s+([A-Z_]+)\s+(.*?)\s+(\d{1,3}(?:\.\d{3})*,\d{2})"
    match = re.match(pattern, text)
    if match:
        data = match.group(1)
        documento = match.group(2)
        historico = match.group(3).strip()
        credito = match.group(4)
        return {
            "Data": data,
            "Documento": documento,
            "Histórico": historico,
            "Crédito": credito,
        }
    else:
        return None

st.set_page_config(
    page_title="Transações Financeiras",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image(
    "src/images/header_img.jpg",
    use_container_width=False,
    caption="",
    output_format="JPEG",
    width=400
)

st.title("💸 App de Extração de Transações")
st.markdown("**Organize suas transações financeiras de maneira rápida e eficiente.**")
st.markdown("---")

if "dataframe" not in st.session_state:
    st.session_state["dataframe"] = pd.DataFrame(
        columns=["Data", "Documento", "Histórico", "Crédito", "Saldo"]
    )

with st.expander("📋 Inserir Transações", expanded=True):
    st.write("Insira as transações no formato adequado (uma por linha):")
    texto = st.text_area(
        "Exemplo: 31/10/2024 PIX_CRED RECEBIMENTO PIX 123456789 Nome Completo 49,00",
        height=200,
    )

with st.sidebar:
    st.header("⚖️ Saldo Inicial")
    saldo_inicial = st.text_input("Insira o saldo inicial:", value="0,00")
    st.markdown("---")

if st.button("Adicionar à Planilha", key="add_button"):
    try:
        saldo_inicial_float = float(saldo_inicial.replace(".", "").replace(",", "."))
        saldo_formatado = (
            "{:,.2f}".format(saldo_inicial_float)
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    except ValueError:
        st.error(
            "Formato de saldo inválido. Use o formato correto, por exemplo: 150.342,05"
        )
    else:
        linhas = texto.split("\n")
        resultados = []
        for linha in linhas:
            linha = linha.strip()
            if linha:
                resultado = parse_transaction(linha)
                if resultado:
                    resultado["Saldo"] = saldo_formatado
                    resultados.append(resultado)

        if resultados:
            st.session_state["dataframe"] = pd.concat(
                [st.session_state["dataframe"], pd.DataFrame(resultados)],
                ignore_index=True,
            )
            st.success("Transações adicionadas com sucesso!")
        else:
            st.error(
                "Nenhuma transação válida encontrada. Verifique o formato dos textos."
            )

st.markdown("### 📊 Planilha de Transações")
st.dataframe(st.session_state["dataframe"], height=300)

def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Transações")
    return output.getvalue()

st.download_button(
    label="📥 Baixar planilha como XLSX",
    data=convert_df_to_excel(st.session_state["dataframe"]),
    file_name="transacoes.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>App desenvolvido para facilitar o controle de transações financeiras. 💼💡</div>",
    unsafe_allow_html=True,
)
