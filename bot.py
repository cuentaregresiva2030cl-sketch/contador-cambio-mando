from datetime import date
import random

from twitter_api import post_tweet_api
from image_generator import create_image

# Fechas del mandato
start = date(2026,3,11)
end = date(2030,3,11)

today = date.today()

total_days = (end - start).days
days_left = (end - today).days

percent_left = (days_left / total_days) * 100

image = create_image(days_left, percent_left)

messages = [

"Un día menos.",
"La cuenta regresiva continúa.",
"El calendario sigue avanzando.",
"Cada día cuenta.",
"El tiempo pasa.",
"Seguimos avanzando.",
"Otro día en el calendario.",
"Un día más cerca del cambio de mando.",
"El reloj sigue corriendo.",
"La cuenta regresiva sigue.",
"Un día menos en el calendario político.",
"Restando los días.",
"Cada día nos acerca al cambio.",
"El contador sigue bajando.",
"Un día menos para el final del mandato.",
"El tiempo no se detiene.",
"Otro día que pasa.",
"La cuenta sigue bajando.",
"Un día menos en esta historia política.",
"El calendario sigue corriendo.",
"Un día más = a un día menos.",
"Seguimos contando.",
"El tiempo sigue avanzando.",
"Un día menos hacia el cambio.",
"El contador no se detiene.",
"El reloj político sigue.",
"Un día más en la cuenta regresiva.",
"El calendario avanza.",
"El contador sigue su curso.",
"El tiempo sigue su marcha."

]

extra = random.choice(messages)

tweet = f"""
⏳ {days_left} días para el cambio de mando

{extra}

📊 {percent_left:.1f}% queda de este mandato
"""

post_tweet_api(tweet,image)

print("Tweet enviado")
