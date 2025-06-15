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
        st.session_state['cenarios'] = pd.DataFrame(columns=['Probabilidade', 'Retorno'])
    st.title("Calculadora Risco e Retorno")
    # with st.sidebar:
    st.subheader('Cenários')
    
    if 'ativos' not in st.session_state:
        st.session_state['ativos'] = ['Ativo1', 'Ativo2', 'Ativo3']
        st.session_state['pesos'] = [0.5, 0.3, 0.2]
    with st.sidebar:
        left, midle, right = st.columns([4, 1, 1], vertical_alignment="top")
        left.subheader('Ativos')


        if midle.button('',icon=':material/add:'):
            st.session_state.ativos.append('')
            st.session_state.pesos.append(0.0)
            st.rerun()

        if right.button('',icon=':material/remove:'):
            if len(st.session_state.ativos)>1:
                st.session_state.ativos.pop()
                st.session_state.pesos.pop()
                st.rerun()
        left, right = st.columns(2)
        for i, ativo in enumerate(st.session_state.ativos):
            with left:
                st.session_state.ativos[i] = st.text_input(
                    f'Ativo {i+1}', 
                    st.session_state.ativos[i], 
                    key=f'a{i}'
                )
            with right:
                st.session_state.pesos[i] = st.number_input(
                    f'Peso {i+1}', 
                    st.session_state.pesos[i], 
                    key=f'p{i}'
                )

    st.data_editor(st.session_state['cenarios'], num_rows= "dynamic")
    st.write(st.session_state)

if __name__ == "__main__":
    main()