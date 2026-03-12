import tweepy
import os
import random
from datetime import datetime

def post_tweet():
    # 1. Configura aquí tus Hashtags (puedes poner los que quieras)
    mis_hashtags = "#Chile #CuentaRegresiva2030 #Presidenciales #CambioDeMando #Elecciones2029 #Santiago "

    # 2. Cálculo de días faltantes
    fecha_objetivo = datetime(2030, 3, 11)
    hoy = datetime.now()
    dias_faltantes = (fecha_objetivo - hoy).days

    # 3. Frases variadas para que el tweet cambie un poco cada día
    frases = [
        "El tiempo sigue su marcha.",
        "Un día más en esta bitácora.",
        "El calendario no se detiene.",
        "Seguimos contando los días.",
        "La meta está un día más cerca."
    ]
    frase_del_dia = random.choice(frases)

    # 4. Construcción del mensaje final
    texto = f"{frase_del_dia}\n\nFaltan {dias_faltantes} días para el 11 de marzo de 2030. 🇨🇱\n\n{mis_hashtags}"

    # 5. Cargar credenciales desde GitHub Secrets
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

   # 5. Inicializar el cliente con un "User Agent" y reintentos automáticos
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True  # Si X está lento, espera en lugar de fallar
    )

    try:
        print(f"Intentando publicar:\n{texto}")
        # Agregamos user_auth=True explícitamente aquí
        response = client.create_tweet(text=texto, user_auth=True) 
        print(f"¡ÉXITO! Tweet publicado. ID: {response.data['id']}")
