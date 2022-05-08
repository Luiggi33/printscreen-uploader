import requests

u = requests.post(
    'https://print-screen.dev/api/upload/index.php',
    data={
        'auth': 'YOUR AUTH',
        'secure': 'YOUR SECURE',
        'url': '', # not required but can be added
    },
    files={
        'sharex': ('image.png', open('image.png', 'rb'), 'image/png'),
    },
)

pic_id = u.json()['url'][25:]

print(u.json().get('url'), pic_id)
