BITCOIN = 21_000_000  
SATOSHI = 100_000_000     
BLOCKS_HALVING = 210_000  
MAX_HALVINGS = 32         
INICIAL = 50
DIVISOR_EXP = 2


def calcular_suministro_bitcoin():
    halving_contador = 0
    total_suministro = 0  

    print(f"{'Halving':<10}{'Block Reward (SATS)':<25}{'Total Supply (BTC)':<30}{'% of Max Supply':<25}")
    print("="*85)

    while halving_contador <= MAX_HALVINGS:

        recompensa_bitcoin = (INICIAL)/(pow(DIVISOR_EXP,halving_contador))
        recompensa_sats = recompensa_bitcoin * SATOSHI
        suministro_halving = recompensa_bitcoin * BLOCKS_HALVING
        total_suministro += suministro_halving

        percentage_mined = (total_suministro / BITCOIN) * 100

        print(f"{halving_contador:<10}{recompensa_sats:<25,.0f}{total_suministro:<25,.13f}{percentage_mined:<20.13f}%")

        halving_contador += 1

calcular_suministro_bitcoin()