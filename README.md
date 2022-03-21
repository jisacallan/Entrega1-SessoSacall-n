# Entrega1-SessoSacallán

Se explicará en las siguientes secciones las funcionalidades como también los diferentes propósitos del programa.

## Información básica

**Propósito del proyecto:** Establecer una página de uso sencillo para profesionales del área de salud de una clínica.

**Utilidad del proyecto:** La necesidad del proyecto se ve en base a la falta de un programa de acceso sencillo a los datos tantos de pacientes como de profesionales de la clínica. Es aquí explícita y fundamental la importancia de la sencillez del programa.

**Aviso de problemas:** Por cualquier urgencia, puede contactarse al mail del creador del proyecto jisacallan@gmail.com

## Desarrollo del programa

**Primera parte:** En la carpeta _Entrega1_ puede observarse los datos básicos de inicio del proyecto. 
En la sección _settings.py_ pueden verse las apps instaladas en_INSTALLED_APPS_ como también el funcionamiento respecto de templates en _TEMPLATES_[^1]. 
A su vez, nótese en la sección _urls.py_ que han sido incluídas las urls de las diferentes aplicaciones y se conserva la url del administrador.
También, cabe destacarse la formación de una base de datos. 
Las siguientes secciones describirán las apps.

**Segunda parte:** Se ha creado la aplicación _Indice_ para poder generar una pantalla de inicio correcta y lo más agradable a la vista. 
En _urls.py_ permite el acceso a la _views.py_. En esta última, la función _home_ es la que habilita al manejo de nuestro template. 
El template se encuentra dentro de la carpeta _home_, estando ésta última dentro de la carpeta _template_[^2].
Se agradece el trabajo de la página _Free CSS_ (https://www.free-css.com/) ya que de aquí se ha podido extraer un template adecuado para la página aquí establecida.
Se ha suministrado del código CSS en la carpeta _static_

**Tercera parte:** Esta aplicación consta en las funcionalidades necesaria para el ingreso y búsqueda de datos. 
En _models.py_ se establecen los modelos necesarios para las funcionalidades que se establecerán en otra sección, éstos son Paciente, Especialista y Tratamiento; y
en _admin.py_ se registran estos modelos. Los formularios se crean mediante _forms.py_ y se establecen con _views.py_.
De aquí se establece el template _entrega_formulario.html_. A su vez, el buscador se desarrolla en _BusquedaPaciente_ y se muestra mediante _busqueda.html_.
Ambos templates se encuentran en la carpeta del mismo nombre, pero dentro de AppPrimerEntrega.

## Entrega

A continuación, se mostrará, en base a la consigna, donde se considera, en base a quien programó este proyecto, dónde puede ubicarse cada consigna en las secciones:

1. Herencia de HTML: En el template de la primera parte se encuentran los bloques incorporados que permitirán incorporar los datos que cambian en el resto de los templates.

2. Por lo menos 3 clases en models: Las tres clases en _models.py_ se han mostrado en la tercera parte

3. Un formulario para insertar datos a todas las clases de tu models: Se ha optado por establecer tres formularios, a vistas de lograr extender el trabajo a futuro.
Estos pueden pueden hallarse en _forms.py_.

4. Un formulario para buscar algo en la BD: A pesar del punto anterior, solo se ha creado un solo formulario para la búsqueda. 
No se descarta la posibilidad de que se establezcan más búsquedas a futuro.

5. Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades: Aquí mismo se lo está mostrando.

[^1]: Nótese que la sección _DIRS_ no está señalada con una ruta específica, así será posible navegar entre templates.
[^2]: En la nota anterior se aclara la razón de porqué no se especifica una ruta en _DIRS_. Lo mismo se repetirá en la tercera parte.
