import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db import Base
from app.models import Country, User
from app.schema import schema


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, future=True)
    s = Session()
    try:
        yield s
    finally:
        s.close()


@pytest.fixture
def alice(session):
    user = User(
        name="Alice", mobile="+221700000001", country=Country.SN, balance=1_000_000
    )
    session.add(user)
    session.commit()
    return user


@pytest.fixture
def bob(session):
    user = User(
        name="Bob", mobile="+221700000002", country=Country.SN, balance=1_000_000
    )
    session.add(user)
    session.commit()
    return user


def context(session, user):
    return {"session": session, "current_user": user}


def send_money(session, sender, recipient, amount):
    return schema.execute_sync(
        "mutation { sendMoney(recipientId: %d, amount: %d) { id amount status } }"
        % (recipient.id, amount),
        context_value=context(session, sender),
    )
