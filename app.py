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
        st.session_state['cenarios'] = pd.DataFrame(columns=['Ativo', 'Probabilidade', 'Retorno'])
    st.title("Calculadora Risco e Retorno")
    # with st.sidebar:
    st.subheader('Cenários')
    
    if 'ativos' not in st.session_state:
        st.session_state['ativos'] = ['Ativo1', 'Ativo2', 'Ativo3']
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
                    f'Ativo {i+1}', 
                    st.session_state.ativos[i], 
                    key=f'a{i}'
                )
            with midle:
                st.session_state.pesos[i] = st.number_input(
                    f'Peso {i+1}', 
                    st.session_state.pesos[i], 
                    key=f'p{i}'
                )
            with right:
                st.write('')
                if st.button(":material/remove:", key=f"del_{i}"):
                    st.session_state.ativos.pop(i)
                    st.session_state.pesos.pop(i)
                    st.rerun()

    st.data_editor(st.session_state['cenarios'], num_rows= "dynamic")
    st.write(st.session_state)

if __name__ == "__main__":
    main()