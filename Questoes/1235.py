import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        
        numero_de_trabalhos = len(startTime)
        trabalhos_ordenados = sorted(zip(endTime, startTime, profit))

        horas_de_fim_ordenadas = [trabalho[0] for trabalho in trabalhos_ordenados]
        
        lucro_maximo_ate_i = [0] * numero_de_trabalhos
        
        for i in range(numero_de_trabalhos):
            hora_de_fim, hora_de_inicio, lucro_do_trabalho = trabalhos_ordenados[i]
            
            lucro_se_agendar_o_trabalho_atual = lucro_do_trabalho
            
            indice_ultimo_compativel = bisect.bisect_right(horas_de_fim_ordenadas, hora_de_inicio) - 1
            
            if indice_ultimo_compativel >= 0:
                lucro_se_agendar_o_trabalho_atual += lucro_maximo_ate_i[indice_ultimo_compativel]
                
            lucro_se_nao_agendar_o_trabalho_atual = lucro_maximo_ate_i[i-1] if i > 0 else 0
            
            lucro_maximo_ate_i[i] = max(lucro_se_agendar_o_trabalho_atual, lucro_se_nao_agendar_o_trabalho_atual)
            
        return lucro_maximo_ate_i[-1]

solver = Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
print(f"Lucro máximo para o exemplo 1: {solver.jobScheduling(startTime, endTime, profit)}")

startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(f"Lucro máximo para o exemplo 2: {solver.jobScheduling(startTime, endTime, profit)}")