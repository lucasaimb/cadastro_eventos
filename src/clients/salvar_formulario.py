from sqlalchemy import text
def salvar_formulario(db, formulario):
    query = text("""
            INSERT INTO formulario
            (nome, email, mensagem, cpf, idade, evento)
            VALUES
            (:nome, :email, :mensagem, :cpf, :idade, :evento)
        """)

    db.execute(
        query,
        {
            "nome": formulario.nome,
            "email": formulario.email,
            "mensagem": formulario.mensagem,
            "cpf": formulario.cpf,
            "idade": formulario.idade,
            "evento": formulario.evento,
        }
    )
    db.commit()