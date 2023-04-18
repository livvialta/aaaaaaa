import sqlite3
import datetime

conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

while True:
    print('Escolha uma opcao:')
    print('1. Registre seus gastos: ')
    print('2. Ver o historico de gastos: ')
    
    choice= int(input())

    if choice == 1:
        data = input('Entre com a data do gasto (YYYY-MM-DD): ')
        description = input('Entre aqui com a descrição do gasto: ')
        
        cur.execute('SELECT DISTINCT category FROM expenses') #SELECT DISTINCT -
        
        categories = cur.fetchall  #FETCHALL -
        
        print('Escolha uma categoria pelo numero: ')
        
        for index, category in enumerate(categories):
            print(f'{index + 1}. {category[0]}')
        print(f'{len(categories)+ 1}. Crie uma nova categoria.')

        category_choice = int(input())
        
        if category_choice == len(categories) + 1:
            category = input('Entre com o nome da nova categoria: ')
        else:
            category = categories[category_choice -1][0]

        price = input('Entre com o valor do gasto: ')
        
        cur.execute('INSERT INTO expenses (Date, description, category, price) VALUE (?, ?, ?, ?)', (data, description, category, price))

        conn.commit()

        
    elif choice == 2: 
        print('Escolha uma das opcoes:')
        print('1. Veja o historico completo dos gastos: ')
        print('Veja os gastos do mes por categoria: ')
        
        view_choice = int(input())
        
        if choice == 1:
            cur.execute('SELECT * FROM expenses')
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month = input('Entre com o mes: ')
            year = input('Entre com o ano: ')
            cur.execute("""SELECT category, SUM(price) FROM expenses 
                    WHERE sstrftime('%m', Data) = ? AND strftime('%Y', Data) = ?
                    GROUP BY category(month, year)""")

            expenses = cur.fetchall()
            for expense in expenses:
                print(f'Categoria: {expense[0]}, Total: {expense[1]}')
        else:
            exit()   
    else: 
        exit
        
    repeat = input('Gostaria de fazer mais alguma coisa? (S/N)\n ')
    
    if repeat.lower() != 'y':
        break
    
conn.close()
    
    