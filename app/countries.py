"""Static per-country configuration."""

from dataclasses import dataclass

from .models import Country


@dataclass(frozen=True)
class CountryInfo:
    timezone: str  # IANA timezone name
    currency: str  # ISO 4217 currency code


COUNTRY_INFO = {
    Country.SN: CountryInfo(timezone="Africa/Dakar", currency="XOF"),
    Country.CI: CountryInfo(timezone="Africa/Abidjan", currency="XOF"),
    Country.CM: CountryInfo(timezone="Africa/Douala", currency="XAF"),
    Country.NE: CountryInfo(timezone="Africa/Niamey", currency="XOF"),
    Country.UG: CountryInfo(timezone="Africa/Kampala", currency="UGX"),
}
