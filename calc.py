import typer

app = typer.Typer()

@app.command()
def soma(a: int, 
         b: int, 
         c: int = typer.Argument(0, help="Este Terceiro numero não é obrigatorio"),
         inverte: bool = True):
    if inverte == True:
        print(f'a soma é {a + b + c}')
    else:
        print(f'a subtração é {a - b - c}')


@app.command()
def multiplica(a: int, b: int):
    print(f'Resultado: {a * b}')
    
if __name__ == '__main__':
    app()
