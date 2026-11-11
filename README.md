# Calculadora de consumo de combustível

Programa simples em Python com uma única tela feita em Tkinter.
Informe a distância percorrida e o combustível consumido para saber o consumo médio do carro em km/l.

## Requisitos

- Python 3 com Tkinter (incluído na instalação padrão do Python para Windows).
- Não precisa instalar pacotes com `pip`.

Em distribuições Linux que não incluam Tkinter, instale o pacote `python3-tk` pelo gerenciador de pacotes do sistema.

## Como executar

Abra o terminal dentro da pasta do projeto e execute:

```bash
python consumo.py
```

No Windows, também é possível usar `py consumo.py`. Em alguns sistemas, o comando é `python3 consumo.py`.

## Como usar

1. Digite a distância percorrida em quilômetros.
2. Digite quantos litros foram consumidos nesse percurso.
3. Clique em **Calcular** ou pressione **Enter**.
4. Use **Limpar** para fazer outro cálculo.

O programa aceita vírgula ou ponto decimal, como `25,5` ou `25.5`. Não use separadores de milhar.
Campos vazios, valores inválidos, zero e números negativos exibem uma mensagem na própria tela.

## Cálculo

**Consumo médio (km/l) = distância percorrida (km) / litros consumidos**

Exemplo: 300 km / 25 litros = **12,00 km/l**.

Para medir por abastecimento, complete o tanque, zere o hodômetro parcial, rode com o carro e complete o tanque novamente. Use a distância percorrida e os litros desse segundo abastecimento. Os litros precisam corresponder ao mesmo percurso informado.

## Arquivos

- `consumo.py`: código completo da aplicação.
- `README.md`: instruções do projeto.
- `.gitignore`: evita enviar arquivos temporários do Python para o GitHub.

Para subir no GitHub, extraia o ZIP e envie os arquivos da pasta `consumo_combustivel` ao seu repositório.
