import tweepy
import os
import random

def post_tweet():
    # 1. Lista de 40 frases rotativas
    messages = [
        "Un día menos en el calendario.", "La cuenta regresiva continúa.", "El tiempo sigue su marcha.",
        "Otro día en el calendario político.", "El reloj sigue corriendo.", "Seguimos contando los días.",
        "Un día más cerca del cambio de mando.", "El contador sigue bajando.", "El calendario avanza sin pausa.",
        "Restando los días para el 2030.", "Un paso más hacia el relevo presidencial.", "El tiempo no se detiene.",
        "Cada día cuenta en esta cuenta regresiva.", "Sumando días, restando esperas.", "El reloj político no descansa.",
        "Un día menos para el 11 de marzo de 2030.", "Avanzamos un día más.", "El contador sigue su curso oficial.",
        "La historia sigue su curso, un día a la vez.", "Marcando el paso del tiempo.", "Día tras día, el contador baja.",
        "Un nuevo amanecer en la cuenta regresiva.", "El horizonte de 2030 está un día más cerca.", "Tic tac: un día menos.",
        "La meta está un día más cerca.", "Actualizando el contador diario.", "Siguiendo el cronograma hacia el 2030.",
        "Un día menos de espera.", "El tiempo vuela, el contador lo sabe.", "Comprometidos con la cuenta diaria.",
        "Un día más en esta bitácora del tiempo.", "Restando horas al calendario.", "El camino al 2030 continúa.",
        "Un día menos para el cambio.", "La cuenta sigue viva.", "Anotando un día más en el registro.",
        "El contador avanza con el sol.", "Cada jornada nos acerca al objetivo.", "Un día menos en la línea de tiempo.",
        "Manteniendo la constancia: un día menos.", "El reloj del cambio de mando sigue activo."
    ]
    
    texto = random.choice(messages)

    # 2. Cargar credenciales
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # 3. Inicializar el cliente con parámetros de estabilidad
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True
    )

    try:
        print(f"Intentando publicar vía v2: {texto}")
        # user_auth=True es clave para forzar la identidad del bot
        response = client.create_tweet(text=texto, user_auth=True)
        print(f"¡ÉXITO! Tweet publicado. ID: {response.data['id']}")
    except Exception as e:
        print(f"Error en v2: {e}")

if __name__ == "__main__":
    post_tweet()
