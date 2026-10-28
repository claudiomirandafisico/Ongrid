"""
Calculadora Solar Fotovoltaica - Dimensionamiento Base (On-Grid / Híbrido)
Zona: Cauquenes, Chile
Autor: Instalador Eléctrico Clase D
"""

def calcular_sistema_solar():
    print("=" * 60)
    print(" DIMENSIONAMIENTO DE SISTEMA FOTOVOLTAICO (CAUQUENES)")
    print("=" * 60)
    
    # Parámetros de entrada (basados en tu levantamiento)
    consumo_anual_kwh = 4500         # kWh / año
    cobertura_deseada = 0.70          # 70% del consumo total
    hsp_anual = 5.0                   # Horas de Sol Pico promedio anual (Cauquenes)
    potencia_panel_wp = 520           # Wp por panel
    tarifa_kwh_clp = 160              # CLP / kWh (Costo aproximado de la energía de red)
    costo_estimado_por_kwp = 1100000  # Costo referencial instalación CLP por kWp

    # 1. Cálculos principales
    energia_a_generar_kwh = consumo_anual_kwh * cobertura_deseada
    # Potencia (kWp) = Energía anual / (HSP * 365 días * eficiencia del sistema ~0.8)
    eficiencia_sistema = 0.80
    tamano_sistema_kwp = energia_a_generar_kwh / (hsp_anual * 365 * eficiencia_sistema)
    
    # 2. Número de paneles
    potencia_panel_kwp = potencia_panel_wp / 1000.0
    num_paneles = round(tamano_sistema_kwp / potencia_panel_kwp)
    tamano_real_kwp = num_paneles * potencia_panel_kwp
    
    # 3. Superficie estimada (aprox 2.3 m² por panel de 520W)
    superficie_aprox_m2 = num_paneles * 2.3
    
    # 4. Inversor recomendado (AC) - Debe cubrir la potencia nominal del arreglo
    inversor_recomendado_kwac = tamano_real_kwp * 0.85 # Factor de sobredimensionamiento típico
    
    # 5. Ahorro económico y financiero
    ahorro_anual_clp = energia_a_generar_kwh * tarifa_kwh_clp
    costo_total_estimado_clp = tamano_real_kwp * costo_estimado_por_kwp
    retorno_inversion_anos = costo_total_estimado_clp / ahorro_anual_clp if ahorro_anual_clp > 0 else 0

    # 6. Emisiones evitadas (Factor de emisión estándar SEN Chile ~0.37 kg CO2/kWh)
    co2_evitado_kg = energia_a_generar_kwh * 0.37
    arboles_equivalentes = round(co2_evitado_kg / 21) # Un árbol absorbe aprox 21 kg CO2/año

    # Resultados en Consola
    print(f"\n[ RESULTADOS DEL CÁLCULO ]")
    print(f"• Tamaño del sistema: {tamano_real_kwp:.2f} kWp")
    print(f"• Producción anual estimada: {energia_a_generar_kwh:,.0f} kWh/año")
    print(f"• Número de paneles: {num_paneles} unid. ({potencia_panel_wp}Wp c/u)")
    print(f"• Superficie aproximada: {superficie_aprox_m2:.1f} m² de paneles")
    print(f"• Inversor recomendado (AC): {inversor_recomendado_kwac:.2f} kWac")
    print(f"• Costo total estimado: ${costo_total_estimado_clp:,.0f} pesos")
    print(f"• Ahorro anual estimado: ${ahorro_anual_clp:,.0f} pesos")
    print(f"• Retorno de la inversión: {retorno_inversion_anos:.1f} años")
    print(f"• CO2 evitado por año: {co2_evitado_kg:.0f} kg CO2/año")
    print(f"• Equivale a plantar: {arboles_equivalentes} árboles/año")
    print("=" * 60)

if __name__ == "__main__":
    calcular_sistema_solar()