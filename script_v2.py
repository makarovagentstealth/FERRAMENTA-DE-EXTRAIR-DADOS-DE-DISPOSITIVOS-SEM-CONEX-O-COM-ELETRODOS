import hashlib
import json
from datetime import datetime

class DarkstrikePendrive:
    def __init__(self, config):
        # Propriedades Físicas (Unidades SI)
        self.comprimento = config["comprimento"]  # metros
        self.largura = config["largura"]          # metros
        self.massa = config["massa"]              # quilogramas
        self.material = config["material"]        # ex: "plástico ABS + cobre"
        
        # Propriedades Digitais
        self.capacidade = config["capacidade"]    # bytes
        self.sistema_arquivos = config["sistema_arquivos"]
        self.uuid = config["uuid"]
        
        # Contexto Ambiental (Monitorado via sensores)
        self.temperatura = config["temperatura"]  # Kelvin
        self.umidade = config["umidade"]          # porcentagem
        
        # Metadados Dinâmicos (Atualizados a cada acesso)
        self.ultimo_acesso = datetime.now().isoformat()
        self.entropia_quantica = 0.0  # Medida de aleatoriedade quântica (0-1)
        
    def gerar_assinatura_darkstrike(self):
        # Passo 1: Calcular geometria fractal do dispositivo
        volume = self.comprimento * self.largura * 0.001  # Supondo altura fixa de 1mm
        fractal_geo = (volume ** 0.5) * (self.massa / 1000)  # Fator de forma
        
        # Passo 2: Incorporar ressonância de elementos químicos
        elementos = {
            "Cu": 0.45 if "cobre" in self.material else 0.0,
            "Au": 0.12 if "ouro" in self.material else 0.0
        }
        ressonancia = sum(elementos.values()) * self.temperatura / 300
        
        # Passo 3: Gerar hash quântico-contextual (SHA3-512 para resistência quântica)
        dados = f"{fractal_geo}-{ressonancia}-{self.capacidade}-{self.ultimo_acesso}"
        hash_quantico = hashlib.sha3_512(dados.encode()).hexdigest()
        
        # Passo 4: Atualizar entropia (simulação de medição quântica)
        self.entropia_quantica = (hash_quantico.count('a') + hash_quantico.count('f')) / 128
        
        return {
            "assinatura": hash_quantico,
            "entropia": self.entropia_quantica,
            "timestamp": self.ultimo_acesso
        }

# --- Configuração de Teste Padrão DARKSTRIKEAPT ---
config_padrao = {
    "comprimento": 0.03,      # 3 cm
    "largura": 0.01,          # 1 cm
    "massa": 0.015,           # 15 gramas
    "material": "plástico ABS + cobre",
    "capacidade": 2147483648, # 2 GB
    "sistema_arquivos": "FAT32",
    "uuid": "DS-9A7F-41D4-B3A2",
    "temperatura": 298.15,    # 25°C
    "umidade": 45.0
}

# Inicializar pendrive para testes
pendrive_ds = DarkstrikePendrive(config_padrao)
resultado = pendrive_ds.gerar_assinatura_darkstrike()

print("=== Assinatura Quântica DARKSTRIKEAPT ===")
print(f"Hash: {resultado['assinatura']}")
print(f"Entropia: {resultado['entropia']:.4f}")
print(f"Timestamp: {resultado['timestamp']}")
