# Pacote voos
import sys
from pathlib import Path

# Adicionar o diretório atual (voos) ao sys.path para importações absolutas
sys.path.insert(0, str(Path(__file__).parent))