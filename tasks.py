from invoke import task


@task
def server(ctx):
    ctx.run("gunicorn app:app", pty=True)


@task
def clean(ctx):
    ctx.run("black app")
