from .const import DOMAIN

async def async_setup_entry(hass, entry):
    # Forward setup to the switch platform so entities get created
    await hass.config_entries.async_forward_entry_setups(entry, ["switch"])
    return True