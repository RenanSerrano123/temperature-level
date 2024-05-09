def verificar_mensagem_temperatura(temperatura):
    if temperatura <= -20:
        return "Muito Baixa"
    elif -20 < temperatura < 30:
        return "Baixa"
    elif 30 <= temperatura < 200:
        return "Normal"
    elif 200 <= temperatura < 250:
        return "Alta"
    else:
        return "Muito Alta"
def main():
    temperatura = float(input())
    mensagem = verificar_mensagem_temperatura(temperatura)
    print(f"{mensagem}")
main()