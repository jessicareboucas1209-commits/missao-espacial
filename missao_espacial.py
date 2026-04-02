nome_astronauta = input("Digite seu nome completo: ")
distancia_km = float(input("Digite a distância da viagem em quilômetros: "))
velocidade_kmh = float(input("Digite a velocidade média da nave em km/h: "))
tempo_horas = distancia_km / velocidade_kmh
tempo_dias = tempo_horas / 24
print(f"\nAstronauta {nome_astronauta}, bem-vindo à simulação!")
print(f"A viagem terá uma distância de {distancia_km:.0f} km.")
print(f"Com velocidade média de {velocidade_kmh:.0f} km/h, o tempo estimado é:")
print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
print("Boa sorte na missão!")

input("\nProcesso finalizado. Aperte ENTER para sair.")
