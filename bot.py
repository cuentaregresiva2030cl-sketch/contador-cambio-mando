import tweepy
import os
import random
from datetime import datetime

def post_tweet():
    # 1. Configuración de tus Hashtags
    mis_hashtags = "#Chile #CuentaRegresiva2030 #Presidenciales #CambioDeMando #Elecciones2029 #Santiago"

    # 2. Cálculo de días faltantes hasta el 11 de marzo de 2030
    fecha_objetivo = datetime(2030, 3, 11)
    hoy = datetime.now()
    dias_faltantes = (fecha_objetivo - hoy).days

    # 3. Frases variadas para evitar el detector de spam de X
    frases = [
        "La meta está un día más cerca.",
        "Un día más en esta bitácora del tiempo.",
        "El calendario no se detiene.",
        "Seguimos contando los días con constancia.",
        "El camino al 2030 continúa sin pausa.",
        "Un paso más en la cuenta regresiva.",
        "El tiempo sigue su marcha hacia el objetivo."
    ]
    frase_del_dia = random.choice(frases)

    # 4. Construcción del mensaje final
    texto = f"{frase_del_dia}\n\nFaltan {dias_faltantes} días para el 11 de marzo de 2030. 🇨🇱\n\n{mis_hashtags}"

    # 5. Cargar credenciales desde los Secrets de GitHub
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # 6. Inicializar el cliente con parámetros de reintento (wait_on_rate_limit)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True
    )

    try:
        print(f"Intentando publicar:\n{texto}")
        # user_auth=True es VITAL para el plan gratuito de la API v2
        response = client.create_tweet(text=texto, user_auth=True)
        print(f"¡ÉXITO! Tweet publicado. ID: {response.data['id']}")
    except Exception as e:
        # Esto nos dirá exactamente qué pasa si vuelve a fallar
        print(f"Error detectado: {e}")

if __name__ == "__main__":
    post_tweet()
