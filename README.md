# ⚠️ Superseded - this fork is archived

**The maintained version is [`y3klab/gmg-ha`](https://github.com/y3klab/gmg-ha).**
Install that instead; this repository is read-only and will not be updated.

> Do **not** add this repository to HACS. It is pinned at v1.2.0 and still carries a
> temperature bug: grill temperatures are 16-bit little-endian, and reading only the low
> byte makes a 350 °F grill report as **94 °F**. That is fixed in `gmg-ha`.

---

## Why this exists

This was a fork of [`jwhitby91/gmg_home_assistant`](https://github.com/jwhitby91/gmg_home_assistant),
made because the original stopped loading on Home Assistant 2025.1 and newer: HA removed the
long-deprecated climate constants (`HVAC_MODE_*`, `SUPPORT_TARGET_TEMPERATURE`,
`TEMP_FAHRENHEIT`) it imports, so the module raises `ImportError` before it can set up.

**All the credit for getting these grills into Home Assistant belongs to
[@jwhitby91](https://github.com/jwhitby91)** - his integration is what put our Green Mountain
grills into Home Assistant in the first place. 🙏

## The fix is still on offer upstream

That `ImportError` fix was submitted back to the original repo as
**[PR #11](https://github.com/jwhitby91/gmg_home_assistant/pull/11)**, and it is still **open and
mergeable** - 24 lines, one file. It is kept alive deliberately.

**If you just want the original working again**, that PR is the smallest possible change and
needs nothing else. Archiving this repository does not close it; the
`modernize-climate-py` branch it points at stays intact here.

## If you want the maintained version instead

[**`y3klab/gmg-ha`**](https://github.com/y3klab/gmg-ha) carries the same fix plus:

- **Correct temperatures above 255 °F** - the 94 °F bug above
- **Retries short datagrams** instead of parsing them, which used to take every entity offline
- **Serialised I/O** behind one shared coordinator, because the grill answers a single client
- **Adaptive polling**, and unplugged probes reporting `unknown` rather than a 607 °F sentinel
- Protocol handling split into [`gmg-local`](https://pypi.org/project/gmg-local/) on PyPI, usable
  outside Home Assistant

Not affiliated with or endorsed by Green Mountain Grills.
