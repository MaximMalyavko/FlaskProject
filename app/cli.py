import os
import click


def register(app):

    @app.cli.group()
    def translate():
        """ Translation and localized commands """
        pass

    @translate.command()
    def update():
        """ Update all languages """
        if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
            raise RuntimeError('pybabel extract filed')
        if os.system('pybabel update -i messages.pot -d app/translations'):
            raise RuntimeError('pybabel update failed')
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """ Compile all languages """
        if os.system('pybabel compile -d app/translations'):
            raise RuntimeError('pybabel compile failed')

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """ Initialize a new language. """
        if os.system('pybabel extract -F babel.cfg -k -l -o messages.pot .'):
            raise RuntimeError('pybabel extract failed')
        if os.system('pybabel init -i messages.pot -d app/translations -l' + lang):
            raise RuntimeError('pybabel init failed')
        os.remove('messages.pot')