import tkinter as tk
from tkinter import ttk

# Arayüz için gerekli kütüphane

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify ile bağlantıyı kurmak için gerekli kütüphane

def spotifyBaglantisi():
    cliend_id = client_id_var.get()  # Client ID değerini almak için
    client_secret = client_secret_var.get()  # Client secret değerini almak için (Paylaşılmaması gereken bir bilgidir, gizli tutulmasında fayda vardır)
    redirect_uri = 'http://localhost:8888/callback'

    if not cliend_id or not client_secret:
        output_text.insert(tk.END, "Lütfen tüm alanları doldurun!\n")  # Eğer Client ID veya Client Secret değerlerinden birisi boş bırakıldıysa hata mesajı yazdır
        return
    
    # Spotify ile bağlantıyı kuruyoruz. Gerekli bilgileri gönderip 'scope' kısmında da izinleri istiyoruz

    global sp
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cliend_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope='user-top-read playlist-modify-public playlist-modify-private'))
    output_text.insert(tk.END, "Spotify ile başarılı şekilde oturum açıldı!\n")
def sarkilariCek():
    time_range = time_range_var.get()  # Zaman aralığı seçimi alınıyor
    limit = int(limit_var.get())  # Liste kaç şarkıdan oluşacak?
    results = sp.current_user_top_tracks(limit=limit, time_range=time_range)  # Belirtilen sayıda şarkı ve zaman aralığınna göre en çok dinlenen şarkı değerlerini 'results' değişkenine atadık

    output_text.delete(1.0, tk.END)  # Metin kutusunu temizleme
    tracks = []

    for idx, track in enumerate(results['items']):  # Index ve şarkı değerlerini alıyoruz
        output_text.insert(tk.END, f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}\n")
        tracks.append(track['uri'])
    return tracks

def playlistOlustur():
    playlist_name = playlist_name_var.get() + ' - TopTracksApp'

    if not playlist_name:
        output_text.insert(tk.END, "Playlist adı boş bırakılamaz!\n")
        return
    
    user_id = sp.current_user()['id']

    playlist = sp.user_playlist_create(user=user_id,
                                       name=playlist_name,
                                       description='The songs that i listened most. Created by Top Tracks App.',
                                       public=True)
    playlist_id = playlist['id']
    tracks = sarkilariCek()
    sp.playlist_add_items(playlist_id, tracks)

    playlist_url = playlist['external_urls']['spotify']
    output_text.insert(tk.END, f"\nPlaylist oluşturuldu: {playlist_url}\n")

# Arayüzü oluşturuyoruz
root = tk.Tk()
root.title("Spotify Top Tracks Playlist Maker App")  # Pencerenin başlığını belirliyoruz.

client_id_label = tk.Label(root, text = "Client ID:")
client_id_label.grid(row=0, column=0, padx=10, pady=10)

client_id_var = tk.StringVar()
client_id_entry = tk.Entry(root, textvariable=client_id_var)
client_id_entry.grid(row=0, column=1, padx=10, pady=10)

client_secret_label = tk.Label(root, text="Client Secret:")
client_secret_label.grid(row=1, column=0, padx=10, pady=10)

client_secret_var = tk.StringVar()
client_secret_entry = tk.Entry(root, textvariable=client_secret_var, show='*')
client_secret_entry.grid(row=1, column=1, padx=10, pady=10)

auth_button = tk.Button(root, text = "Authenicate with Spotify", command=spotifyBaglantisi)
auth_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

time_range_label = tk.Label(root, text="Time Range:")
time_range_label.grid(row=3, column=1, padx=10, pady=10)

time_range_var = tk.StringVar(value="medium_term")
time_range_options = ["short_term", "medium_term", "long_term"]
time_range_menu = ttk.Combobox(root, textvariable=time_range_var, values=time_range_options)
time_range_menu.grid(row=3, column=1, padx=10, pady=10)

limit_label = tk.Label(root, text="Limit:")
limit_label.grid(row=4, column=0, padx=10, pady=10)

limit_var = tk.StringVar(value="50")
limit_entry = tk.Entry(root, textvariable=limit_var)
limit_entry.grid(row=4, column=1, padx=10, pady=10)

playlist_name_label = tk.Label(root, text="Playlist Name:")
playlist_name_label.grid(row=5, column=0, padx=10, pady=10)

playlist_name_var = tk.StringVar()
playlist_name_entry = tk.Entry(root, textvariable=playlist_name_var)
playlist_name_entry.grid(row=5, column=1, padx=10, pady=10)

create_playlist_button = tk.Button(root, text="Create Playlist", command=playlistOlustur)
create_playlist_button.grid(row=6, column=0, padx=10, pady=10)

output_text = tk.Text(root, width=60, height=20)
output_text.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()