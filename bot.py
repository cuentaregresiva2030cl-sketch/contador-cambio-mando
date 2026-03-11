import tweepy
import os
import random

def post_tweet():
    # 1. Lista completa de mensajes
    messages = [
        "Un día menos.", "La cuenta regresiva continúa.", "El tiempo sigue su marcha.",
        "Otro día en el calendario.", "El reloj sigue corriendo.", "Seguimos contando.",
        "Un día más cerca del cambio de mando.", "El contador sigue bajando.",
        "El calendario político avanza.", "Restando los días para el 2030."
    ]
    texto = random.choice(messages)

    # 2. Cargar credenciales desde GitHub Secrets
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # 3. Inicializar el cliente de la v2 (OAuth 1.0a User Context)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        print(f"Intentando publicar vía v2: {texto}")
        # En la API v2 se usa create_tweet
        response = client.create_tweet(text=texto)
        print(f"¡ÉXITO! Tweet publicado. ID: {response.data['id']}")
    except Exception as e:
        print(f"Error en v2: {e}")

# 4. Esto es MUY importante para que el script corra
if __name__ == "__main__":
    post_tweet()
