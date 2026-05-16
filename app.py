import streamlit as st

# Configuración de la página
st.set_page_config(page_title="CAPM Calculator", layout="centered")

# ---------------------------
# ESTILOS PERSONALIZADOS
# ---------------------------
st.markdown("""
<style>

/* Sidebar color azul claro */
[data-testid="stSidebar"] {
    background-color: #ADD8E6;
}

/* Botón naranja intenso */
div.stButton > button {
    background-color: #FF6600;
    color: white;
    font-weight: bold;
    border-radius: 8px;
}

/* Mensaje éxito verde fuerte */
.success-box {
    background-color: #008000;
    color: white;
    padding: 10px;
    border-radius: 8px;
    font-weight: bold;
}

/* Resultado fondo negro, letras blancas */
.result-box {
    background-color: black;
    color: white;
    padding: 20px;
    border-radius: 10px;
    font-size: 20px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# TÍTULO PRINCIPAL
# ---------------------------
st.title("📈 Calculadora CAPM")

st.write("Modelo de Valoración de Activos (CAPM)")

# ---------------------------
# SIDEBAR INPUTS
# ---------------------------
st.sidebar.header("Parámetros de entrada")

rf = st.sidebar.number_input(
    "Tasa libre de riesgo (%)",
    min_value=0.0,
    value=5.0
)

beta = st.sidebar.number_input(
    "Beta (β)",
    min_value=0.0,
    value=1.0
)

rm = st.sidebar.number_input(
    "Rendimiento del mercado (%)",
    min_value=0.0,
    value=10.0
)

# ---------------------------
# BOTÓN
# ---------------------------
if st.button("Calcular CAPM"):
    
    # Conversión a decimal
    rf_dec = rf / 100
    rm_dec = rm / 100
    
    # Fórmula CAPM
    capm = rf_dec + beta * (rm_dec - rf_dec)
    
    # Resultado en porcentaje
    capm_result = capm * 100

    # Mensaje éxito
    st.markdown('<div class="success-box">Cálculo realizado correctamente</div>', unsafe_allow_html=True)

    # Resultado en caja negra
    st.markdown(
        f'<div class="result-box">Rendimiento Esperado (CAPM): {capm_result:.2f} %</div>',
        unsafe_allow_html=True
    )
