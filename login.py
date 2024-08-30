# Rodar o código
# streamlit run login.py

from time import sleep

import streamlit as st

from achmy import ler_todos_usuarios

def login():
    with st.container(border=True):
        st.markdown('Bem-Vindo a Tela de Login')
        usuarios = ler_todos_usuarios()
        usuarios = {usuario.nome: usuario for usuario in usuarios}
        nome_usuario = st.selectbox('Selecione o seu nome', list(usuarios.keys())
        )
        senha = st.text_input("Digite sua senha", type="password")
        if st.button("Entrar"):
            usuario = usuarios[nome_usuario]
            if usuario.check_senha(senha):
                st.success("Login bem-sucedido")
                st.session_state["usuario"] = usuario
                st.session_state["logado"] = True
                sleep(2)
                st.rerun()
            else:
                st.error("Senha inválida")


def main():
    if not "logado" in st.session_state:
        st.session_state["logado"] = False

    if not st.session_state["logado"]:
        login()
    else:
        st.markdown("Bem-vindo {}".format(st.session_state["usuario"].nome))


if __name__ == "__main__":
    main()