


import pandas as pd
import matplotlib.pyplot as plt
from django.db import connection
from blogtgl.models import Comment
import io
import base64



def fetch_posts_data():
    # Consulta la base de datos y obtén los datos que necesitas
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, created_at FROM blogtgl_post")
        rows = cursor.fetchall()

    # Crea un DataFrame de Pandas con los resultados
    df = pd.DataFrame(rows, columns=['id', 'title', 'created_at'])

    return df

def plot_post_counts(df):
    # Realiza análisis de datos y crea gráficos
    df['created_at'] = pd.to_datetime(df['created_at'])
    df.set_index('created_at', inplace=True)
    daily_counts = df['id'].resample('D').count()
    
    plt.figure(figsize=(8, 4))
    plt.plot(daily_counts.index, daily_counts.values, marker='o')
    plt.title('Número de publicaciones por día')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad')
    plt.grid(True)

    # Convierte la gráfica en formato base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300)
    plt.close()

    # Convierte los datos binarios en una cadena base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Devuelve la imagen en formato base64
    return image_base64




def fetch_user_comments_data():
    # Consulta la base de datos y obtén los datos que necesitas
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                blogtgl_userprofile.username AS user,
                COUNT(blogtgl_comment.id) AS comment_count
            FROM
                blogtgl_userprofile
            LEFT JOIN
                blogtgl_comment ON blogtgl_userprofile.id = blogtgl_comment.user_id
            GROUP BY
                blogtgl_userprofile.id, blogtgl_userprofile.username
        """)
        rows = cursor.fetchall()

    if not rows:
        # Manejar el caso en el que no se encuentran resultados
        return None

    # Crea un DataFrame de Pandas con los resultados
    df = pd.DataFrame(rows, columns=['user', 'comment_count'])

    return df


def plot_user_comment_distribution():
    # Obtén los datos de los comentarios por usuario
    df = fetch_user_comments_data()

    # Ordena el DataFrame por la cantidad de comentarios en orden descendente
    df = df.sort_values(by='comment_count', ascending=False)

    # Crea la gráfica de barras
    plt.figure(figsize=(8, 4))
    plt.bar(df['user'], df['comment_count'])
    plt.title('Distribución de Comentarios por Usuario')
    plt.xlabel('Usuario')
    plt.ylabel('Cantidad de Comentarios')
    plt.xticks(rotation=90)  # Rota las etiquetas del eje x para una mejor visualización
    plt.tight_layout()

    # Convierte la gráfica en formato base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300)
    plt.close()

    # Convierte los datos binarios en una cadena base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Devuelve la imagen en formato base64
    return image_base64