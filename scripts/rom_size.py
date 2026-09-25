#!/usr/bin/env python3
"""Report ROM padding and space reclaimed by optional removals."""

import argparse
import re
from pathlib import Path


def format_bytes(value):
    return f"{value:,} bytes ({value / 1024:.1f} KiB)"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", type=Path, required=True)
    parser.add_argument("--unpadded", type=Path, required=True)
    parser.add_argument("--map", type=Path, required=True)
    parser.add_argument("--compression-bytes", type=int, default=0)
    parser.add_argument("--removed-bytes", type=int, default=0)
    args = parser.parse_args()

    padded_size = args.rom.stat().st_size
    unpadded_size = args.unpadded.stat().st_size
    padding_size = padded_size - unpadded_size
    map_text = args.map.read_text()
    match = re.search(r"^ROM\s+0x[0-9a-fA-F]+\s+0x([0-9a-fA-F]+)", map_text, re.MULTILINE)
    linked_address_space = int(match.group(1), 16) if match else None

    print("ROM size report")
    print(f"  Padded ROM:   {format_bytes(padded_size)}")
    print(f"  Unpadded ROM: {format_bytes(unpadded_size)}")
    print(f"  End padding:  {format_bytes(padding_size)}")
    if linked_address_space is not None:
        print(f"  Linked range: {format_bytes(linked_address_space)}")
    total_reclaimed = args.compression_bytes + args.removed_bytes
    print(f"  Compression savings: {format_bytes(args.compression_bytes)}")
    print(f"  Optional removal savings: {format_bytes(args.removed_bytes)}")
    print(f"  Total reclaimed content: {format_bytes(total_reclaimed)}")
    print("  Note: removed content creates internal free space when fixed-address")
    print("        sections keep the physical ROM near its maximum size.")


if __name__ == "__main__":
    main()
