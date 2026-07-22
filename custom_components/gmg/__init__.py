"""The Green Mountain Grill integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Green Mountain Grill component.

    The legacy ``climate: - platform: gmg`` YAML is migrated to a config entry
    from the climate platform's ``async_setup_platform`` import.
    """
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Green Mountain Grill from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
