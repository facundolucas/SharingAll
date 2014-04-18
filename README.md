Ayudalos a Ayudar
=======
Es un site donde podras hacer donaciones a distintas organizaciones sin fines de lucro

Inquietud:
----------
Como arranco / instalo el proyecto en mi máquina?

Respuesta: 
----------

Debes tener python3, NO codeamos el sitio con compatibilidad con python.

1- Debes crear un nuevo virtualenv, Ej: pyvenv3.3

Activas tu virtualenv, ej: source pyvenv3.3/bin/activate

Si no pip instalado, descarga el .tar.gz desde https://pypi.python.org/pypi/setuptools
e instalalo con el python3 de tu virtualenv. Luego de instalar setuptools hacer:

easy_install-3.3 pip

2. Clona el proyecto

git clone https://github.com/facundolucas/SharingAll.git

2. instalar las dependencias, ej: pip3 install -r ./requirements.txt

3. python manage.py syncdb

4. python manage.py runserver

5. Visitar con tu browser http://localhost:8000  y listo!
