---
layout: tip
title: Saltar ingreso de usuario y password en github
categories: tip
tags: github, bitbucket, ssh
---

Al iniciar un repositorio o clonar uno existente, terminamos con un repositorio que pide usuario y contraseña,
puesto que viene definida del tipo `https://github.com/username/reponame`

¿Cómo evitar que cada `git push` solicite el usuario y contraseña (en github)?


### (1) Genera una llave rsa
{% highlight bash %}
{% raw %}
ssh-keygen -t rsa -b 4096 -C "name@domain.com"
{% endraw %}
{% endhighlight %}
Basta con aceptar las opciones por defecto.
En ubuntu la llave típicamente está en `~/.ssh/id_rsa.pub`.

### (2) Abre el archivo generado y copia el contenido
{% highlight bash %}
{% raw %}
cat ~/.ssh/id_rsa.pub
{% endraw %}
{% endhighlight %}
Esto debería entregar una larga cadena de carácteres que no debes compartir con nadie excepto con github.

### (3) Agrega la llave generada en github o bitbucket
Abre github en la sección de configuración [https://github.com/settings/ssh]() 
y agrega el texto copiado en punto (2).

### (4) Obtén el nombre de usuario y del repositorio.
{% highlight bash %}
{% raw %}
git remote show origin
{% endraw %}
{% endhighlight %}
Mostrará algo del tipo
{% highlight html %}
{% raw %}
* remote origin
  Fetch URL: https://github.com/username/reponame.git
  Push  URL: https://github.com/username/reponame.git
  HEAD branch: master
  Remote branches:
    console-script tracked
    master         tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
{% endraw %}
{% endhighlight %}

## (5) Cambia el repositorio para aceptar ssh
{% highlight bash %}
{% raw %}
git remote set-url origin git+ssh://git@github.com/username/reponame.git
{% endraw %}
{% endhighlight %}

## (6) Chequea que todo funciona correctamente
Al hacer
{% highlight bash %}
{% raw %}
git remote show origin
{% endraw %}
{% endhighlight %}
ahora se debería obtener
{% highlight html %}
{% raw %}
* remote origin
  Fetch URL: git+ssh://git@github.com/username/reponame.git
  Push  URL: git+ssh://git@github.com/username/reponame.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
{% endraw %}
{% endhighlight %}

El procedimiento es muy similar en [https://bitbucket.org/](Bitbucket).

Los enlaces (en inglés) que utilicé fueron los siguientes:

 * [http://solvedstack.com/questions/git-push-username-password-how-to-avoid]()

 * [https://help.github.com/articles/generating-ssh-keys/]()
