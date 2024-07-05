import subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def streamlit_view(request):
    # Run the Streamlit app as a subprocess
    streamlit_process = subprocess.Popen(['streamlit', 'run', 'D:\\testjango\\myproject\\myapp\\app.py'])


