# Projeto Final de curso

Simulação de sistema de detecção de aeronaves invasoras utilizando modelagem baseada em agentes construída em Python

![Ant Simulation GIF](antsimulation.gif)

## Instalação 

1. Clone o repositório:

```bash
git clone https://github.com/danfigueroa/espaco-aereo.git
```

2. Atualize o pip:

```bash
pip install --upgrade pip
```
4. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como rodar a simulação

```bash
mesa runserver
```
Caso a simulação não abra imediatamente no seu browser acesse o link [http://127.0.0.1:8521/](http://127.0.0.1:8521/) e aperte Start.

## Parâmetros da simulação

There are many parameters that can be adjusted to explore different behaviors.

*  *Evaporation Rate*: the percentage of pheromone that disappears each step.
*  *Diffusion Rate*: the percentage of pheromone that is disbursed to surrounding cells each step.
*  *Initial Drop*: the amount of pheromone the ants use at the start of the homing behavior.
*  *Random Move Probability*: the chance that a foraging ant will make a random move instead
of following the pheromone gradient.
*  *Drop Decay Rate*: the exponential decay of the pheromone being
dropped by the ants, such that they leave less pheromone the further away they
are from the food source.