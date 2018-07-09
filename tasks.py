from time import sleep

from invoke import task


@task
def server(ctx):
    ctx.run("gunicorn app:app", pty=True)


@task
def clean(ctx):
    ctx.run("black app")


@task
def docker_server(ctx, command):
    if command == "start":
        ctx.run("docker-compose up -d db")
        sleep(1)
        ctx.run("docker-compose up web")
    elif command == "stop":
        ctx.run("docker-compose stop")
    else:
        print("start or stop")


@task
def docker_build(ctx):
    ctx.run("docker-compose build")