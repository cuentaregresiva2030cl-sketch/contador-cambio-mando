import tweepy
import os
import random # Para elegir un mensaje al azar

def post_tweet_api():
    # 1. Tu lista de mensajes
    messages = [
        "Un día menos.", "La cuenta regresiva continúa.", "El calendario sigue avanzando.",
        "Cada día cuenta.", "El tiempo pasa.", "Seguimos avanzando.",
        "Otro día en el calendario.", "Un día más cerca del cambio de mando.",
        "El reloj sigue corriendo.", "La cuenta regresiva sigue.",
        "Un día menos en el calendario político.", "Restando los días.",
        "Cada día nos acerca al cambio.", "El contador sigue bajando.",
        "Un día menos para el final del mandato.", "El tiempo no se detiene.",
        "Otro día que pasa.", "La cuenta sigue bajando.",
        "Un día menos en esta historia política.", "El calendario sigue corriendo.",
        "Un día más = a un día menos.", "Seguimos contando.",
        "El tiempo sigue avanzando.", "Un día menos hacia el cambio.",
        "El contador no se detiene.", "El reloj político sigue.",
        "Un día más en la cuenta regresiva.", "El calendario avanza.",
        "El contador sigue su curso.", "El tiempo sigue su marcha."
    ]

    # 2. Elegir un mensaje aleatorio
    texto_para_twittear = random.choice(messages)

    # 3. Obtener credenciales de GitHub
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # 4. Configurar Cliente (API v2)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        print(f"Intentando publicar: {texto_para_twittear}")
        response = client.create_tweet(text=texto_para_twittear)
        print(f"¡Éxito! Tweet publicado. ID: {response.data['id']}")
    except Exception as e:
        print(f"Error detectado: {e}")

if __name__ == "__main__":
    post_tweet_api()
