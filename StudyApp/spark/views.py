from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Создайте здесь свои представления
from .models import Topic


def index(request):
    """Домашняя страница приложения SPARK"""
    return render(request, 'spark/index.html')


@login_required
def topics(request):
    """Выводит список тем."""
    topicss = Topic.objects.order_by('date_added')
    context = {'topics': topicss}
    return render(request, 'spark/topics.html', context)


@login_required
def topic(request, topic_id):
    """Выводит одну тему и все ее записи."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'spark/topic.html', context)

