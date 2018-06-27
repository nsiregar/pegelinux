from invoke import task

@task
def server(ctx):
    ctx.run('waitress-serve app:app', pty=True)
