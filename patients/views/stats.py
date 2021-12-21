from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from patients.views import LOGIN_URL
from patients.utils.stats.month import get_current_month_stats
from patients.utils.stats.year import get_current_year_stats
from patients.utils.stats import get_gross_stats


@login_required(login_url=LOGIN_URL)
def stats(request):
    context = {
        'active': 'stats',
        'current_month_stats': get_current_month_stats(),
        'current_year_stats': get_current_year_stats(),
        'gross_stats': get_gross_stats()
    }
    return render(request, 'stats/stats.html', context)