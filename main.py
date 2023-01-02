import discord
import requests
from PIL import Image

client = discord.Client()

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user.name}!')

@client.event
async def on_message(message):
    if message.content.startswith('!generuj'):
        # Pobierz życzenie użytkownika
        user_request = message.content[len('!generuj'):].strip()

        # Generuj obrazek
        image_url = generate_image(user_request)

        # Przeslij obrazek do kanału
        await message.channel.send(file=discord.File(image_url))

def generate_image(request):
    # Ustaw klucz API Unsplash
    api_key = 'YOUR_UNSPLASH_API_KEY'

    # Wyszukaj obrazki za pomocą Unsplash API
    api_url = f'https://api.unsplash.com/photos/random?query={request}&client_id={api_key}'
    response = requests.get(api_url)
    data = response.json()

    # Pobierz URL obrazka
    image_url = data['urls']['full']

    # Pobierz obrazek z sieci i zapisz go do pliku lokalnego
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    file_path = f'{request}.jpg'
    image.save(file_path)

    # Zwróć ścieżkę do pliku
    return file_path

client.run('YOUR_BOT_TOKEN')
