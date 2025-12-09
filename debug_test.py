#!/usr/bin/env python3
"""Script de debug para testar o fluxo de dados"""
import sys
import os

# Adicionar o diretório voos ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'voos'))

from repository.voo_repository import buscar_voos

# Testar diferentes formatos de data
print("=" * 60)
print("TESTE 1: Data no formato do banco (YYYY-MM-DD)")
print("=" * 60)
resultado = buscar_voos("POA", "GRU", "2025-12-10")
print(f"Busca: origem=POA, destino=GRU, data=2025-12-10")
print(f"Resultado: {resultado}")
print(f"Tipo: {type(resultado)}")
if resultado:
    print(f"Primeiro item: {resultado[0]}")
    print(f"Tipo do primeiro item: {type(resultado[0])}")

print("\n" + "=" * 60)
print("TESTE 2: Data no formato DD/MM/YYYY")
print("=" * 60)
resultado2 = buscar_voos("POA", "GRU", "10/12/2025")
print(f"Busca: origem=POA, destino=GRU, data=10/12/2025")
print(f"Resultado: {resultado2}")

print("\n" + "=" * 60)
print("TESTE 3: Verificar estrutura dos dados retornados")
print("=" * 60)
if resultado:
    for idx, linha in enumerate(resultado):
        print(f"\nVoo {idx + 1}:")
        print(f"  Tipo: {type(linha)}")
        print(f"  Conteúdo: {linha}")
        if isinstance(linha, tuple):
            print(f"  Campos: id={linha[0]}, numero_voo={linha[1]}, origem={linha[2]}, destino={linha[3]}, data={linha[4]}")
