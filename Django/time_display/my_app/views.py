from django.shortcuts import render
from datetime import datetime

def index(request):
    """Render the current server time using datetime (alternative to time.strftime)."""
    now = datetime.now()
    context = {
        "time": now.strftime("%Y-%m-%d %I:%M:%S %p"),
        "iso": now.isoformat(),
    }
    return render(request, 'index.html', context)
