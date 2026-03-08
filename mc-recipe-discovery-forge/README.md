# mc-recipe-discovery — Forge Mod

A Minecraft 1.21.1 Forge mod that locks all crafting recipes behind Knowledge
Books hidden in structure chests. Find them to learn them.

## Why a mod instead of a datapack?

This Forge version uses **Global Loot Modifiers (GLM)** — an API that *adds*
a pool to any loot table without overriding it. This means:

- ✅ Zero load-order issues
- ✅ Fully compatible with Dungeons and Taverns (built-in, automatic)
- ✅ Compatible with any other mod that modifies the same loot tables
- ✅ Enabling/disabling doLimitedCrafting is handled on world join

## Requirements

- Minecraft 1.21.1
- Forge 52.x  (https://files.minecraftforge.net)
- Fabric is NOT supported — use the datapack version or NeoForge port

## Building from source

```bash
# 1. Set up the Forge MDK
#    Download the MDK from https://files.minecraftforge.net for 1.21.1
#    Extract it, then copy src/ and build.gradle from this repo into it.

# 2. Build
./gradlew build

# Output: build/libs/mc-recipe-discovery-1.0.0.jar
```

Then drop the jar into your mods/ folder.

## Structures covered

### Vanilla (38 loot tables)
Dungeon, Mineshaft, Stronghold (3 rooms), 8× Village professions, Desert
Pyramid, Jungle Temple, Shipwreck (3 chests), Underwater Ruin (big + small),
Igloo, Pillager Outpost, Woodland Mansion, Ruined Portal, Nether Fortress,
Bastion (4 variants), End City, Ancient City, Trail Ruins, Trial Chambers (5)

### Dungeons and Taverns (21 loot tables)
Activates automatically if D&T is installed. No configuration needed.

Tavern, Firewatch Tower, Conduit Ruins, Mangrove Witch Hut, Ruin Town,
Underground House, Badlands Miner Outpost, Illager Hideout (+vegitarian),
Illager Camp, Lost Bunker, Desert Ruins, Jungle Ruins, Swamp Village,
Lone Citadel, Nether Keep, Stray Fort, Creeping Crypt, Nether Skeleton Camp,
Piglin Outstation, End Castle

## Project structure

```
src/main/
├── java/com/mc_recipe_discovery/
│   ├── RecipeDiscovery.java          ← Mod entry point
│   └── loot/
│       ├── ModLootModifiers.java     ← Registers the GLM codec
│       └── RecipeBookLootModifier.java ← Core logic
└── resources/
    ├── META-INF/mods.toml
    ├── pack.mcmeta
    └── data/
        ├── forge/loot_modifiers/
        │   └── global_loot_modifiers.json   ← lists all 59 modifiers
        └── mc_recipe_discovery/loot_modifiers/
            └── *.json                       ← one file per structure (59 total)
```

## Adding more structures

1. Open `generate_data.py`
2. Add an entry to the `TABLES` dict:
   ```python
   "yourmod:chests/your_structure": [
       ["minecraft:iron_sword", "minecraft:iron_axe"],
       ["minecraft:diamond_sword"],
   ]
   ```
3. Run `python3 generate_data.py` to regenerate the JSON files
4. Rebuild the mod

## License

MIT
