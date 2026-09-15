from django.contrib import admin
from django.urls import path

from tracker.views import (
    dashboard,
    login_view,
    logout_view,
    register_view,

    expense_list,
    add_expense,
    edit_expense,
    delete_expense,

    income_list,
    add_income,
    edit_income,
    delete_income,

    budget_list,
    add_budget,
    edit_budget,
    delete_budget,

    reports,
    statistics,

    profile,
    settings_view,
)


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    # Dashboard
    path(
        '',
        dashboard,
        name='dashboard'
    ),

    # Authentication
    path(
        'login/',
        login_view,
        name='login'
    ),

    path(
        'register/',
        register_view,
        name='register'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    # Expenses
    path(
        'expenses/',
        expense_list,
        name='expenses'
    ),

    path(
        'expenses/add/',
        add_expense,
        name='add_expense'
    ),

    path(
        'expenses/<int:pk>/edit/',
        edit_expense,
        name='edit_expense'
    ),

    path(
        'expenses/<int:pk>/delete/',
        delete_expense,
        name='delete_expense'
    ),

    # Income
    path(
        'income/',
        income_list,
        name='income'
    ),

    path(
        'income/add/',
        add_income,
        name='add_income'
    ),

    path(
        'income/<int:pk>/edit/',
        edit_income,
        name='edit_income'
    ),

    path(
        'income/<int:pk>/delete/',
        delete_income,
        name='delete_income'
    ),

    # Budgets
    path(
        'budgets/',
        budget_list,
        name='budgets'
    ),

    path(
        'budgets/add/',
        add_budget,
        name='add_budget'
    ),

    path(
        'budgets/<int:pk>/edit/',
        edit_budget,
        name='edit_budget'
    ),

    path(
        'budgets/<int:pk>/delete/',
        delete_budget,
        name='delete_budget'
    ),

    # Analytics
    path(
        'reports/',
        reports,
        name='reports'
    ),

    path(
        'statistics/',
        statistics,
        name='statistics'
    ),

    # Account
    path(
        'profile/',
        profile,
        name='profile'
    ),

    path(
        'settings/',
        settings_view,
        name='settings'
    ),
]