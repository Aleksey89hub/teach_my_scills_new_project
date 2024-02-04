from enum import Enum


class AssertMessage(Enum):
    TITLE_SHOULD_BE_SHOWN = "The title {} should be shown"
    TEXT_SHOULD_BE_SHOWN = "The text {} should be shown"
    FIELD_SHOULD_BE_CLEANED = "The text should be cleaned"
    ALERT_SHOULD_BE_DISMISSED = "Alert should be dismissed"
    FILE_SHOULD_BE_DOWNLOADED = "File should be downloaded"
