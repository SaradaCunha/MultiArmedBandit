###__Multi-armed Bandit__###

O *Multi-armed Bandit* (Ma-b) trata-se de um problema de *reinforcement learning*. É consituido por um __agente__ que explora as suas opções e faz uma __escolha__ que, no seu __ambiente__, retorna uma __recompensa__ dessa acção. O agente tem de realizar uma escolha entre K acções e recebe uma recompensa a partir de uma distribuição de probabiliades desconhecida, correspondente a essa acção. Assim, o seu objectivo é fazer escolhas que maximizem a sua recompensa total. Relativamente ao ambiente, o seu estado permanece inalterado em todas as fases da experiência, o que facilita o problema MaB. Um bom exemplo, será o caso das máquinas num casino, em que cada máquina tem uma probabilidade específica de gerar uma recompensa. O problema a ser resolvido é o facto de não ser conhecida a distribuição de probabilidade de recompensa à priori. Isto faz com que tenhamos a necessidade de explorar as opções: *explore* e *exploit*. 

##__How to use this?__##

1. O utilizador terá de inserir as probabilidades de recompensa de cada máquina para o número de máquinas que pretender. Para informar o programa que terminou de definir as probabibilidades associadas a todas as máquinas, terá de inserir um 's' (maiúsculo ou minúsculo). Estas ficarão estáticas para cada vez que correr o programa, assim que para as mudar, será necessário reiniciar o mesmo.

2. Deverá escolher uma das seguintes opções, conforme o algorítmo que pretender correr, ou caso queira sair do programa:
   [1] - Greedy puro
   [2] - Epsilon Greedy
   [3] - Decayed Epsilon Greedy
   [4] - Saida

3.Deverá inserir o número de tentativas que pretende que o programa realize.

4. No caso escolher [2] - Epsilon Greedy, terá de definir o valor a assumir para *epslon*, sendo que este varia entre 0 e 1, e que quanto mais próximo de 1, mais *explore* será a experiência e, quanto menor for o valor do epsilon, mais vezes vamos entrar numa fase de aproveitamento (*exploit*).

##__Explaining the code behind it__##

#1. MAB.py#

Criação da classe MAB, que contem 3 funções: 
a) função __init__, que coresponde às definições iniciais do programa que só irá ser corrida uma vez, e que corresponde à tentativa zer e que assume uma estimativa de probabilidade de 100%;
b) função alavanca, que simula o *arm*, ou seja a acção de puxar a alavanca da máquina no casino;
c) função update, que são as probabilidades estimadas para cada máquina

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issue-757970962

#2. Programa.ipynb:#

1) set_recompensa_máquinas: conforme mencionado, a probabilidade estimada de cada máquina vai ser definida pelo utilizador, esta é a função que o permite, retornando erro sempre que não seja inserido um número decimal entre 0 e 1, um 's' (maiúsculo ou minúsculo).

2)
