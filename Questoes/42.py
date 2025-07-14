from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        total_water = 0

        #Pre calcular a altura max da esquerda de cada barra

        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        #Pre calcular a altura máxima da direita

        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calcular agua pra cada barra
        for i in range(n):
            # A agua q pode ser presa em uma pos e limitada pela menor das duas paredes
            water_level = min(left_max[i], right_max[i])
            
            # A qtd de agua e o nivel de agua menos a altura da barra
            trapped = water_level - height[i]
            
            # so soma se for positivo
            if trapped > 0:
                total_water += trapped

        return total_water
