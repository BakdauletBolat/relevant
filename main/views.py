from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Brand, Feature, Person, Rating, Project, TelegramUser
from .forms import RequestForm
from rest_framework.generics import CreateAPIView
from .serializers import TelegramBotSerializer
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)


class TelegramUserCreateAPIView(CreateAPIView):
    serializer_class = TelegramBotSerializer
    queryset = TelegramUser.objects.all()


def home_view(request):
    brands = Brand.objects.all()
    features = Feature.objects.all()
    ratings = Rating.objects.all()
    projects = Project.objects.all()

    data = {
        'brands': brands,
        'features': features,
        'ratings': ratings,
        'projects': projects
    }

    return render(request, 'main/home.html', context=data)


def contact_us_view(request):
    return render(request, 'main/contact.html')


def success_view(request):
    return render(request, 'main/success.html')


def about_us_view(request):
    persons = Person.objects.all()
    data = {
        'persons': persons
    }
    return render(request, 'main/about-us.html', context=data)


def projects_view(request):
    projects = Project.objects.all()
    data = {
        'projects': projects
    }
    return render(request, 'main/projects.html', context=data)


def submit_request(request):
    updater = Updater("5478835430:AAEqT3Kw8QKDlTPRzIfSRVYAlBOW2uIxfPQ")
    telegram_users = TelegramUser.objects.all()
    if request.method == "POST" or None:
        form = RequestForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False)
            obj = form.save()
            for user in telegram_users:
                updater.bot.send_message(chat_id=user.chat_id, text=f"""
                <b>Ух ты у нас новая заявка № {obj.id} !!! </b> \n Номер телефона:  <u><b>{obj.phone}</b></u> \n Имя: <b> {obj.name} </b> \n Время создание: {obj.created_at} \n
                """, parse_mode="HTML")
            return redirect(reverse('success_view'))
        else:
            return render(request, 'main/contact.html', {'form': form})
    else:
        return render(request, 'main/404.html')
