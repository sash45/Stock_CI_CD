import requests


colab_url = "https://colab.research.google.com/drive/1GZbP2btHQO8KGyqxE1Kv1m85Ra3HnzFw?usp=sharing"


def trigger_colab_execution():
    response = requests.get(colab_url)
    if response.status_code == 200:
        print("Colab notebook execution triggered successfully.")
    else:
        print(f"Failed to trigger Colab notebook. Status code: {response.status_code}")


if __name__ == "__main__":
    trigger_colab_execution()