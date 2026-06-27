import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Calculadora de Horas", page_icon="⚙️", layout="centered")

st.title("⚙️ Calculadora de Horas a Pago")
st.write("Ingresa tus datos del mes para proyectar con cuántas horas vas a quedar.")

# Separamos los inputs en dos columnas para mejor visualización en móviles
col1, col2 = st.columns(2)

with col1:
    dias_habiles = st.number_input("Días hábiles del mes", min_value=1, value=22, step=1)
    horas_notificadas = st.number_input("Horas notificadas", min_value=0.0, value=80.0, step=0.5)

with col2:
    dias_vacaciones = st.number_input("Días de vacaciones", min_value=0, value=0, step=1)
    dias_curso = st.number_input("Días de curso", min_value=0, value=0, step=1)

# Lógica matemática basada en tu fórmula
dias_ausente = dias_vacaciones + dias_curso
dias_efectivos = dias_habiles - dias_ausente

# Evitar división por cero si alguien pone demasiados días de ausencia
if dias_efectivos <= 0:
    st.error("⚠️ Los días de ausencia no pueden ser mayores o iguales a los días hábiles del mes.")
else:
    # Cálculo final: (Horas / Días trabajados) * Días totales del mes
    horas_finales = (horas_notificadas / dias_efectivos) * dias_habiles
    promedio_diario = horas_notificadas / dias_efectivos
    
    st.divider()
    st.subheader("📊 Tu Proyección")
    st.metric(label="Horas Finales a Pago", value=f"{horas_finales:.1f} hrs")
    
    # Un pequeño texto de feedback para que entiendan el porqué del número
    st.info(f"💡 **Detalle:** Estás rindiendo un promedio de **{promedio_diario:.1f} horas por día trabajado**. Al proyectar ese ritmo a los {dias_habiles} días del mes, obtienes tu resultado.")
