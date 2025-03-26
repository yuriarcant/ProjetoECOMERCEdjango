import mercadopago


public_key= "APP_USR-935d17cb-7a88-4ed3-83f1-0fdb209f527c"
token= "APP_USR-3008335894034181-102914-a00cf6b5c2f906edf3ae3d725dae65a2-2066624856"


def criar_pagamento(itens_pedido, link):
#CONFIGURAÇÃO DE CREDENCIAIS
    sdk = mercadopago.SDK(token)

    itens=[]

    for item in itens_pedido:
        quantidade= int(item.quantidade)
        nome_produto= item.item_estoque.produto.nome
        preco_unitario= float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity":quantidade,
            "unit_price": preco_unitario,
        })

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success":link,
            "pending":link,
            "failure":link,
        }
    }
    preference_response= sdk.preference().create(preference_data)
    resposta = preference_response["response"]
    link_pagamento = resposta["init_point"]
    id_pagamento = resposta["id"]
    print(link_pagamento, id_pagamento)
    return (link_pagamento, id_pagamento)

