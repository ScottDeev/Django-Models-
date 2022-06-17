from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

User = get_user_model()

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_detail.html"
