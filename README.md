# wallet-service

A small internal service that powers peer-to-peer (P2P) money transfers.
Users can send money to each other; every transfer is recorded in the
`transfers` table with a status (`pending`, `completed`, `reversed`,
`failed`).

## Layout

- **`app/schema.py`** — GraphQL API (Strawberry), the HTTP-facing layer
- **`app/transfers.py`** — the transfer logic layer: the actual business
  rules for moving money live here, independent of GraphQL
- **`app/models.py`** / **`app/db.py`** — SQLAlchemy models and persistence
- **`app/countries.py`** — static per-country configuration (timezone, currency)
- **`app/auth.py`** — authentication is handled at the edge; resolvers read the
  authenticated user via `get_authenticated_user`
- **`app/__init__.py`** — Flask app exposing a single `/graphql` endpoint

Money amounts are stored as integers in the currency's minor units.

## Running the tests

```
pip install -r requirements.txt
pytest
```
