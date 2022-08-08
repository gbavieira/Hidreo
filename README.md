# Hydric Potential Calculator for the customers of Hidreo energy solutions

This repository is a project made for Hidreo energy solutions website. It is a hydric potential calculator. To understand their businesse, please check their website: [Hidreo] (https://hidreo.com.br/)

## Understanding the calculator

Hidreo has a product that generates power through the flow of water from a river with a determined slope. Therefore, the calculator can show the customers how much energy, as well as how many products they can buy, according to their river's slope and water flow. It has two ways of calculating it: the basic and the advanced.

The Basic calculator is meant for those who only want to know in simple way how much power a river can generate. While the Advanced Calculator is meant for those who wants a more precise calculation and customizing the way the installatin will be done. Basically, you input more data about how far the river will be from the product installation and how far this is from the electric connection.

## Tools and Development

To create the calculator, we wanted a database to store the information on the customers that used any of the options to simulate their rivers power. To do so, I have used a [PostgreSQL database](https://www.postgresql.org/) as it is very simple to integrate with [Django Framework](https://www.djangoproject.com/) and the [Amazon Web Services](https://aws.amazon.com/pt/?nc2=h_lg).

Both models use some clients information as Name, Mobile, CPF or CNPJ, E-mail and the Power Distribuition Companys Name.
The Basic Calculator needs only the Water Flow, Slope, Model as inputs, while it calculates the Power and MCHs.

While the Advanced Calculator needs some more information as the 'Distance between the MCH and the river', the 'Distance between the MCH and the power connection' and the type of the cable the customer wants to use (Copper or Aluminum).

The file forms.py contains all the forms rules, as making some fields hidden, so they can be stored in the database but are not a a field in the users input, such as Power and MCHs number.

The views.py contains all the math calculations that are required for the calculator. The rules are mostly physicis and math, but it was need some logic to implement all the information.

## Demo

A demo is available in my own [Portfolio Website](https://gbavieira.com/): [Calculator Index](https://gbavieira.com/calculadora)

## Next Steps

Refactorate and maintain. Correct some small bugs and integrate the calculator to Hidreos website.
