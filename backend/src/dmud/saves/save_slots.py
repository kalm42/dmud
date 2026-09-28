from typing import Literal

from pydantic import BaseModel, ConfigDict


class EmptySaveSlot(BaseModel):
    """An explicitly empty numbered slot; for example, EmptySaveSlot(number=1, status='empty')."""

    model_config = ConfigDict(strict=True, extra="forbid")
    number: Literal[1, 2, 3]
    status: Literal["empty"]


class SaveSlotsResponse(BaseModel):
    """The current three-slot index; for example, SaveSlotsResponse(slots=[])."""

    model_config = ConfigDict(strict=True, extra="forbid")
    slots: list[EmptySaveSlot]
