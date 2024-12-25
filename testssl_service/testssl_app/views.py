import subprocess
import os 
import pandas as pd

from django.shortcuts import render, redirect

from .forms import URLForm
from .models import URLItem

def homepage(request):
    # result_df = None
    # extracted_values = None

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            
            url = form.cleaned_data['url']
            # form.save()
            form_instance = form.save(commit=False)  # Create instance but don't save yet

            # script_path = '/home/kaifong/testssl.sh/testssl.sh'
            # Define Docker paths
            docker_image = "mytestssl"  # Name of your Docker image
            results_dir_host = os.path.abspath("../testssl_service/testssl_docker/results")  # Local results directory
            results_dir_container = "/home/testssl/results"  # Path inside the container
            results_file = "results.csv"

            # Ensure local results directory exists
            os.makedirs(results_dir_host, exist_ok=True)

            docker_command = [
                "docker", "run", "--rm", "-t",
                "-v", f"{results_dir_host}:{results_dir_container}",
                docker_image,
                url
            ]

            try: 
                # result = subprocess.run(['wsl', 'bash', script_path, '--csvfile', 'results.csv', '--overwrite', url], capture_output=True, text=True)
                result = subprocess.run(docker_command, capture_output=True, text=True)

                if result.returncode == 0:
                    # print(f"Docker Output: {result.stdout}")
                    print("Success!")
                    # Load results CSV file
                    csv_path = os.path.join(results_dir_host, results_file)
                    if os.path.exists(csv_path):

                        result_df = pd.read_csv(csv_path)

                        # Extract values from CSV
                        # value_sslv2 = result_df.loc[result_df['id'] == 'SSLv2', 'finding'].values[0]
                        # value_sslv3 = result_df.loc[result_df['id'] == 'SSLv3', 'finding'].values[0]
                        # value_tls1 = result_df.loc[result_df['id'] == 'TLS1', 'finding'].values[0]
                        # value_tls11 = result_df.loc[result_df['id'] == 'TLS1_1', 'finding'].values[0]
                        # value_tls12 = result_df.loc[result_df['id'] == 'TLS1_2', 'finding'].values[0]
                        # value_tls13 = result_df.loc[result_df['id'] == 'TLS1_3', 'finding'].values[0]
                        form_instance.value_sslv2 = result_df.loc[result_df['id'] == 'SSLv2', 'finding'].values[0]
                        form_instance.value_sslv3 = result_df.loc[result_df['id'] == 'SSLv3', 'finding'].values[0]
                        form_instance.value_tls1 = result_df.loc[result_df['id'] == 'TLS1', 'finding'].values[0]
                        form_instance.value_tls11 = result_df.loc[result_df['id'] == 'TLS1_1', 'finding'].values[0]
                        form_instance.value_tls12 = result_df.loc[result_df['id'] == 'TLS1_2', 'finding'].values[0]
                        form_instance.value_tls13 = result_df.loc[result_df['id'] == 'TLS1_3', 'finding'].values[0]

                        form_instance.save()

                        # extracted_values = {
                        #     'sslv2': form_instance.value_sslv2,
                        #     'sslv3': form_instance.value_sslv3,
                        #     'tls1': form_instance.value_tls1,
                        #     'tls11': form_instance.value_tls11,
                        #     'tls12': form_instance.value_tls12,
                        #     'tls13': form_instance.value_tls13,
                        # }

                        # if value_sslv2:
                        #     print(f"{value_sslv2, value_sslv3, value_tls1, value_tls11, value_tls12, value_tls13}")
                        # else:
                        #     print("No matching value found")
                    # else:
                    #     print("Results file not generated.")
                # else:
                #     print(f"Docker Error: {result.stderr}")
            
            except Exception as e:
                print(f"Error running Docker command: {str(e)}")

            return redirect('results', instance_id=form_instance.id)
    form = URLForm()

    page = {
        "forms": form,
        "title": "testssl homepage",
    }

    return render(request, 'testssl_app/index.html', page)

def results(request, instance_id):
    try:
        instance = URLItem.objects.get(id=instance_id)
        page = {
            "title": "testssl results",
            "instance": instance,
        }
        return render(request, 'testssl_app/results.html', page)
    except URLItem.DoesNotExist:
        return render(request, 'testssl_app/error.html', {"message": "Results not found"})


def history(request):

    url_list = URLItem.objects.order_by("-date")


    page = {
        "list": url_list,
        "title": "testssl history",
    }

    return render(request, 'testssl_app/history.html', page)
