from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config = Configurator(settings=settings)
    config.set_session_factory(my_session_factory)
    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.add_route('pdftest', '/pdftest')
    config.add_route('create_pdf', '/pdfnew')
    config.add_route('pdfform', '/pdfform')
    config.scan('.views')
    return config.make_wsgi_app()
