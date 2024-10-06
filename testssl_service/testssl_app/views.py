import subprocess
import pandas as pd

from django.shortcuts import render, redirect

from .forms import URLForm
from .models import URLItem

def homepage(request):
    result_pd = None

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            
            url = form.cleaned_data['url']
            form.save()

            script_path = '/home/kaifong/testssl.sh/testssl.sh'

            try: 
                result = subprocess.run(['wsl', 'bash', script_path, '--csvfile', 'results.csv', url], capture_output=True, text=True)

                if result.returncode == 0:
                    print(f"Script Output: {result.stdout}")
                    result_df = pd.read_csv("results.csv")
                    value = result_df.loc[result_df['id'] == 'TLS1', 'finding'].values[0]
                    if not len(value) == 0:
                        print(f"The value is {value}")
                    else:
                        print("No matching value found")
                else:
                    print(f"Script Error: {result.stderr}")
            except Exception as e:
                print(f"Error running script via WSL: {str(e)}")

            return redirect('home')
    form = URLForm()

    page = {
        "forms": form,
        "title": "SEARCH",
    }

    return render(request, 'testssl_app/index.html', page)


def history(request):

    url_list = URLItem.objects.order_by("-date")


    page = {
        "list": url_list,
        "title": "URL LIST",
    }

    return render(request, 'testssl_app/history.html', page)
