import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calculadora Risco e Retorno",
    page_icon=":bar_chart:",
    layout="wide",
    # initial_sidebar_state="expanded"
)

def main():
    if 'cenarios' not in st.session_state:
        st.session_state['cenarios'] = pd.DataFrame([
            {'Ativo': 'AçãoA', 'Probabilidade': 0.5, 'Retorno': 0.1},
            {'Ativo': 'AçãoB', 'Probabilidade': 0.3, 'Retorno': 0.05},
            {'Ativo': 'AçãoC', 'Probabilidade': 0.2, 'Retorno': -0.02}
        ])
    st.title("Calculadora Risco e Retorno")
    # with st.sidebar:
    st.subheader('Cenários')
    
    if 'ativos' not in st.session_state:
        st.session_state['ativos'] = ['AçãoA', 'AçãoB', 'AçãoC']
        st.session_state['pesos'] = [0.5, 0.3, 0.2]
    with st.sidebar:
        left, midle, right = st.columns([3, 2, 1], vertical_alignment="top")
        left.subheader('Ativos')


        if right.button('',icon=':material/add:'):
            st.session_state.ativos.append('')
            st.session_state.pesos.append(0.0)
            st.rerun()

        for i, ativo in enumerate(st.session_state.ativos):
            left, midle, right = st.columns([3, 2, 1], vertical_alignment="bottom")
            with left:
                st.session_state.ativos[i] = st.text_input(
                    f'Ativo', 
                    st.session_state.ativos[i], 
                    key=f'a{i}'
                )
            with midle:
                st.session_state.pesos[i] = st.number_input(
                    f'Peso', 
                    st.session_state.pesos[i], 
                    key=f'p{i}'
                )
            with right:
                st.write('')
                if st.button(":material/remove:", key=f"del_{i}"):
                    st.session_state.ativos.pop(i)
                    st.session_state.pesos.pop(i)
                    st.rerun()

    cenarios_editado = st.data_editor(
        st.session_state['cenarios'], 
        key="cenarios_editor",
        num_rows= "dynamic",
        column_config={
            "Ativo": st.column_config.SelectboxColumn(
                options=st.session_state['ativos'],
                required=True
            ),
            "Probabilidade": st.column_config.NumberColumn(
                format="percent",
                min_value=0.0,
                max_value=1.0,
                step=0.00001,
                required=True
            ),
            "Retorno": st.column_config.NumberColumn(
                format="percent",
                min_value=-1.0,
                max_value=1.0,
                step=0.00001,
                required=True
            )
        }
    )
    st.session_state['cenarios'] = cenarios_editado
    st.write(st.session_state)

if __name__ == "__main__":
    main()