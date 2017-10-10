from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'wkhtmltopdf',
    'reportlab',
    'xhtml2pdf',
    'pdfjinja',
    'pdfkit',
    'pdb',
    'pyramid_debugtoolbar',
]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)
