# Typer CLI entrypoint
if __name__ == "__main__":
    import typer
    app = typer.Typer()
    @app.command()
    def hello():
        print("CLI works")
    app()
