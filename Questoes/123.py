class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        numero_de_dias = len(prices)

        lucro_max_ate_o_dia = [0] * numero_de_dias
        menor_preco_encontrado = prices[0]

        for i in range(1, numero_de_dias):
            menor_preco_encontrado = min(menor_preco_encontrado, prices[i])
            lucro_se_vendesse_hoje = prices[i] - menor_preco_encontrado
            lucro_max_ate_o_dia[i] = max(lucro_max_ate_o_dia[i-1], lucro_se_vendesse_hoje)

        lucro_max_a_partir_do_dia = [0] * numero_de_dias
        maior_preco_encontrado = prices[numero_de_dias-1]

        for i in range(numero_de_dias - 2, -1, -1):
            maior_preco_encontrado = max(maior_preco_encontrado, prices[i])
            lucro_se_comprasse_hoje = maior_preco_encontrado - prices[i]
            lucro_max_a_partir_do_dia[i] = max(lucro_max_a_partir_do_dia[i+1], lucro_se_comprasse_hoje)

        lucro_total_maximo = 0
        for i in range(numero_de_dias):
            lucro_combinado_no_dia_i = lucro_max_ate_o_dia[i] + lucro_max_a_partir_do_dia[i]
            lucro_total_maximo = max(lucro_total_maximo, lucro_combinado_no_dia_i)
            
        return lucro_total_maximo