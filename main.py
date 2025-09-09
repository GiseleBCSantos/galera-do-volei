from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List
from enum import Enum

app = FastAPI(
    title="API Galera do Volei",
    description="API para gerenciamento de jogadores, times e partidas de vôlei.",
    version="1.0.0"
)

class SexoEnum(str, Enum):
    M = "M"
    F = "F"

class CategoriaTimeEnum(str, Enum):
    Misto = "Misto"
    Feminino = "Feminino"
    Masculino = "Masculino"

class StatusPartidaEnum(str, Enum):
    Nova = "Nova"
    EmAndamento = "Em Andamento"
    Encerrada = "Encerrada"

class Jogador(BaseModel):
    id: int
    nome: str
    email: str
    idade: int
    sexo: SexoEnum

class Time(BaseModel):
    id: int
    nome: str
    categoria: CategoriaTimeEnum

class Partida(BaseModel):
    id: int
    timeAnfitriao: str
    timeConvidado: str
    categoria: CategoriaTimeEnum
    data: str
    local: str
    status: StatusPartidaEnum

router_jogadores = APIRouter(prefix="/api/jogadores", tags=["Jogadores"])
router_times = APIRouter(prefix="/api/times", tags=["Times"])
router_partidas = APIRouter(prefix="/api/partidas", tags=["Partidas"])

@router_jogadores.get("/", response_model=List[Jogador])
def get_jogadores():
    return [
        {"id": 1, "nome": "João", "email": "joao@email.com", "idade": 25, "sexo": "M"},
        {"id": 2, "nome": "Maria", "email": "maria@email.com", "idade": 22, "sexo": "F"},
    ]

@router_jogadores.get("/{id}", response_model=Jogador)
def get_jogador(id: int):
    return {"id": id, "nome": "João", "email": "joao@email.com", "idade": 25, "sexo": "M"}

@router_jogadores.post("/", response_model=Jogador, status_code=201)
def create_jogador(jogador: Jogador):
    return jogador

@router_jogadores.put("/{id}", response_model=Jogador)
def update_jogador(id: int, jogador: Jogador):
    return jogador

@router_jogadores.delete("/{id}", status_code=204)
def delete_jogador(id: int):
    return

@router_times.get("/", response_model=List[Time])
def get_times():
    return [
        {"id": 1, "nome": "Time A", "categoria": "Masculino"},
        {"id": 2, "nome": "Time B", "categoria": "Feminino"},
    ]

@router_times.get("/{id}", response_model=Time)
def get_time(id: int):
    return {"id": id, "nome": "Time A", "categoria": "Masculino"}

@router_times.post("/", response_model=Time, status_code=201)
def create_time(time: Time):
    return time

@router_times.put("/{id}", response_model=Time)
def update_time(id: int, time: Time):
    return time

@router_times.delete("/{id}", status_code=204)
def delete_time(id: int):
    return

@router_times.get("/{id}/jogadores", response_model=List[Jogador])
def get_jogadores_do_time(id: int):
    return [
        {"id": 1, "nome": "João", "email": "joao@email.com", "idade": 25, "sexo": "M"},
        {"id": 3, "nome": "Lucas", "email": "lucas@email.com", "idade": 27, "sexo": "M"},
    ]

@router_times.get("/{id}/partidas", response_model=List[Partida])
def get_partidas_do_time(id: int):
    return [
        {
            "id": 1,
            "timeAnfitriao": "Time A",
            "timeConvidado": "Time B",
            "categoria": "Masculino",
            "data": "2025-10-01",
            "local": "Ginásio Central",
            "status": "Agendada",
        },
        {
            "id": 2,
            "timeAnfitriao": "Time C",
            "timeConvidado": "Time A",
            "categoria": "Masculino",
            "data": "2025-11-01",
            "local": "Ginásio Secundário",
            "status": "Concluída",
        }
    ]

@router_partidas.get("/", response_model=List[Partida])
def get_partidas():
    return [
        {
            "id": 1,
            "timeAnfitriao": "Time A",
            "timeConvidado": "Time B",
            "categoria": "Masculino",
            "data": "2025-10-01",
            "local": "Ginásio Central",
            "status": "Agendada",
        }
    ]

@router_partidas.get("/{id}", response_model=Partida)
def get_partida(id: int):
    return {
        "id": id,
        "timeAnfitriao": "Time A",
        "timeConvidado": "Time B",
        "categoria": "Masculino",
        "data": "2025-10-01",
        "local": "Ginásio Central",
        "status": "Agendada",
    }

@router_partidas.post("/", response_model=Partida, status_code=201)
def create_partida(partida: Partida):
    return partida

@router_partidas.put("/{id}", response_model=Partida)
def update_partida(id: int, partida: Partida):
    return partida

@router_partidas.delete("/{id}", status_code=204)
def delete_partida(id: int):
    return

@router_partidas.get("/{id}/times", response_model=List[Time])
def get_times_da_partida(id: int):
    return [
        {"id": 1, "nome": "Time A", "categoria": "Masculino"},
        {"id": 2, "nome": "Time B", "categoria": "Masculino"},
    ]

@router_partidas.get("/{id}/jogadores", response_model=List[Jogador])
def get_jogadores_da_partida(id: int):
    return [
        {"id": 1, "nome": "João", "email": "joao@email.com", "idade": 25, "sexo": "M"},
        {"id": 2, "nome": "Maria", "email": "maria@email.com", "idade": 22, "sexo": "F"},
    ]

app.include_router(router_jogadores)
app.include_router(router_times)
app.include_router(router_partidas)
