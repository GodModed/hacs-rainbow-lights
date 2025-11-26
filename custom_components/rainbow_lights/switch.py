from homeassistant.components.switch import SwitchEntity

class MySwitch(SwitchEntity):
    _attr_has_entity_name = True
    _attr_name = "Rainbow Lights"  # <-- add a friendly name

    def __init__(self):
        self._is_on = False

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True
        # Notify Home Assistant of state change
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False
        # Notify Home Assistant of state change
        self.schedule_update_ha_state()


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up switches from a config entry."""
    async_add_entities([MySwitch()])


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up switches from YAML/platform configuration (legacy)."""
    add_entities([MySwitch()])