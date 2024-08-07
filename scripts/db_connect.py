import psycopg2

def connect_to_db():
    try:
        # Conexão ao banco de dados
        connection = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432",
            database="AtividadesBD"
        )

        cursor = connection.cursor()
        
        # Executar uma consulta SQL
        cursor.execute("SELECT version();")
        
        # Obter o resultado
        db_version = cursor.fetchone()
        print(f"Você está conectado ao - {db_version}\n")

        # Fechar a conexão
        cursor.close()
        connection.close()
        print("Conexão ao PostgreSQL fechada.")

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar-se ao PostgreSQL", error)

if __name__ == "__main__":
    connect_to_db()
