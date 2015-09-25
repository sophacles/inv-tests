from invoke import ctask as task, Collection


@task
def subtask1(ctx, foo=None):
    if foo is None:
        ctx.run("echo libb st1 no foo")
    else:
        ctx.run("echo libb st1 foo")

@task
def subtask2(ctx):
    ctx.run("echo libb st2")

ns = libb = Collection('libb', subtask1, subtask2)
