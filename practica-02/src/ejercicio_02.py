playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

def duration_to_seconds(duration):
    """Convertir la duración de mm:ss a segundos"""

    minutes, seconds = map(int, duration.split(":"))

    return minutes * 60 + seconds

def seconds_to_duration(secs):
    """Convertir segundos a formato Xm Ys"""

    minutes = secs // 60
    seconds = secs % 60

    return f"{minutes}m {seconds}s"

def process_playlist(playlist):
    """Procesar la lista de canciones para calcular la duración total y ordenar por duración"""

    total_duration = 0

    for song in playlist:
        song["duration_seconds"] = duration_to_seconds(song["duration"])
        total_duration += song["duration_seconds"]

    # Ordenar la lista de canciones por duración en segundos (de mayor a menor)
    playlist.sort(key=lambda x: x["duration_seconds"], reverse=True)

    return total_duration

def print_playlist(playlist=playlist):
    """Imprimir la lista de canciones con su duración y la duración total"""
    
    total_duration = process_playlist(playlist)
    print(f"Duración total: {seconds_to_duration(total_duration)}")

    print(f"Canción más larga: \"{playlist[0]['title']}\" ({playlist[0]['duration']})")
    print(f"Canción más corta: \"{playlist[-1]['title']}\" ({playlist[-1]['duration']})")

if __name__ == "__main__":
    print_playlist()
