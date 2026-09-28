from dmud.saves.save_slots import EmptySaveSlot, SaveSlotsResponse


def get_save_slots() -> SaveSlotsResponse:
    """Read the foundation's empty index without opening branch state; for example, GET /api/save-slots."""
    return SaveSlotsResponse(
        slots=[
            EmptySaveSlot(number=1, status="empty"),
            EmptySaveSlot(number=2, status="empty"),
            EmptySaveSlot(number=3, status="empty"),
        ]
    )
