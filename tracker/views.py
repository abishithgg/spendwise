from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)
from django.db.models import Sum
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import ExpenseForm, IncomeForm, BudgetForm
from .models import Expense, Income, Budget


# =========================
# AUTHENTICATION
# =========================

def register_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Account created successfully!'
            )

            return redirect('dashboard')

    else:
        form = UserCreationForm()

    return render(
        request,
        'tracker/register.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            messages.success(
                request,
                'Welcome back!'
            )

            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'tracker/login.html',
        {'form': form}
    )


def logout_view(request):

    logout(request)

    return redirect('login')


# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):

    today = timezone.localdate()

    month_start = today.replace(day=1)

    expenses = Expense.objects.filter(
        user=request.user,
        date__gte=month_start,
        date__lte=today
    )

    incomes = Income.objects.filter(
        user=request.user,
        date__gte=month_start,
        date__lte=today
    )

    total_expenses = (
        expenses.aggregate(
            total=Sum('amount')
        )['total']
        or Decimal('0')
    )

    total_income = (
        incomes.aggregate(
            total=Sum('amount')
        )['total']
        or Decimal('0')
    )

    balance = total_income - total_expenses

    if total_income > 0:

        savings_rate = (
            balance / total_income
        ) * 100

    else:

        savings_rate = Decimal('0')

    recent_expenses = Expense.objects.filter(
        user=request.user
    ).order_by(
        '-date',
        '-id'
    )[:5]

    recent_income = Income.objects.filter(
        user=request.user
    ).order_by(
        '-date',
        '-id'
    )[:5]

    budgets = Budget.objects.filter(
        user=request.user,
        month__year=today.year,
        month__month=today.month
    )

    budget_data = []

    for budget in budgets:

        spent = (
            Expense.objects.filter(
                user=request.user,
                category=budget.category,
                date__year=today.year,
                date__month=today.month
            ).aggregate(
                total=Sum('amount')
            )['total']
            or Decimal('0')
        )

        if budget.amount > 0:

            percentage = (
                spent / budget.amount
            ) * 100

        else:

            percentage = Decimal('0')

        budget_data.append({
            'budget': budget,
            'spent': spent,
            'percentage': min(percentage, 100)
        })

    context = {

        'total_income': total_income,

        'total_expenses': total_expenses,

        'balance': balance,

        'savings_rate': savings_rate,

        'recent_expenses': recent_expenses,

        'recent_income': recent_income,

        'budget_data': budget_data,

    }

    return render(
        request,
        'tracker/dashboard.html',
        context
    )


# =========================
# EXPENSES
# =========================

@login_required
def expense_list(request):

    expenses = Expense.objects.filter(
        user=request.user
    ).order_by(
        '-date',
        '-id'
    )

    search = request.GET.get(
        'search',
        ''
    ).strip()

    category = request.GET.get(
        'category',
        ''
    )

    if search:

        expenses = expenses.filter(
            title__icontains=search
        )

    if category:

        expenses = expenses.filter(
            category=category
        )

    context = {

        'expenses': expenses,

        'search': search,

        'category': category,

        'categories': Expense.CATEGORY_CHOICES,

    }

    return render(
        request,
        'tracker/expenses.html',
        context
    )


@login_required
def add_expense(request):

    if request.method == 'POST':

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(
                commit=False
            )

            expense.user = request.user

            expense.save()

            messages.success(
                request,
                'Expense added successfully!'
            )

            return redirect('expenses')

    else:

        form = ExpenseForm(
            initial={
                'date': timezone.localdate()
            }
        )

    return render(
        request,
        'tracker/expense_form.html',
        {
            'form': form,
            'title': 'Add Expense'
        }
    )


@login_required
def edit_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Expense updated successfully!'
            )

            return redirect('expenses')

    else:

        form = ExpenseForm(
            instance=expense
        )

    return render(
        request,
        'tracker/expense_form.html',
        {
            'form': form,
            'title': 'Edit Expense'
        }
    )


@login_required
@require_POST
def delete_expense(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )

    expense.delete()

    messages.success(
        request,
        'Expense deleted successfully!'
    )

    return redirect('expenses')


# =========================
# INCOME
# =========================

@login_required
def income_list(request):

    incomes = Income.objects.filter(
        user=request.user
    ).order_by(
        '-date',
        '-id'
    )

    return render(
        request,
        'tracker/income.html',
        {
            'incomes': incomes
        }
    )


@login_required
def add_income(request):

    if request.method == 'POST':

        form = IncomeForm(
            request.POST
        )

        if form.is_valid():

            income = form.save(
                commit=False
            )

            income.user = request.user

            income.save()

            messages.success(
                request,
                'Income added successfully!'
            )

            return redirect('income')

    else:

        form = IncomeForm(
            initial={
                'date': timezone.localdate()
            }
        )

    return render(
        request,
        'tracker/income_form.html',
        {
            'form': form,
            'title': 'Add Income'
        }
    )


@login_required
def edit_income(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = IncomeForm(
            request.POST,
            instance=income
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Income updated successfully!'
            )

            return redirect('income')

    else:

        form = IncomeForm(
            instance=income
        )

    return render(
        request,
        'tracker/income_form.html',
        {
            'form': form,
            'title': 'Edit Income'
        }
    )


@login_required
@require_POST
def delete_income(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    income.delete()

    messages.success(
        request,
        'Income deleted successfully!'
    )

    return redirect('income')


# =========================
# BUDGETS
# =========================

@login_required
def budget_list(request):

    budgets = Budget.objects.filter(
        user=request.user
    ).order_by(
        '-month',
        'category'
    )

    budget_data = []

    for budget in budgets:

        spent = (
            Expense.objects.filter(
                user=request.user,
                category=budget.category,
                date__year=budget.month.year,
                date__month=budget.month.month
            ).aggregate(
                total=Sum('amount')
            )['total']
            or Decimal('0')
        )

        percentage = (
            spent / budget.amount * 100
            if budget.amount > 0
            else Decimal('0')
        )

        budget_data.append({
            'budget': budget,
            'spent': spent,
            'percentage': min(percentage, 100)
        })

    return render(
        request,
        'tracker/budgets.html',
        {
            'budget_data': budget_data
        }
    )


@login_required
def add_budget(request):

    if request.method == 'POST':

        form = BudgetForm(
            request.POST
        )

        if form.is_valid():

            budget = form.save(
                commit=False
            )

            budget.user = request.user

            budget.save()

            messages.success(
                request,
                'Budget created successfully!'
            )

            return redirect('budgets')

    else:

        today = timezone.localdate()

        form = BudgetForm(
            initial={
                'month': today.replace(day=1)
            }
        )

    return render(
        request,
        'tracker/budget_form.html',
        {
            'form': form,
            'title': 'Set Budget'
        }
    )


@login_required
def edit_budget(request, pk):

    budget = get_object_or_404(
        Budget,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':

        form = BudgetForm(
            request.POST,
            instance=budget
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Budget updated successfully!'
            )

            return redirect('budgets')

    else:

        form = BudgetForm(
            instance=budget
        )

    return render(
        request,
        'tracker/budget_form.html',
        {
            'form': form,
            'title': 'Edit Budget'
        }
    )


@login_required
@require_POST
def delete_budget(request, pk):

    budget = get_object_or_404(
        Budget,
        pk=pk,
        user=request.user
    )

    budget.delete()

    messages.success(
        request,
        'Budget deleted successfully!'
    )

    return redirect('budgets')


# =========================
# REPORTS
# =========================

@login_required
def reports(request):

    expenses = Expense.objects.filter(
        user=request.user
    )

    total = (
        expenses.aggregate(
            total=Sum('amount')
        )['total']
        or Decimal('0')
    )

    category_data = []

    for category, label in Expense.CATEGORY_CHOICES:

        amount = (
            expenses.filter(
                category=category
            ).aggregate(
                total=Sum('amount')
            )['total']
            or Decimal('0')
        )

        category_data.append({
            'name': label,
            'amount': amount
        })

    return render(
        request,
        'tracker/reports.html',
        {
            'total': total,
            'category_data': category_data
        }
    )


@login_required
def statistics(request):

    expenses = Expense.objects.filter(
        user=request.user
    )

    incomes = Income.objects.filter(
        user=request.user
    )

    total_expenses = (
        expenses.aggregate(
            total=Sum('amount')
        )['total']
        or Decimal('0')
    )

    total_income = (
        incomes.aggregate(
            total=Sum('amount')
        )['total']
        or Decimal('0')
    )

    return render(
        request,
        'tracker/statistics.html',
        {
            'total_expenses': total_expenses,
            'total_income': total_income,
            'balance': total_income - total_expenses,
        }
    )


# =========================
# PROFILE
# =========================

@login_required
def profile(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username',
            ''
        ).strip()

        email = request.POST.get(
            'email',
            ''
        ).strip()

        if username:

            request.user.username = username

        request.user.email = email

        request.user.save()

        messages.success(
            request,
            'Profile updated successfully!'
        )

        return redirect('profile')

    return render(
        request,
        'tracker/profile.html'
    )


# =========================
# SETTINGS
# =========================

@login_required
def settings_view(request):

    return render(
        request,
        'tracker/settings.html'
    )