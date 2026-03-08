from pydantic import BaseModel, Field

class Formulario(BaseModel):
    nome: str = Field(max_length=150, description="Nome deve ter no máximo 100 caracteres")
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$', description="Email deve estar no formato correto", max_length=100)
    mensagem: str = Field(max_length=200, description="Mensagem deve ter no máximo 200 caracteres")
    cpf: str = Field(pattern=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', description="CPF deve estar no formato XXX.XXX.XXX-XX")
    idade: int = Field(ge=20, le=60, description="Idade deve ser entre 20 e 60 anos")
    evento: str = Field(max_length=200, description="Evento deve ser entre 20 e 60 anos")

    def __str__(self):
        return f"Formulario(nome={self.nome}, email={self.email}, mensagem={self.mensagem}, cpf={self.cpf}, idade={self.idade}, evento={self.evento})"

