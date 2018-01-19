from django.shortcuts import render
from .models import Audio

# Create your views here.


def play_audio(request, title):
    print(title)
    audio = Audio.objects.all().filter(title=title)[0]
    context = {
        'audio': audio
    }
    print(audio)
    return render(request, 'play/audio.html', context=context)
