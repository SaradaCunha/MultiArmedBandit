__Multi-armed Bandit__

O *Multi-armed Bandit* (Ma-b) trata-se de um problema de *reinforcement learning*. É consituido por um __agente__ que explora as suas opções e faz uma __escolha__ que, no seu __ambiente__, retorna uma __recompensa__ dessa acção. O agente tem de realizar uma escolha entre K acções e recebe uma recompensa a partir de uma distribuição de probabiliades desconhecida, correspondente a essa acção. Assim, o seu objectivo é fazer escolhas que maximizem a sua recompensa total. Relativamente ao ambiente, o seu estado permanece inalterado em todas as fases da experiência, o que facilita o problema MaB. Um bom exemplo, será o caso das máquinas num casino, em que cada máquina tem uma probabilidade específica de gerar uma recompensa. O problema a ser resolvido é o facto de não ser conhecida a distribuição de probabilidade de recompensa à priori. Isto faz com que tenhamos a necessidade de explorar as opções: *explore* e *exploit*. 

__How to use this?__

1. O utilizador terá de inserir as probabilidades de recompensa de cada máquina para o número de máquinas que pretender. Para informar o programa que terminou de definir as probabibilidades associadas a todas as máquinas, terá de inserir um 's' (maiúsculo ou minúsculo). Estas ficarão estáticas para cada vez que correr o programa, assim que para as mudar, será necessário reiniciar o mesmo.

2. Deverá escolher uma das seguintes opções, conforme o algorítmo que pretender correr, ou caso queira sair do programa:
   [1] - Greedy puro
   [2] - Epsilon Greedy
   [3] - Decayed Epsilon Greedy
   [4] - Saida

3.Deverá inserir o número de tentativas que pretende que o programa realize.

4. No caso escolher [2] - Epsilon Greedy, terá de definir o valor a assumir para *epslon*, sendo que este varia entre 0 e 1, e que quanto mais próximo de 1, mais *explore* será a experiência e, quanto menor for o valor do epsilon, mais vezes vamos entrar numa fase de aproveitamento (*exploit*).

__Explaining the code behind it__

1. MAB.py

Criação da classe MAB, que contem 3 funções: 
a) função __init__, que coresponde às definições iniciais do programa que só irá ser corrida uma vez, e que corresponde à tentativa zer e que assume uma estimativa de probabilidade de 100%;
b) função alavanca, que simula o *arm*, ou seja a acção de puxar a alavanca da máquina no casino. Gera um número aleatório e verifica se a probabilidade é menor do que esse número aleatório;
c) função update, que são as probabilidades estimadas para cada máquina. Cada vez que uma máquina é escolhida, é chamada esta função que ajusta a probabilidade estimada, de acordo com o sucesso ou insucesso.

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issue-757970962

2. Programa.ipynb:

1) set_recompensa_máquinas: conforme mencionado, a probabilidade estimada de cada máquina vai ser definida pelo utilizador, esta é a função que o permite, retornando erro sempre que não seja inserido um número decimal entre 0 e 1, um 's' (maiúsculo ou minúsculo).

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issuecomment-739531007

2) teste_epsilon_greedy: o algoritmo de epslon greedy utiliza o tradeoff entre a fase de exploration e exploitation, dando instruções ao computador para fazer *explore* (escolhendo uma opção aleatória com a probabilidade epslon, ou seja, quanto maior for o epsilon, menos greedy irá será a ação) e *exploit* (escolher a máquina que até ao momento parece ser a melhor, dado ter uma probabilidade de recompensa maior nas tentativas já efectuadas), para as restantes vezes.
Sempre que o utilizador escolher esta opção, irá também obter dois gráficos: um para as probabilidades de cada uma das maquinas, tendo em conta o número de tentativas, e o outro para os ganhos acumulados por máquina. Ou seja, percorre o *array* de máquinas (*for j in range..*) e recolhe o número de vezes, em que cada uma de pois seleccionada, teve sucesso.

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issuecomment-739531526

3) teste_epslon_decay: em semelhança à função anterior, esta utiliza o tradeoff entre a fase de exploration e exploitation. No entanto, para esta não é necessário assumir um valor de epsilon estático, dado que é calculado pela função em questão. Assim, numa fase inicial, é importante que o epsilon seja elevado, uma vez que estamos numa fase de descoberta, no entanto à medida que é criado o histórico e podemos ter mais conhecimento sobre as probabiliaddes futuras, o epsilon decai por forma a podermos entrar numa fase de aproveitamento *exploit*, de forma a serem realizadas escolhas mais *greedy*.

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issuecomment-739531554

4) menu: esta é usada para apresentar as opções referidas no ponto 2 do capitulo How to use this, retornando uma mensagem de erro sempre que o digito inserido não for um número inteiro entre 1 e 4.

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issuecomment-739531807

5) funções que definem os *inputs* que o utilizador irá ter de colocar, conforme a opção escolhida.

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issuecomment-739538038

6) esta função permite que seja apresentada a lista das probabilidades definidas pelo utilizador, bem como as diferentes opções. Caso o utilizador insira um número  que não seja um numero inteiro entre 1 e 4, apresentará um print de erro, em conjunto com o menu.

https://github.com/SaradaCunha/MultiArmedBandit/issues/1#issuecomment-739532651
