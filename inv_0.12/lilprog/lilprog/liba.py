from invoke import ctask as task, Collection


@task
def subtask1(ctx, foo=None):
    if foo is None:
        ctx.run("echo st1 no foo")
    else:
        ctx.run("echo st1 foo")

@task
def subtask2(ctx):
    ctx.run("echo st2")

ns = liba = Collection('liba', subtask1, subtask2)

