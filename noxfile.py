import nox

@nox.session(python='3.8')
def tests(session):
    session.run('pip', 'install', '-r', 'requirements.txt', external=True)
    session.run('pytest', '-v', 'tests', external=True)
