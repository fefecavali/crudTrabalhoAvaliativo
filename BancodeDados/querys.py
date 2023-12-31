# Parte das consultas

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from classes import Customer, Item, Order_item, Employee, Order, Payment

engine = create_engine('postgresql://EUFACOPROGRAMA:apXBE4kgASy6@ep-damp-waterfall-38037149.us-east-2.aws.neon.tech/mecanica_teste?sslmode=require')
Session = sessionmaker(bind=engine)
session = Session()

# '--> consultas Bruno'
print(f''' \n
---------------------------------
Consultas Bruno Eduardo Pena 
RA: 2461234
--------------------------------- ''')
## 1 ----> SELECT <----
items_with_prices = session.query(Item.name_item_request, Item.price).all()

## 2 ----> COUNT <----
total_items = session.query(Item).count()

## 3 ----> DISTINCT <----
payment_methods = session.query(Order_item.payment).distinct().all()


# '--> consultas Fernanda'
print(f''' \n
---------------------------------
Consultas Fernanda Moreira Cavali 
RA: 2441012
--------------------------------- ''')
#1 Retorne o cliente que possui o id 1234567890
print(f' \n ----> Consulta 1')
id="1234567890"
cliente1 = session.query(Customer).filter_by(id_customer=id).first()

if cliente1:
    print(cliente1)
else:
    print(f'Cliente {id} não encontrado.')

#2 Retorne os carros dos clientes moram na "Avenida araruna fedida"
print(f' \n ----> Consulta 2')

address = "Avenida araruna fedida"
carros_cliente2 = session.query(Customer).filter_by(address_customer=address).all()
for i in carros_cliente2:
    print(f"Cliente: {i.name_customer} possui o carro: {i.car}")

#3 Retorne todos os numeros de pedido da cliente Sara Guaiume

cliente3 = 'Sara Guaiume'
numeros_clientes3 = session.query(Order.id_order, Customer.name_customer).join(Customer, Order.id_customer == Customer.id_customer).filter(Customer.name_customer == cliente3).all()

print(f' \n ----> Consulta 3')
for a in numeros_clientes3:
    print(f'O número de um dos pedidos do cliente {a.name_customer} é {a.id_order}')
print('\n')


#'--> consultas Lara'
print(f''' \n
---------------------------------
Consultas Lara Heloisa Silva Deitos
RA: 2441071
--------------------------------- ''')
#consulta 1: numero de pessoas que pagaram com cartao de crdito
count = session.query(Payment).filter(Payment.name_pay == "cartão").count()
print(f"Total de pessoas que pagaram com cartão de crédito: {count}")

#consulta 2: lista pagamentos com parcelas maiores que 6
filter = session.query(Payment).filter(Payment.portion > 6).all()
for payment in filter:
   print(payment)

#consulta 3: soma formas de pagamento
payment= session.query(Payment.name_pay).distinct().all()
print("Formas de pagamentos:")
for method in payment:
   print(method.name_pay)

'--> consultas Pedro'
print(f''' \n
---------------------------------
Consultas Pedro Felipe Onofre Utumi
RA: 2441160
--------------------------------- ''')
#1
all = session.query(Order).all()
print(all)
session.commit()
#2
orders_ordered = session.query(Order).order_by(Order.id_order).all()
print(orders_ordered)
session.commit()
#3
specific_orders = session.query(Order).filter(Order.id_customer == '21499845678').all()
print(specific_orders)
session.commit()

'--> consultas Sara'
print(f''' \n
---------------------------------
Consultas Sara Stephany Guaiume Cipriano
RA: 2441187
--------------------------------- ''')
#1
data = session.query(Employee).all() #selecionando tudo da tabela employee
print(data[2].wage_employee,data[4].wage_employee) #pegando o salario do objeto na posição 02
session.commit()
#2
data2 = session.query(Employee).filter(Employee.name_employee == 'Bob').all()
print(data2)
#3
data3 = session.query(Employee).filter(Employee.wage_employee < 2000).order_by(Employee.number_employee).all()
print(data3)
