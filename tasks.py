from invoke import task

@task
def server(ctx):
    ctx.run('gunicorn app:app', pty=True)
