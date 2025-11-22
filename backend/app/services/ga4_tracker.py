"""
Google Analytics 4 Event Tracking

Utility module for tracking user interactions and calculator usage.
Integrates with GA4 Measurement Protocol API for server-side event tracking.
"""

import logging

import httpx

from app.core.config import settings

logger = logging.getLogger(__name__)


class GA4Tracker:
    """
    GA4 Measurement Protocol client for server-side event tracking.

    Events are sent asynchronously to GA4 to avoid blocking request handling.
    Only sends events when GA4_MEASUREMENT_ID is configured (disabled in development by default).
    """

    def __init__(self):
        self.measurement_id = settings.GA4_MEASUREMENT_ID
        self.api_secret = getattr(settings, "GA4_API_SECRET", None)
        self.endpoint = "https://www.google-analytics.com/mp/collect"
        self.enabled = bool(self.measurement_id and self.api_secret)

        if not self.enabled:
            logger.info("GA4 tracking disabled (missing measurement ID or API secret)")

    async def track_event(
        self,
        event_name: str,
        client_id: str = "anonymous",
        params: dict | None = None,
    ) -> bool:
        """
        Send an event to GA4.

        Args:
            event_name: Name of the event (e.g., 'calculator_use', 'diagnosis_request')
            client_id: Unique identifier for the user (use session ID or IP hash)
            params: Additional event parameters

        Returns:
            True if event sent successfully, False otherwise
        """
        if not self.enabled:
            logger.debug(f"GA4 disabled, skipping event: {event_name}")
            return False

        try:
            payload = {
                "client_id": client_id,
                "events": [
                    {
                        "name": event_name,
                        "params": params or {},
                    }
                ],
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.endpoint}?measurement_id={self.measurement_id}&api_secret={self.api_secret}",
                    json=payload,
                    timeout=2.0,  # Short timeout to avoid blocking
                )

                if response.status_code == 204:
                    logger.debug(f"GA4 event sent: {event_name}")
                    return True
                else:
                    logger.warning(
                        f"GA4 event failed: {event_name} (status {response.status_code})"
                    )
                    return False

        except Exception as e:
            logger.error(f"GA4 event error: {event_name} - {e}")
            return False


# Global tracker instance
_tracker: GA4Tracker | None = None


def get_tracker() -> GA4Tracker:
    """Get or create the global GA4 tracker instance."""
    global _tracker
    if _tracker is None:
        _tracker = GA4Tracker()
    return _tracker


async def track_calculator_use(
    calculator_name: str, client_id: str = "anonymous", params: dict | None = None
) -> None:
    """
    Track calculator usage event.

    Args:
        calculator_name: Name of calculator used (e.g., 'rotation_distance', 'pressure_advance')
        client_id: User identifier
        params: Additional parameters (e.g., material_type, result values)
    """
    tracker = get_tracker()
    event_params = {"calculator": calculator_name}
    if params:
        event_params.update(params)

    await tracker.track_event(event_name="calculator_use", client_id=client_id, params=event_params)


async def track_diagnosis_request(
    diagnosis_type: str, client_id: str = "anonymous", params: dict | None = None
) -> None:
    """
    Track diagnosis request event.

    Args:
        diagnosis_type: Type of diagnosis ('image' or 'text')
        client_id: User identifier
        params: Additional parameters (e.g., issue_type, classification)
    """
    tracker = get_tracker()
    event_params = {"diagnosis_type": diagnosis_type}
    if params:
        event_params.update(params)

    await tracker.track_event(
        event_name="diagnosis_request", client_id=client_id, params=event_params
    )


async def track_csv_validation_check(
    client_id: str = "anonymous", params: dict | None = None
) -> None:
    """
    Track CSV validation endpoint usage.

    Args:
        client_id: User identifier
        params: Additional parameters (e.g., validation_errors_count)
    """
    tracker = get_tracker()
    await tracker.track_event(
        event_name="csv_validation_check", client_id=client_id, params=params or {}
    )
