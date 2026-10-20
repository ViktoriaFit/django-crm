from django.http import HttpResponse
from .models import Client

def client_list(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        clients = Client.objects.filter(last_name__icontains=search_query)
    else:
        clients = Client.objects.all()
    
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>База клиентов</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #f4f7f6; padding: 20px; margin: 0; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; text-align: center; margin-bottom: 10px; }
            .search-form { display: flex; gap: 10px; margin-bottom: 20px; background: #ecf0f1; padding: 15px; border-radius: 5px; }
            .search-form input { flex: 1; padding: 10px; border: 1px solid #bdc3c7; border-radius: 5px; }
            .search-form button { padding: 10px 20px; background: #3498db; color: white; border: none; border-radius: 5px; cursor: pointer; }
            .admin-btn { display: block; text-align: center; background: #27ae60; color: white; padding: 10px; text-decoration: none; border-radius: 5px; margin-bottom: 20px; }
            .admin-btn:hover { background: #219150; }
            ul { list-style: none; padding: 0; }
            li { background: #ecf0f1; margin-bottom: 15px; padding: 20px; border-radius: 8px; border-left: 5px solid #3498db; }
            .name { font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; display: block; }
            .details { color: #7f8c8d; font-size: 16px; line-height: 1.8; }
            .label { font-weight: bold; color: #34495e; }
            .empty { text-align: center; color: #7f8c8d; font-size: 18px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>База клиентов</h1>
            
            <form method="GET" class="search-form">
                <input type="text" name="search" placeholder="Поиск по фамилии..." value="""" + search_query + """">
                <button type="submit">Найти</button>
            </form>

            <a href="/admin/" class="admin-btn">Добавить клиента (через админку)</a>
            <ul>
    """
    
    if clients:
        for client in clients:
            html += f"""
            <li>
                <span class="name">{client.last_name}</span>
                <div class="details">
                    <span class="label">Занятий:</span> {client.visits}<br>
                    <span class="label">Оплата:</span> {client.payment_date}<br>
                    <span class="label">Действует до:</span> {client.expiry_date}<br>
                    <span class="label">Дни недели:</span> {client.days_of_week}<br>
                    <span class="label">Телефон:</span> {client.phone}
                </div>
            </li>
            """
    else:
        html += "<li class='empty'>Клиентов не найдено.</li>"
        
    html += """
            </ul>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)