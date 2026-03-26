posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

def _extract_hashtags(posts):
    """Extrae los hashtags de una lista de posts y cuenta su frecuencia."""

    hashtags = {}
    
    for post in posts:
        words = post.split()
        for word in words:
            if word.startswith("#"):
                hashtag = word.lower()
                if hashtag in hashtags:
                    hashtags[hashtag] += 1
                else:
                    hashtags[hashtag] = 1
    return hashtags

def _trending_hashtags(hashtags):
    """Filtra los hashtags que aparecen más de una vez y los ordena por frecuencia."""

    # Filtrar solo los hashtags que aparecen más de una vez
    trending = {tag: count for tag, count in hashtags.items() if count > 1}
    
    # Ordenar los hashtags por su conteo de mayor a menor
    trending = dict(sorted(trending.items(), key=lambda item: item[1], reverse=True))
    return trending

def print_trending_hashtags(posts):
    """Extrae los hashtags de los posts, identifica los trending y los imprime."""

    hashtags = _extract_hashtags(posts)
    trending = _trending_hashtags(hashtags)

    print("Hashtags trending (más de una aparición):")
    for tag, count in trending.items():
        print(f"  {tag}: {count}")

    print(f"\nTotal de hashtags únicos: {len(hashtags)}")

if __name__ == "__main__":
    print_trending_hashtags(posts)