import os
from dotenv import load_dotenv

load_dotenv()

# Cargo forte: título que só existe mesmo em vaga de dados/produto/BI, sem
# possibilidade real de ser outra área.
KEYWORDS_CARGO_FORTE = [
    "Analista de Dados",
    "Data Analyst",
    "Analista de Produto",
    "Product Analyst",
    "Product Analytics",
    "Analista de Performance",
    "Analista de Estratégia",
    "Analista de Desempenho",
]

# Cargo ambíguo: título que também é usado em vaga sem nada a ver com
# dados/produto (ex: "Business Analyst" e "Analista de Negócios" existem em
# TI, finanças, RH, operações... qualquer área). Só conta como match se o
# título TAMBÉM tiver um QUALIFICADORES_DADOS junto.
KEYWORDS_CARGO_AMBIGUO = [
    "Business Analyst",
    "Analista de Negócios",
    "Business Analytics",
]

# Termo que precisa aparecer junto no título quando o cargo é ambíguo, pra
# confirmar que é vaga de dados/produto/BI e não de outra área qualquer.
QUALIFICADORES_DADOS = [
    "dados",
    "data",
    "bi",
    "sql",
    "power bi",
    "excel",
    "analytics",
    "kpi",
    "dashboard",
    "métricas",
    "reporting",
    "insights",
]

# Ferramenta que aparece como núcleo do título ("Analista de Power BI").
# Só conta como match se o título TAMBÉM tiver uma palavra de cargo.
FERRAMENTAS_TITULO = [
    "Power BI",
]

# Palavra de cargo que confirma que a vaga de ferramenta é de análise.
# "desenvolvedor"/"developer"/"engenheiro" ficam FORA de propósito: é o que
# mantém vaga de dev fora do radar.
QUALIFICADORES_CARGO = [
    "analista",
    "analyst",
    "especialista",
    "specialist",
    "consultor",
    "consultant",
]

KEYWORDS = KEYWORDS_CARGO_FORTE + KEYWORDS_CARGO_AMBIGUO

# Termos de busca enviados a cada site. Ficam separados das KEYWORDS de
# propósito: TERMOS_BUSCA é a rede ampla (o que é pesquisado em cada site),
# enquanto KEYWORDS é o filtro final e só olha o título da vaga já
# encontrada.
TERMOS_CARGO_EXTRA = [
    "power bi",
]

TERMOS_CARGO = sorted(set(k.lower() for k in KEYWORDS) | set(TERMOS_CARGO_EXTRA))

TERMOS_FERRAMENTA = [
    "sql",
    "excel",
    "power bi",
]

TERMOS_BUSCA = TERMOS_CARGO + TERMOS_FERRAMENTA

TERMOS_POR_CICLO = 10

# Onde vaga HIBRIDA ou PRESENCIAL e aceita (mais "Remoto", que nao e
# cidade e sim a porta de entrada da regra de modalidade remota — ver
# _FLAGS_REMOTO em job.py). Vaga hibrida/presencial fora desta lista e
# rejeitada; e uma whitelist, nao uma preferencia de ordenacao.
#
# Customizado para o perfil da usuária: presencial/híbrida aceita em
# Guarulhos e São Paulo capital, além de vaga remota (via "Remoto").
CIDADES = [
    "Remoto",
    "Guarulhos",
    "São Paulo",
]

# Eixo Europa/Ibérico e mercados internacionais: desligados, pois a
# usuária só quer vagas do Brasil.
CIDADES_EUROPA_IBERICA = [
    "Portugal",
    "Lisboa",
    "Porto",
    "Braga",
    "Espanha",
    "España",
    "Spain",
    "Madrid",
    "Barcelona",
    "Valencia",
]

ATIVAR_EIXO_IBERICO_BR = False

# Mercado "casa": busca modalidade completa (presencial/híbrida + remoto).
LOCATIONS_LINKEDIN = ["Brasil"]

# Mercados adicionais (remoto apenas): desligado, usuária só quer Brasil.
LOCATIONS_LINKEDIN_REMOTO_APENAS = []

LOCATIONS_LINKEDIN_CIDADES_PRESENCIAL = [c for c in CIDADES if c != "Remoto"]

# Mercado que a vaga remota precisa aceitar pra contar, quando o texto de
# local DECLARA um escopo geográfico. Restrito ao Brasil.
MERCADOS_REMOTO_ACEITOS = ["Brasil"]

INTERVALO_MINUTOS = int(os.getenv("INTERVALO_MINUTOS", 180))

# Digest ranqueado: vaga com Job.pontuar_relevancia() >= este limiar
# notifica na hora; abaixo disso, fica na fila do digest diário.
LIMIAR_DIGEST_IMEDIATO = 7

# Hora UTC em que o digest diário dispara. 0 = meia-noite UTC = 21h em
# Brasília (UTC-3).
DIGEST_HORA_UTC = 0

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

# Caminho ancorado na RAIZ do projeto, não na pasta deste arquivo.
_RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.getenv("JOBRADAR_DB_PATH") or os.path.join(_RAIZ_PROJETO, "data", "jobs.db")
