import tweepy
import os

def post_tweet_api(text, image_path):
    # Extraemos las llaves de las variables de entorno de GitHub
    api_key = os.environ.get("API_KEY")
    api_secret = os.environ.get("API_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

    # Autenticación para subir la IMAGEN (API v1.1)
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api_v1 = tweepy.API(auth)

    # Autenticación para publicar el TWEET (API v2)
    client_v2 = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        # Paso 1: Subir la imagen
        print(f"Subiendo imagen: {image_path}...")
        media = api_v1.media_upload(filename=image_path)
        
        # Paso 2: Publicar el tweet con la imagen
        print("Publicando tweet...")
        client_v2.create_tweet(text=text, media_ids=[media.media_id])
        print("¡Éxito! Tweet enviado.")
        
    except Exception as e:
        print(f"Error detectado: {e}")

# Ejemplo de cómo llamar a la función (asegúrate de que la ruta de la imagen sea correcta)
# post_tweet_api("¡Hola desde GitHub Actions!", "imagen.jpg")
