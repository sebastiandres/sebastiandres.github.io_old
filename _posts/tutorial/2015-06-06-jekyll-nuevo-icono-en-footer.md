---
layout: tutorial
title: Nuevo ícono en footer en Jekyll.
categories: [tutorial, jekyll] 
tags: icono, footer
---

La lista de iconos disponibles en Jekyll now es bastante completa: 
dribbble, facebook, flickr, githu, instagram, linkedin, pinterest, rss, twitter, stackoverflow y youtube.
Sin embargo, creo que le faltaban algunos, por lo que decidí investigar cómo agregar más íconos: kaggle y bitbucket.

## Creando el ícono

Necesitas un ícono de 40x40 pixeles, ojala en svg, pero png también serviría.
Lo primero que debes hacer es convertir la imagen a base 64. El texto que obtengas tienes que agregarlo en 
`_sass/_svg-icons.scss` siguiendo el formato ahí indicado.

## Creando el vínculo
Lo siguiente es editar el enlace que será utilizado. Para eso, necesitas editar el archivo `_includes/svg-icons.html`.
Nuevamente, duplica una de las entradas existentes y edita convenientemente.

## Personaliza
Lo último es editar tu nombre de usuario en la configuración principal `_config.yml`.
