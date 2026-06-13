from typing import Literal

from pydantic import Field

from ._base import AnystatModel


class BaseEvent(AnystatModel):
	"""Base fields, for all eventts in Telegram."""
	user_id: int
	timestamp: int | None