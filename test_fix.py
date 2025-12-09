#!/usr/bin/env python3
"""Script para testar a correção"""
import sys
import os

# Adicionar o diretório voos ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'voos'))

from repository.voo_repository import buscar_voos

print("=" * 60)
print("TESTE: Busca de voos após correção")
print("=" * 60)
resultado = buscar_voos("POA", "GRU", "2025-12-10")
print(f"Busca: origem=POA, destino=GRU, data=2025-12-10")
print(f"Quantidade de voos encontrados: {len(resultado)}")
print(f"Tipo do resultado: {type(resultado)}")

if resultado:
    print(f"\nPrimeiro voo:")
    voo = resultado[0]
    print(f"  Tipo: {type(voo)}")
    print(f"  ID: {voo.id}")
    print(f"  Número: {voo.numero_voo}")
    print(f"  Origem: {voo.origem}")
    print(f"  Destino: {voo.destino}")
    print(f"  Data: {voo.data}")
    print(f"  Hora Saída: {voo.hora_saida}")
    print(f"  Hora Chegada: {voo.hora_chegada}")
    print(f"  Preço: {voo.preco}")
    print(f"  Capacidade: {voo.capacidade_disponivel}")
    print(f"  Companhia: {voo.companhia_aerea}")
    
print("\n✅ Correção aplicada com sucesso!")
