import tweepy
import os
import random

def post_tweet():
    messages = [
        "Un día menos.", "La cuenta regresiva continúa.", "El tiempo sigue su marcha.",
        "Otro día en el calendario.", "El reloj sigue corriendo.", "Seguimos contando."
    ]
    texto = random.choice(messages)

    # Las 4 llaves maestras para publicar
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # Inicializamos el cliente de la v2 SOLO con las llaves de usuario
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        print(f"Intentando publicar vía v2: {texto}")
        # Comando específico de la v2
        response = client.create_tweet(text=texto)
        print(f"¡ÉXITO! Tweet publicado. ID: {response.data['id']}")
    except Exception as e:
        print(f"Error en v2: {e}")

if __name__ == "__main__":
    post_tweet()
