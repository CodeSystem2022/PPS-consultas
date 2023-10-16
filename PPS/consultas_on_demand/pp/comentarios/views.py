# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.contenttypes.models import ContentType

from .forms import FormComentarios
from .models import Comentarios
from post.models import Post
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
User = settings.AUTH_USER_MODEL



def comentario_id(request, pk):

	instance = get_object_or_404(Comentarios, pk=pk)

	context = {

		"comentario":instance
	}

	return render(request, 'comentarios/instance.html', context)

def post_idd(request, pk):
    instance = get_object_or_404(Post, pk=pk)

    # Inicializar los datos del formulario
    inicializar_datos = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }

    # Crear una instancia del formulario con los datos iniciales
    form = FormComentarios(request.POST or None, initial=inicializar_datos)

    if form.is_valid():
        # Obtener los datos del formulario
        models       = form.cleaned_data.get("content_type")
        #content_type = ContentType.objects.get(model=models)
        content_type = form.cleaned_data.get("content_type")
        print("Content Type Value:", content_type)
        obj_id = form.cleaned_data.get("object_id")
        texto_data = form.cleaned_data.get("texto")
        
    
        # Crear el comentario
        comentarios, created = Comentarios.objects.get_or_create(
            usuario=request.user,
            content_type=content_type,
            object_id=obj_id,
            texto=texto_data
        )

        if created:
            print("Fue creado con éxito")

        # Redirigir a la URL del objeto relacionado (en este caso, el post)
        return HttpResponseRedirect(comentarios.content_object.get_absolute_url())
        
    # Obtener los comentarios asociados al post
    #ver_comentarios = instance.comentarios_relacionados.all()
    ver_comentarios = instance.comentarios

    context = {
        'form': form,
        'instance': instance,
        'ver_comentarios': ver_comentarios
    }

    return render(request, 'comentarios/comentar.html', context)

def eliminarComentarios(request, id):
    try:
        instance = Comentarios.objects.get(id=id)
    except Comentarios.DoesNotExist:
        raise Http404("La página que buscas no existe")

    if instance.usuario != request.user:
        response = HttpResponse("No tienes permiso para realizar esta acción")
        response.status_code = 403
        return response

    if request.method == "POST":
        padre_instance_url = instance.content_object.get_absolute_url()
        instance.delete()
        messages.success(request, "Esta acción ha eliminado el comentario")
        return HttpResponseRedirect(padre_instance_url)

    context = {'instance': instance}
    return render(request, 'comentarios/eliminar.html', context)
