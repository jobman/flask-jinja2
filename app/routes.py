# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'jobman'}
    posts = [
        {
            'author': {'username': 'Джанго Фримен'},
            'body': 'Не знаю что значит "абсолютно"'
        },
        {
            'author': {'username': 'Доктор Шульц'},
            'body': 'Не знаешь уверен ли ты?'
        },
        {
            'author': {'username': 'Джанго Фримен'},
            'body': 'Не знаю'
        },
        {
            'author': {'username': 'Доктор Шульц'},
            'body': 'Абсолютно?'
        },
        {
            'author': {'username': 'Джанго Фримен'},
            'body': 'Да'
        },
        {
            'author': {'username': 'Доктор Шульц'},
            'body': 'Уверен?'
        },
        {
            'author': {'username': 'Джанго Фримен'},
            'body': 'Вон он, бежит через поле во весь опор!'
        }
    ]

    return render_template('index.html', title='Цитаты из кинофильмов', user=user, posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Запрошен вход для пользователя {} ({}), запомнить = {}'.format(form.username.data, form.password.data,
                                                                              form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)
