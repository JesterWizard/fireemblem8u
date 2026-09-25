# ROM Savings

This document tracks space reclaimed inside the linked ROM. These figures are
content savings, not necessarily a reduction in the final `.gba` file size:
the linker still places unrelated assets at fixed addresses near the end of
the ROM.

## Compression savings

- **Portrait tilesets:** 369,000 bytes reduced to 171,748 bytes; saved
  **197,252 bytes** (192.6 KiB).
- **Portrait mouths:** 138,240 bytes reduced to 37,548 bytes; saved
  **100,692 bytes** (98.3 KiB).
- **World-map image:** 76,800 bytes reduced to 76,464 bytes; saved
  **336 bytes** (0.3 KiB).

Compression subtotal: **298,280 bytes** (291.3 KiB).

## Optional content removal

- **Opening animation:** **411,436 bytes** of code/data removed from the
  linked build. The health/safety screen and title screen remain.

## Combined reclaimed content

Compression plus optional removal reclaim **709,716 bytes** (693.1 KiB) of
linked content.

## Current output files

- Padded `fireemblem8.gba`: 16,777,216 bytes (16 MiB).
- Unpadded `fireemblem8.unpadded.gba`: 16,776,960 bytes.
- Trailing file padding: 256 bytes.

Run `make rom_size` to regenerate the size report after rebuilding.
