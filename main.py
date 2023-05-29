"""Modules for create interface, translate text and create sentences"""
import streamlit as st


if __name__ == '__main__':
    title = st.text_input('Введите свой текст:', 'Life of Brian')
    count = st.slider('Выберите максимальное '
                      'количество слов в предложении', 20, 400, 20)
    if st.button('Начать'):
        result = generate_ru_text(title, count)
        st.write(result)
