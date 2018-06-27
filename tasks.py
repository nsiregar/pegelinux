from invoke import task

@task
def server(ctx):
    ctx.run('waitress-serve --host=0.0.0.0 --port=5000 app:app', pty=True)
