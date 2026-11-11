"""Calculadora de consumo de combustível com interface Tkinter."""

import math
import tkinter as tk
from tkinter import ttk


def ler_numero(texto, campo):
    """Aceita números positivos com vírgula ou ponto decimal."""
    try:
        valor = float(texto.strip().replace(",", "."))
    except ValueError:
        raise ValueError(f"Informe um número válido em {campo}.") from None
    if not math.isfinite(valor) or valor <= 0:
        raise ValueError(f"O valor de {campo} deve ser maior que zero.")
    return valor


def calcular_consumo(distancia, litros):
    """Retorna o consumo médio em quilômetros por litro."""
    if not all(math.isfinite(v) and v > 0 for v in (distancia, litros)):
        raise ValueError("Distância e litros devem ser números positivos.")
    consumo = distancia / litros
    if not math.isfinite(consumo) or consumo == 0:
        raise ValueError("Os valores informados estão fora do intervalo permitido.")
    return consumo


class CalculadoraConsumo:
    def __init__(self, janela):
        janela.title("Consumo de combustível")
        janela.minsize(400, 310)

        painel = ttk.Frame(janela, padding=24)
        painel.pack(fill="both", expand=True)
        painel.columnconfigure(0, weight=1)

        ttk.Label(
            painel, text="Calculadora de consumo", font=("Arial", 15, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 18))

        ttk.Label(painel, text="Distância percorrida (km):").grid(
            row=1, column=0, sticky="w"
        )
        self.distancia = ttk.Entry(painel)
        self.distancia.grid(row=2, column=0, sticky="ew", pady=(4, 12))

        ttk.Label(painel, text="Combustível consumido (litros):").grid(
            row=3, column=0, sticky="w"
        )
        self.litros = ttk.Entry(painel)
        self.litros.grid(row=4, column=0, sticky="ew", pady=(4, 16))

        botoes = ttk.Frame(painel)
        botoes.grid(row=5, column=0, sticky="w")
        ttk.Button(botoes, text="Calcular", command=self.calcular).pack(side="left")
        ttk.Button(botoes, text="Limpar", command=self.limpar).pack(
            side="left", padx=(8, 0)
        )

        self.resultado = ttk.Label(painel, text="", wraplength=350)
        self.resultado.grid(row=6, column=0, sticky="w", pady=(18, 0))
        janela.bind("<Return>", lambda evento: self.calcular())
        self.distancia.focus_set()

    def calcular(self):
        try:
            distancia = ler_numero(self.distancia.get(), "distância")
            litros = ler_numero(self.litros.get(), "combustível")
            consumo = calcular_consumo(distancia, litros)
        except ValueError as erro:
            self.resultado.config(text=str(erro), foreground="#b00020")
            return

        # Vírgula decimal na apresentação do resultado.
        valor = f"{consumo:.2f}".replace(".", ",")
        self.resultado.config(
            text=f"Consumo médio: {valor} km/l", foreground="#165d24"
        )

    def limpar(self):
        self.distancia.delete(0, tk.END)
        self.litros.delete(0, tk.END)
        self.resultado.config(text="")
        self.distancia.focus_set()


if __name__ == "__main__":
    janela = tk.Tk()
    CalculadoraConsumo(janela)
    janela.mainloop()
