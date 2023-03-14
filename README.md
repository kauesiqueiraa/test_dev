<h1 align="center">Desenvolvedor Web (Back/Front-End) - Django/Python</h1>

Uma empresa de assinatura de energia está interessada em criar uma calculadora de economia em seu site e consultou você para desenvolver a calculadora para eles. Você escolheu a linguagem Python e o framework Django para desenvolver a aplicação.  

Sua aplicação receberá as seguintes entradas:

- Três valores representando o consumo de energia elétrica dos últimos 3 meses
- Valor da tarifa da distribuidora
- Tipo de tarifa (Comercial, Residencial e Industrial)

Os resultados da sua aplicação serão:

- Economia Anual
- Economia Mensal
- Desconto Aplicado
- Cobertura

A empresa de assinatura de energia te forneceu as seguintes premissas para o desconto:

| Consumo (Média) | Desconto (Residencial) | Desconto (Comercial) | Desconto (Industrial) |
| --- | --- | --- | --- |
| < 10.000 kWh | 18% | 16% | 12% |
| >= 10.000 kWh e <= 20.000 kWh | 22% | 18% | 15% |
| > 20.000 kWh | 25% | 22% | 18% |

Alem disso, deve-se considerar os seguintes percentuais de cobertura baseado no consumo:

| Consumo (Média) - kWh | < 10.000 kWh | >= 10.000 kWh e <= 20.000 kWh | > 20.000 kWh |
| --- | --- | --- | --- |
| Cobertura*** | 90% | 95% | 99% |

*** Cobertura é o valor da energia que o consumidor irá receber da empresa de assinatura de energia em relação à energia consumida

Requisitos:

1 - A calculadora terá que ser desenvolvida no arquivo calculator.py dentro da função calculator();

2 - Deverá ser utilizado o framework Django para fazer a integração entre a calculadora e a interface;

3 - O candidato terá que criar uma branch nomeada com o seu nome e abrir um pull request para concluir a entrega do teste.

Bônus:

Terá uma pontuação extra o candidato que conseguir disponibilizar a aplicação em Nuvem com um servidor de sua escolha. O candidato deve disponibilizar o link da aplicação no final desta documentação.

Por curiosidade, segue um exemplo de uma calculadora em produção: 
[Simulador - Group Energia - Desconto na conta de luz e gestão de energia](https://groupenergia.com.br/simulador/)
