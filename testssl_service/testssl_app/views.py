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
            form_instance = form.save(commit=False)  # Create instance but don't save yet

            # script_path = '/home/kaifong/testssl.sh/testssl.sh'
            # Define Docker paths
            docker_image = "oqs-testssl"  # Name of your Docker image
            results_dir_host = os.path.abspath("../testssl_service/testssl_docker/results")  # Local results directory
            results_dir_container = "/opt/testssl.sh/results"  # Path inside the container
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
                # print(result.returncode)     
                
                # if Docker fails
                if result.returncode != 0: 
                    print(f"Docker command failed with return code {result.returncode}")
                    print(f"Standard Output:\n{result.stdout}")
                    print(f"Standard Error:\n{result.stderr}")
                    return render(request, 'testssl_app/error.html', {"message": "Docker execution failed."})

                # if Docker does not fail
                if result.returncode == 0:
                    print("Docker command succeeded")
                    print(f"Standard Output: {result.stdout}")

                    # Load results CSV file
                    csv_path = os.path.join(results_dir_host, results_file)
                    if os.path.exists(csv_path):

                        result_df = pd.read_csv(csv_path)

                        # Mapping CSV 'id' values to form_instance attributes
                        field_mapping = {
                            "SSLv2": "value_sslv2",
                            "SSLv3": "value_sslv3",
                            "TLS1": "value_tls1",
                            "TLS1_1": "value_tls11",
                            "TLS1_2": "value_tls12",
                            "TLS1_3": "value_tls13",
                            "cipherorder_TLSv1": "tls10_ciphers",
                            "cipherorder_TLSv1_1": "tls11_ciphers",
                            "cipherorder_TLSv1_2": "tls12_ciphers",
                            "supportedciphers_TLSv1_3": "tls13_ciphers",
                            "FS_KEMs": "kems",
                            "FS_ECDHE_curves": "ecdhe_curves",
                            "FS_TLS12_sig_algs": "tls12_sig_alg",
                            "FS_TLS13_sig_algs": "tls13_sig_alg",
                            "cert_signatureAlgorithm <hostCert#1>": "cert_sig_alg",
                            "cert <hostCert#1>": "cert"
                        }
                        # Loop through the mapping and set attributes dynamically
                        for csv_id, model_field in field_mapping.items():
                            matching_row = result_df.loc[result_df['id'] == csv_id, 'finding']
                            if not matching_row.empty:
                                setattr(form_instance, model_field, matching_row.values[0])  # Dynamic assignment

                        form_instance.save()

                        # form_instance.value_sslv2 = result_df.loc[result_df['id'] == 'SSLv2', 'finding'].values[0]
                        # form_instance.value_sslv3 = result_df.loc[result_df['id'] == 'SSLv3', 'finding'].values[0]
                        # form_instance.value_tls1 = result_df.loc[result_df['id'] == 'TLS1', 'finding'].values[0]
                        # form_instance.value_tls11 = result_df.loc[result_df['id'] == 'TLS1_1', 'finding'].values[0]
                        # form_instance.value_tls12 = result_df.loc[result_df['id'] == 'TLS1_2', 'finding'].values[0]
                        # form_instance.value_tls13 = result_df.loc[result_df['id'] == 'TLS1_3', 'finding'].values[0]

                        # form_instance.save()
                        if form_instance.id is None:
                            print("Error: form_instance not saved correctly!")
                            return render(request, 'testssl_app/error.html', {"message": "Could not save instance."})

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
                print(f"Error running Docker command and saving results: {str(e)}")
            
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
