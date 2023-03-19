import nox


@nox.session(python=['3.8'])
def tests(session):
    # pass along args to pytest
    args = session.posargs or ['--cov']
    # poetry is not part of the environment created by Nox,
    # so we specify external to void warnings about external
    # commands leaking into the isolated test environments
    session.run('poetry', 'install', external=True)
    session.run('pytest', *args)
