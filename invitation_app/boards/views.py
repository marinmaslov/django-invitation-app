from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from django.utils.crypto import get_random_string
import datetime

from .models import Board

class AdminBoardView():
    template_name = 'boards/board.html'

    def get_context_data(self, **kwargs):
        context = super(AdminBoardView, self).get_context_data(**kwargs)
        return context
    