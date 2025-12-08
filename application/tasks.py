from sys import platform
from subprocess import call
from invoke import task



@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))

@task
def test(ctx):
    ctx.run("poetry run pytest ", pty=True)

@task
def lint(ctx):
    ctx.run("poetry run pylint src/ ", pty=True)

@task
def build(ctx):
    ctx.run("poetry install", pty=True)



@task
def format(ctx):
    ctx.run("poetry run autopep8 -v --in-place --recursive src")
