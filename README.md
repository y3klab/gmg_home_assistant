# Green Mountain Grill for Home Assistant

> ## 🔥 Community-maintained fork — updated for modern Home Assistant 🔥
>
> **All the credit for this integration belongs to [@jwhitby91](https://github.com/jwhitby91)** — his
> work is what put our Green Mountain grills into Home Assistant in the first place. 🙏
>
> The original stopped loading on **Home Assistant 2025.1 and newer**: HA removed some long-deprecated
> climate constants (`HVAC_MODE_*`, `SUPPORT_TARGET_TEMPERATURE`, `TEMP_FAHRENHEIT`) that `climate.py`
> imports, so the module raises `ImportError` before it can even set up — the kind of upstream API
> churn that eventually catches every integration. This fork **only modernizes `climate.py`** to the
> current climate API so it loads and works again. Verified live on **HA 2026.7.2**; same discovery,
> same features.
>
> **What changed** (only `climate.py`): `HVAC_MODE_*` → `HVACMode.*` · `SUPPORT_TARGET_TEMPERATURE` →
> `ClimateEntityFeature.TARGET_TEMPERATURE` (+ `TURN_ON`/`TURN_OFF` + the new turn-on/off model) ·
> `TEMP_FAHRENHEIT` → `UnitOfTemperature.FAHRENHEIT`.
>
> The fix is also being offered back to the original repo as a PR — if @jwhitby91 ever picks it up
> again, all the better. This fork just keeps his work alive for fellow GMG owners in the meantime.
>
> **Install (HACS):** ⋮ → *Custom repositories* → add `https://github.com/y3klab/gmg_home_assistant`
> as an **Integration** → download it → **restart HA** → then **Settings → Devices & Services → Add Integration → "Green Mountain Grill"**.
> *(Existing `climate: - platform: gmg` YAML setups are auto-migrated to the UI on restart — nothing to change.)* ⚠️ The grill must be on the **same network/subnet as Home Assistant** — it's
> auto-discovered via a UDP broadcast on port 8080 (which doesn't cross VLANs).

---

# Green Mountain Grill for Home Assistant

## **WARNING** This compoment is still in development. Use with caution!  

## Installation

Install via HACS 

<ul>
    <li>click 3 dots in top right</li>
    <li>Custom Repositories</li>
    <li>add this github URI as integration</li>
    <li>click add</li>
    </br>
    <li>click Exlore & download repo bottom right</li>
    <li>Search & select Green Mountain Grill</li>
    <li>Click install</li>
</ul>

Add below to configuration.yaml in home assistant

```yaml
    climate:
        - platform: gmg
```

## Requirements 

<ul>
    <li>UDP port 8080 open between home assistant & GMG</li>
    <li>Auto discovery will discover multiple GMG devices if on same network as home assistant</li>
</ul>

## TODO 

<ul>
    <li>Sensors for
        <ul>
            <li>food probes (temperature monitor.. set temperature etc.) - in development.. Set them up as climate as you can set temp for them </li>
            <li>
                <ul>
                    <li>Need to better detect when probes are unplugged</li>
                </ul>
            </li>
            <li>Warning states..</li>
            <li>Fire States</li>
        </ul>
    </li>
    <li>Test cold smoke mode</li>
    <li>Change Home assistant to use config flow for easier set up</li>
</ul>

## Test list

<ul>
    <li>Power on - successful</li>
    <li>Power off - successful</li>
    <li>Set temp - successful </br><b>Notes:</b> as recommended in GMG manual you shouldn't change temp until it reaches 150 F so I put in check to only change temp once that has been reached</li> 
    <li>Probes - successful</li>
</ul>
