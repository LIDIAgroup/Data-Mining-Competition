Data-Mining-Competition
=======================

###Requisitos

- [Python](https://www.python.org/).
- [Scikit](http://scikit-learn.org/stable/).

###Instalacion
	> sudo apt-get install build-essential python-dev python-numpy python-setuptools python-scipy libatlas-dev

	> sudo apt-get install python-pip

	> pip install -U scikit-learn

###Pre-procesado
Los datos vienen en formato .arff, y nos interesan en csv para ello existe el archivo to_csv.py que realiza esta transformacion. Ademas se incluye un archivo replace_chars.py que elimina todos los caracteres alfanumericos en favor de caracteres numericos para facilitar su carga en matlab.

###Subsamplig
Para obtener un archivo con los patrones de la clase minoritaria utilizar el archivo get_min.py
para la mayoritaria utilizar get_maj.py.
(Los archivos tienen que estar preprocesados)

###Entrenamiento
train.py sirve para entrenar n clasificadores y los guarda en disco.

###Clasificacion
classify.py realiza la clasificacion.

##workflow
- Descargar el archivo con todos los patrones
- Pre-procesarlo
- Obtener un archivo con patrones la clase mayoritaria y otro con patrones de la minoritaria

(En lugar de entrenar un solo clasificador, entrenaremos varios que clasificaran todos a la vez, el resultado de la clasificacion sera el mayoritario entre los clasificadores)

- Partir los archivos de patrones en varios trozos y utilizar cada uno de ellos para entrenar un clasificador.
(se puede utilizar subsampling.py).

- Una vez entrenados todos los clasificadores (tarda bastante) crear un archivo test.csv y ejecutar test.py


