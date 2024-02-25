import campeonatos as camp
import controller as c
import menu as m
import options as o
import time

inicio = time.time()

campeonato = m.obter_escolha(camp.campeonatos)
print(f"Você escolheu: {campeonato['nome']}")
temporada = c.get_last_season(campeonato)
times = c.get_standings(campeonato, temporada)
time_escolhido = m.obter_escolha(times)
jogos = c.get_events(campeonato, temporada, time_escolhido)
statistics = c.get_statistics(jogos)
arquivo = c.create_file(campeonato, time_escolhido, statistics)

fim = time.time()

tempo_total = (fim - inicio) / 60

print(f'Tempo total de execução: {tempo_total:.2f} m')

time.sleep(5)