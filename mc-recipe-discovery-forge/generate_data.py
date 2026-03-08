#!/usr/bin/env python3
"""
Generates all Global Loot Modifier JSON files for the Forge mod.
Run this script to regenerate the JSON data files.
"""

import json
import os

MODID = "mc_recipe_discovery"
OUT = "src/main/resources/data"

# ─────────────────────────────────────────────────────────────
# RECIPE GROUPS  (identical logic to the datapack, but now
#                 expressed as GLM JSON files instead)
# ─────────────────────────────────────────────────────────────

# Format: "namespace:chest_path" -> [ [recipe, ...], [recipe, ...], ... ]
TABLES = {

    # ── VANILLA ───────────────────────────────────────────────

    "minecraft:chests/simple_dungeon": [
        ["minecraft:crafting_table", "minecraft:chest", "minecraft:furnace",
         "minecraft:stick", "minecraft:torch"],
        ["minecraft:wooden_pickaxe", "minecraft:wooden_axe",
         "minecraft:wooden_shovel", "minecraft:wooden_sword", "minecraft:wooden_hoe"],
        ["minecraft:stone_pickaxe", "minecraft:stone_axe",
         "minecraft:stone_shovel", "minecraft:stone_sword", "minecraft:stone_hoe"],
        ["minecraft:bow", "minecraft:arrow", "minecraft:fishing_rod"],
        ["minecraft:ladder", "minecraft:scaffolding",
         "minecraft:lantern", "minecraft:soul_lantern"],
        ["minecraft:bread", "minecraft:bowl",
         "minecraft:mushroom_stew", "minecraft:pumpkin_pie"],
    ],

    "minecraft:chests/abandoned_mineshaft": [
        ["minecraft:oak_planks", "minecraft:spruce_planks", "minecraft:birch_planks",
         "minecraft:jungle_planks", "minecraft:acacia_planks", "minecraft:dark_oak_planks",
         "minecraft:mangrove_planks", "minecraft:cherry_planks", "minecraft:bamboo_planks",
         "minecraft:crimson_planks", "minecraft:warped_planks"],
        ["minecraft:oak_slab", "minecraft:spruce_slab", "minecraft:birch_slab",
         "minecraft:jungle_slab", "minecraft:acacia_slab", "minecraft:dark_oak_slab",
         "minecraft:mangrove_slab", "minecraft:cherry_slab"],
        ["minecraft:oak_stairs", "minecraft:spruce_stairs", "minecraft:birch_stairs",
         "minecraft:jungle_stairs", "minecraft:acacia_stairs", "minecraft:dark_oak_stairs",
         "minecraft:mangrove_stairs", "minecraft:cherry_stairs"],
        ["minecraft:oak_door", "minecraft:spruce_door", "minecraft:birch_door",
         "minecraft:jungle_door", "minecraft:acacia_door", "minecraft:dark_oak_door",
         "minecraft:mangrove_door", "minecraft:cherry_door",
         "minecraft:crimson_door", "minecraft:warped_door"],
        ["minecraft:oak_fence", "minecraft:spruce_fence", "minecraft:birch_fence",
         "minecraft:jungle_fence", "minecraft:acacia_fence", "minecraft:dark_oak_fence",
         "minecraft:oak_fence_gate", "minecraft:spruce_fence_gate", "minecraft:birch_fence_gate",
         "minecraft:jungle_fence_gate", "minecraft:acacia_fence_gate"],
        ["minecraft:rail", "minecraft:powered_rail", "minecraft:detector_rail",
         "minecraft:activator_rail", "minecraft:minecart",
         "minecraft:chest_minecart", "minecraft:hopper_minecart"],
        ["minecraft:piston", "minecraft:sticky_piston", "minecraft:observer"],
        ["minecraft:oak_sign", "minecraft:spruce_sign", "minecraft:birch_sign",
         "minecraft:jungle_sign", "minecraft:acacia_sign", "minecraft:dark_oak_sign"],
    ],

    "minecraft:chests/stronghold_library": [
        ["minecraft:enchanting_table", "minecraft:bookshelf", "minecraft:book",
         "minecraft:lectern", "minecraft:chiseled_bookshelf"],
        ["minecraft:ender_chest", "minecraft:eye_of_ender"],
    ],
    "minecraft:chests/stronghold_corridor": [
        ["minecraft:iron_pickaxe", "minecraft:iron_axe",
         "minecraft:iron_shovel", "minecraft:iron_sword", "minecraft:iron_hoe"],
        ["minecraft:iron_helmet", "minecraft:iron_chestplate",
         "minecraft:iron_leggings", "minecraft:iron_boots"],
    ],
    "minecraft:chests/stronghold_crossing": [
        ["minecraft:compass", "minecraft:clock", "minecraft:spyglass"],
        ["minecraft:hopper", "minecraft:dropper", "minecraft:dispenser"],
        ["minecraft:golden_apple"],
    ],

    "minecraft:chests/village/village_weaponsmith": [
        ["minecraft:iron_sword", "minecraft:golden_sword", "minecraft:diamond_sword"],
        ["minecraft:iron_axe", "minecraft:golden_axe", "minecraft:diamond_axe"],
        ["minecraft:shield", "minecraft:flint_and_steel", "minecraft:shears"],
    ],
    "minecraft:chests/village/village_toolsmith": [
        ["minecraft:iron_pickaxe", "minecraft:iron_shovel",
         "minecraft:iron_hoe", "minecraft:golden_pickaxe", "minecraft:golden_shovel"],
        ["minecraft:diamond_pickaxe", "minecraft:diamond_shovel",
         "minecraft:diamond_hoe", "minecraft:diamond_axe"],
        ["minecraft:smithing_table", "minecraft:grindstone",
         "minecraft:anvil", "minecraft:spyglass"],
    ],
    "minecraft:chests/village/village_armorer": [
        ["minecraft:iron_helmet", "minecraft:iron_chestplate",
         "minecraft:iron_leggings", "minecraft:iron_boots"],
        ["minecraft:golden_helmet", "minecraft:golden_chestplate",
         "minecraft:golden_leggings", "minecraft:golden_boots"],
        ["minecraft:diamond_helmet", "minecraft:diamond_chestplate",
         "minecraft:diamond_leggings", "minecraft:diamond_boots"],
        ["minecraft:blast_furnace", "minecraft:iron_block",
         "minecraft:gold_block", "minecraft:diamond_block"],
    ],
    "minecraft:chests/village/village_cartographer": [
        ["minecraft:compass", "minecraft:clock", "minecraft:map"],
        ["minecraft:item_frame", "minecraft:glow_item_frame",
         "minecraft:painting", "minecraft:armor_stand"],
        ["minecraft:cartography_table"],
    ],
    "minecraft:chests/village/village_fletcher": [
        ["minecraft:bow", "minecraft:crossbow",
         "minecraft:arrow", "minecraft:spectral_arrow"],
        ["minecraft:fletching_table"],
    ],
    "minecraft:chests/village/village_mason": [
        ["minecraft:stonecutter",
         "minecraft:stone_bricks", "minecraft:stone_brick_slab",
         "minecraft:stone_brick_stairs", "minecraft:stone_brick_wall"],
        ["minecraft:polished_andesite", "minecraft:polished_diorite",
         "minecraft:polished_granite", "minecraft:polished_andesite_slab",
         "minecraft:polished_diorite_slab", "minecraft:polished_granite_slab",
         "minecraft:polished_andesite_stairs", "minecraft:polished_diorite_stairs",
         "minecraft:polished_granite_stairs"],
        ["minecraft:smooth_stone", "minecraft:smooth_stone_slab",
         "minecraft:cut_sandstone", "minecraft:chiseled_sandstone",
         "minecraft:chiseled_stone_bricks", "minecraft:mossy_stone_bricks",
         "minecraft:mossy_cobblestone", "minecraft:cracked_stone_bricks"],
        ["minecraft:bricks", "minecraft:brick_slab",
         "minecraft:brick_stairs", "minecraft:brick_wall"],
        ["minecraft:sandstone", "minecraft:sandstone_slab",
         "minecraft:sandstone_stairs", "minecraft:sandstone_wall",
         "minecraft:red_sandstone", "minecraft:red_sandstone_slab",
         "minecraft:red_sandstone_stairs", "minecraft:red_sandstone_wall"],
        ["minecraft:tuff_bricks", "minecraft:polished_tuff", "minecraft:chiseled_tuff",
         "minecraft:tuff_brick_slab", "minecraft:tuff_brick_stairs", "minecraft:tuff_brick_wall",
         "minecraft:polished_tuff_slab", "minecraft:polished_tuff_stairs",
         "minecraft:polished_tuff_wall"],
        ["minecraft:mud_bricks", "minecraft:mud_brick_slab",
         "minecraft:mud_brick_stairs", "minecraft:mud_brick_wall"],
    ],
    "minecraft:chests/village/village_shepherd": [
        ["minecraft:white_bed", "minecraft:orange_bed", "minecraft:magenta_bed",
         "minecraft:light_blue_bed", "minecraft:yellow_bed", "minecraft:lime_bed",
         "minecraft:pink_bed", "minecraft:gray_bed"],
        ["minecraft:cyan_bed", "minecraft:purple_bed", "minecraft:blue_bed",
         "minecraft:brown_bed", "minecraft:green_bed", "minecraft:red_bed",
         "minecraft:black_bed", "minecraft:light_gray_bed"],
        ["minecraft:white_carpet", "minecraft:orange_carpet", "minecraft:magenta_carpet",
         "minecraft:light_blue_carpet", "minecraft:yellow_carpet", "minecraft:lime_carpet",
         "minecraft:pink_carpet", "minecraft:gray_carpet"],
        ["minecraft:cyan_carpet", "minecraft:purple_carpet", "minecraft:blue_carpet",
         "minecraft:brown_carpet", "minecraft:green_carpet", "minecraft:red_carpet",
         "minecraft:black_carpet", "minecraft:light_gray_carpet"],
        ["minecraft:white_banner", "minecraft:orange_banner", "minecraft:magenta_banner",
         "minecraft:light_blue_banner", "minecraft:yellow_banner", "minecraft:lime_banner",
         "minecraft:pink_banner", "minecraft:gray_banner"],
        ["minecraft:cyan_banner", "minecraft:purple_banner", "minecraft:blue_banner",
         "minecraft:brown_banner", "minecraft:green_banner", "minecraft:red_banner",
         "minecraft:black_banner", "minecraft:light_gray_banner"],
        ["minecraft:loom"],
    ],
    "minecraft:chests/village/village_tannery": [
        ["minecraft:leather_helmet", "minecraft:leather_chestplate",
         "minecraft:leather_leggings", "minecraft:leather_boots"],
        ["minecraft:book", "minecraft:bookshelf",
         "minecraft:lectern", "minecraft:chiseled_bookshelf"],
    ],
    "minecraft:chests/village/village_temple": [
        ["minecraft:brewing_stand", "minecraft:cauldron", "minecraft:flower_pot"],
        ["minecraft:fermented_spider_eye", "minecraft:magma_cream",
         "minecraft:blaze_powder", "minecraft:eye_of_ender"],
        ["minecraft:white_candle", "minecraft:orange_candle", "minecraft:magenta_candle",
         "minecraft:light_blue_candle", "minecraft:yellow_candle", "minecraft:lime_candle",
         "minecraft:pink_candle", "minecraft:gray_candle", "minecraft:candle"],
        ["minecraft:cyan_candle", "minecraft:purple_candle", "minecraft:blue_candle",
         "minecraft:brown_candle", "minecraft:green_candle", "minecraft:red_candle",
         "minecraft:black_candle", "minecraft:light_gray_candle"],
    ],

    "minecraft:chests/desert_pyramid": [
        ["minecraft:tnt", "minecraft:fire_charge", "minecraft:flint_and_steel"],
        ["minecraft:glass", "minecraft:glass_pane",
         "minecraft:white_stained_glass", "minecraft:orange_stained_glass",
         "minecraft:magenta_stained_glass", "minecraft:light_blue_stained_glass",
         "minecraft:yellow_stained_glass", "minecraft:lime_stained_glass"],
        ["minecraft:pink_stained_glass", "minecraft:gray_stained_glass",
         "minecraft:cyan_stained_glass", "minecraft:purple_stained_glass",
         "minecraft:blue_stained_glass", "minecraft:brown_stained_glass",
         "minecraft:green_stained_glass", "minecraft:red_stained_glass",
         "minecraft:black_stained_glass", "minecraft:light_gray_stained_glass"],
        ["minecraft:white_concrete_powder", "minecraft:orange_concrete_powder",
         "minecraft:magenta_concrete_powder", "minecraft:light_blue_concrete_powder",
         "minecraft:yellow_concrete_powder", "minecraft:lime_concrete_powder",
         "minecraft:pink_concrete_powder", "minecraft:gray_concrete_powder"],
        ["minecraft:cyan_concrete_powder", "minecraft:purple_concrete_powder",
         "minecraft:blue_concrete_powder", "minecraft:brown_concrete_powder",
         "minecraft:green_concrete_powder", "minecraft:red_concrete_powder",
         "minecraft:black_concrete_powder", "minecraft:light_gray_concrete_powder"],
        ["minecraft:white_terracotta", "minecraft:orange_terracotta",
         "minecraft:yellow_terracotta", "minecraft:red_terracotta",
         "minecraft:brown_terracotta", "minecraft:gray_terracotta"],
    ],

    "minecraft:chests/jungle_temple": [
        ["minecraft:piston", "minecraft:sticky_piston",
         "minecraft:dispenser", "minecraft:dropper", "minecraft:observer"],
        ["minecraft:hopper", "minecraft:comparator",
         "minecraft:repeater", "minecraft:daylight_detector", "minecraft:target"],
        ["minecraft:tripwire_hook", "minecraft:redstone_torch",
         "minecraft:redstone_lamp"],
        ["minecraft:note_block", "minecraft:jukebox"],
    ],

    "minecraft:chests/shipwreck_supply": [
        ["minecraft:oak_boat", "minecraft:spruce_boat", "minecraft:birch_boat",
         "minecraft:jungle_boat", "minecraft:acacia_boat", "minecraft:dark_oak_boat",
         "minecraft:mangrove_boat", "minecraft:cherry_boat", "minecraft:bamboo_raft"],
        ["minecraft:oak_chest_boat", "minecraft:spruce_chest_boat",
         "minecraft:birch_chest_boat", "minecraft:jungle_chest_boat"],
        ["minecraft:bucket", "minecraft:fishing_rod",
         "minecraft:carrot_on_a_stick", "minecraft:warped_fungus_on_a_stick"],
    ],
    "minecraft:chests/shipwreck_map": [
        ["minecraft:compass", "minecraft:map", "minecraft:item_frame", "minecraft:clock"],
        ["minecraft:spyglass", "minecraft:glow_item_frame"],
    ],
    "minecraft:chests/shipwreck_treasure": [
        ["minecraft:conduit"],
    ],

    "minecraft:chests/underwater_ruin_big": [
        ["minecraft:prismarine", "minecraft:prismarine_bricks", "minecraft:dark_prismarine"],
        ["minecraft:prismarine_slab", "minecraft:prismarine_brick_slab",
         "minecraft:dark_prismarine_slab", "minecraft:prismarine_stairs",
         "minecraft:prismarine_brick_stairs", "minecraft:dark_prismarine_stairs",
         "minecraft:prismarine_wall", "minecraft:sea_lantern"],
    ],
    "minecraft:chests/underwater_ruin_small": [
        ["minecraft:prismarine", "minecraft:sea_lantern", "minecraft:conduit"],
    ],

    "minecraft:chests/igloo_chest": [
        ["minecraft:packed_ice", "minecraft:blue_ice", "minecraft:snow_block"],
        ["minecraft:campfire", "minecraft:soul_campfire",
         "minecraft:smoker", "minecraft:blast_furnace"],
        ["minecraft:soul_torch", "minecraft:soul_lantern"],
    ],

    "minecraft:chests/pillager_outpost": [
        ["minecraft:crossbow", "minecraft:shield"],
        ["minecraft:target", "minecraft:tripwire_hook", "minecraft:redstone_lamp"],
    ],

    "minecraft:chests/woodland_mansion": [
        ["minecraft:enchanting_table", "minecraft:chiseled_bookshelf",
         "minecraft:bookshelf", "minecraft:lectern"],
        ["minecraft:diamond_sword", "minecraft:diamond_pickaxe",
         "minecraft:diamond_helmet", "minecraft:diamond_chestplate",
         "minecraft:diamond_leggings", "minecraft:diamond_boots"],
        ["minecraft:golden_apple", "minecraft:golden_carrot"],
        ["minecraft:note_block", "minecraft:jukebox", "minecraft:painting"],
    ],

    "minecraft:chests/ruined_portal": [
        ["minecraft:golden_helmet", "minecraft:golden_chestplate",
         "minecraft:golden_leggings", "minecraft:golden_boots"],
        ["minecraft:golden_sword", "minecraft:golden_pickaxe",
         "minecraft:golden_axe", "minecraft:golden_shovel", "minecraft:golden_hoe"],
        ["minecraft:golden_apple", "minecraft:golden_carrot", "minecraft:fire_charge"],
    ],

    "minecraft:chests/nether_bridge": [
        ["minecraft:nether_brick", "minecraft:nether_brick_slab",
         "minecraft:nether_brick_stairs", "minecraft:nether_brick_wall",
         "minecraft:nether_brick_fence"],
        ["minecraft:red_nether_bricks", "minecraft:red_nether_brick_slab",
         "minecraft:red_nether_brick_stairs", "minecraft:red_nether_brick_wall"],
        ["minecraft:blaze_powder", "minecraft:magma_cream",
         "minecraft:fire_charge", "minecraft:brewing_stand"],
        ["minecraft:magma_block"],
    ],

    "minecraft:chests/bastion_treasure": [
        ["minecraft:netherite_sword", "minecraft:netherite_pickaxe",
         "minecraft:netherite_axe", "minecraft:netherite_shovel", "minecraft:netherite_hoe"],
        ["minecraft:netherite_helmet", "minecraft:netherite_chestplate",
         "minecraft:netherite_leggings", "minecraft:netherite_boots"],
        ["minecraft:netherite_block", "minecraft:gold_block",
         "minecraft:lodestone", "minecraft:netherite_ingot"],
        ["minecraft:respawn_anchor"],
        ["minecraft:polished_blackstone", "minecraft:polished_blackstone_bricks",
         "minecraft:chiseled_polished_blackstone",
         "minecraft:polished_blackstone_brick_slab", "minecraft:polished_blackstone_brick_stairs",
         "minecraft:polished_blackstone_brick_wall",
         "minecraft:blackstone_slab", "minecraft:blackstone_stairs", "minecraft:blackstone_wall"],
        ["minecraft:polished_blackstone_slab", "minecraft:polished_blackstone_stairs",
         "minecraft:polished_blackstone_wall", "minecraft:polished_blackstone_pressure_plate",
         "minecraft:polished_blackstone_button"],
    ],
    "minecraft:chests/bastion_other": [
        ["minecraft:golden_helmet", "minecraft:golden_chestplate",
         "minecraft:golden_leggings", "minecraft:golden_boots"],
        ["minecraft:golden_sword", "minecraft:golden_pickaxe", "minecraft:golden_axe"],
    ],
    "minecraft:chests/bastion_hoglin_stable": [
        ["minecraft:gold_block", "minecraft:golden_apple", "minecraft:golden_carrot"],
    ],
    "minecraft:chests/bastion_bridge": [
        ["minecraft:lodestone", "minecraft:respawn_anchor", "minecraft:crying_obsidian"],
    ],

    "minecraft:chests/end_city_treasure": [
        ["minecraft:end_crystal",
         "minecraft:end_stone_bricks", "minecraft:end_stone_brick_slab",
         "minecraft:end_stone_brick_stairs", "minecraft:end_stone_brick_wall"],
        ["minecraft:purpur_block", "minecraft:purpur_slab",
         "minecraft:purpur_stairs", "minecraft:purpur_pillar"],
        ["minecraft:popped_chorus_fruit"],
        ["minecraft:diamond_sword", "minecraft:diamond_pickaxe",
         "minecraft:diamond_axe", "minecraft:diamond_helmet",
         "minecraft:diamond_chestplate", "minecraft:diamond_leggings",
         "minecraft:diamond_boots"],
    ],

    "minecraft:chests/ancient_city": [
        ["minecraft:calibrated_sculk_sensor"],
        ["minecraft:recovery_compass"],
        ["minecraft:diamond_hoe", "minecraft:diamond_sword", "minecraft:enchanting_table"],
    ],

    "minecraft:chests/trail_ruins_archaeology_rare": [
        ["minecraft:tuff_bricks", "minecraft:tuff_brick_slab",
         "minecraft:tuff_brick_stairs", "minecraft:tuff_brick_wall",
         "minecraft:chiseled_tuff", "minecraft:polished_tuff",
         "minecraft:polished_tuff_slab", "minecraft:polished_tuff_stairs",
         "minecraft:polished_tuff_wall"],
    ],

    "minecraft:chests/trial_chambers/reward": [
        ["minecraft:mace"],
        ["minecraft:copper_block", "minecraft:cut_copper",
         "minecraft:cut_copper_slab", "minecraft:cut_copper_stairs",
         "minecraft:chiseled_copper", "minecraft:copper_grate",
         "minecraft:copper_bulb", "minecraft:copper_door", "minecraft:copper_trapdoor"],
        ["minecraft:exposed_cut_copper", "minecraft:weathered_cut_copper",
         "minecraft:oxidized_cut_copper",
         "minecraft:exposed_chiseled_copper", "minecraft:weathered_chiseled_copper",
         "minecraft:oxidized_chiseled_copper"],
        ["minecraft:waxed_copper_block", "minecraft:waxed_cut_copper",
         "minecraft:waxed_cut_copper_slab", "minecraft:waxed_cut_copper_stairs",
         "minecraft:waxed_chiseled_copper", "minecraft:waxed_copper_grate",
         "minecraft:waxed_copper_bulb", "minecraft:waxed_copper_door",
         "minecraft:waxed_copper_trapdoor"],
        ["minecraft:waxed_exposed_cut_copper", "minecraft:waxed_weathered_cut_copper",
         "minecraft:waxed_oxidized_cut_copper",
         "minecraft:waxed_exposed_copper_bulb", "minecraft:waxed_weathered_copper_bulb",
         "minecraft:waxed_oxidized_copper_bulb"],
    ],
    "minecraft:chests/trial_chambers/supply": [
        ["minecraft:tuff_bricks", "minecraft:polished_tuff",
         "minecraft:chiseled_tuff", "minecraft:tuff_brick_slab",
         "minecraft:tuff_brick_stairs"],
        ["minecraft:iron_pickaxe", "minecraft:iron_sword",
         "minecraft:iron_helmet", "minecraft:iron_chestplate"],
    ],
    "minecraft:chests/trial_chambers/entrance": [
        ["minecraft:tuff_brick_slab", "minecraft:tuff_brick_stairs",
         "minecraft:tuff_brick_wall", "minecraft:polished_tuff_slab",
         "minecraft:polished_tuff_stairs"],
    ],
    "minecraft:chests/trial_chambers/corridor": [
        ["minecraft:cut_copper", "minecraft:waxed_cut_copper", "minecraft:copper_grate"],
    ],
    "minecraft:chests/trial_chambers/intersection": [
        ["minecraft:copper_bulb", "minecraft:waxed_copper_bulb"],
    ],

    # ── DUNGEONS AND TAVERNS (nova_structures) ────────────────
    # If D&T is not installed, these conditions will never be met
    # → zero impact. If D&T IS installed, the modifier activates
    # automatically — no load order required!

    "nova_structures:chests/tavern": [
        ["minecraft:barrel", "minecraft:smoker", "minecraft:blast_furnace",
         "minecraft:campfire", "minecraft:soul_campfire"],
        ["minecraft:crafting_table", "minecraft:chest", "minecraft:furnace",
         "minecraft:trapped_chest"],
        ["minecraft:bread", "minecraft:cake", "minecraft:cookie",
         "minecraft:pumpkin_pie", "minecraft:bowl", "minecraft:mushroom_stew"],
        ["minecraft:oak_trapdoor", "minecraft:spruce_trapdoor",
         "minecraft:birch_trapdoor", "minecraft:jungle_trapdoor",
         "minecraft:acacia_trapdoor", "minecraft:dark_oak_trapdoor"],
        ["minecraft:oak_button", "minecraft:spruce_button", "minecraft:birch_button",
         "minecraft:stone_button", "minecraft:polished_blackstone_button"],
        ["minecraft:oak_pressure_plate", "minecraft:spruce_pressure_plate",
         "minecraft:stone_pressure_plate", "minecraft:polished_blackstone_pressure_plate",
         "minecraft:heavy_weighted_pressure_plate", "minecraft:light_weighted_pressure_plate"],
    ],

    "nova_structures:chests/firewatch_tower": [
        ["minecraft:spyglass", "minecraft:compass", "minecraft:clock"],
        ["minecraft:torch", "minecraft:lantern", "minecraft:soul_torch",
         "minecraft:soul_lantern", "minecraft:campfire"],
        ["minecraft:ladder", "minecraft:scaffolding"],
        ["minecraft:dark_oak_planks", "minecraft:dark_oak_slab",
         "minecraft:dark_oak_stairs", "minecraft:dark_oak_door",
         "minecraft:dark_oak_fence", "minecraft:dark_oak_fence_gate"],
    ],

    "nova_structures:chests/conduit_ruins": [
        ["minecraft:conduit"],
        ["minecraft:prismarine", "minecraft:prismarine_bricks",
         "minecraft:dark_prismarine", "minecraft:sea_lantern"],
        ["minecraft:prismarine_slab", "minecraft:prismarine_brick_slab",
         "minecraft:dark_prismarine_slab", "minecraft:prismarine_stairs",
         "minecraft:prismarine_brick_stairs", "minecraft:dark_prismarine_stairs",
         "minecraft:prismarine_wall"],
    ],

    "nova_structures:chests/mangrove_witch_hut": [
        ["minecraft:brewing_stand", "minecraft:cauldron"],
        ["minecraft:fermented_spider_eye", "minecraft:magma_cream",
         "minecraft:blaze_powder", "minecraft:eye_of_ender"],
        ["minecraft:flower_pot",
         "minecraft:white_candle", "minecraft:orange_candle",
         "minecraft:magenta_candle", "minecraft:purple_candle",
         "minecraft:cyan_candle", "minecraft:blue_candle"],
        ["minecraft:mangrove_planks", "minecraft:mangrove_slab",
         "minecraft:mangrove_stairs", "minecraft:mangrove_door",
         "minecraft:mangrove_fence", "minecraft:mangrove_fence_gate"],
    ],

    "nova_structures:chests/ruin_town": [
        ["minecraft:cobblestone_slab", "minecraft:cobblestone_stairs",
         "minecraft:cobblestone_wall"],
        ["minecraft:mossy_cobblestone", "minecraft:mossy_cobblestone_wall",
         "minecraft:mossy_cobblestone_stairs", "minecraft:mossy_cobblestone_slab",
         "minecraft:mossy_stone_bricks", "minecraft:mossy_stone_brick_wall",
         "minecraft:mossy_stone_brick_stairs", "minecraft:mossy_stone_brick_slab"],
        ["minecraft:chiseled_stone_bricks", "minecraft:cracked_stone_bricks",
         "minecraft:stone_brick_wall"],
        ["minecraft:iron_door", "minecraft:iron_trapdoor",
         "minecraft:iron_bars", "minecraft:heavy_weighted_pressure_plate"],
    ],

    "nova_structures:chests/underground_house": [
        ["minecraft:chest", "minecraft:trapped_chest", "minecraft:barrel"],
        ["minecraft:white_shulker_box", "minecraft:orange_shulker_box",
         "minecraft:magenta_shulker_box", "minecraft:light_blue_shulker_box",
         "minecraft:yellow_shulker_box", "minecraft:lime_shulker_box",
         "minecraft:pink_shulker_box", "minecraft:gray_shulker_box"],
        ["minecraft:cyan_shulker_box", "minecraft:purple_shulker_box",
         "minecraft:blue_shulker_box", "minecraft:brown_shulker_box",
         "minecraft:green_shulker_box", "minecraft:red_shulker_box",
         "minecraft:black_shulker_box", "minecraft:light_gray_shulker_box"],
        ["minecraft:crafting_table", "minecraft:furnace",
         "minecraft:smoker", "minecraft:blast_furnace"],
    ],

    "nova_structures:chests/badlands_miner_outpost": [
        ["minecraft:iron_pickaxe", "minecraft:iron_shovel",
         "minecraft:iron_axe", "minecraft:iron_sword"],
        ["minecraft:diamond_pickaxe", "minecraft:diamond_shovel",
         "minecraft:diamond_axe"],
        ["minecraft:blast_furnace", "minecraft:smoker",
         "minecraft:anvil", "minecraft:smithing_table", "minecraft:grindstone"],
        ["minecraft:iron_block", "minecraft:gold_block",
         "minecraft:redstone_block", "minecraft:lapis_block",
         "minecraft:coal_block", "minecraft:copper_block",
         "minecraft:raw_iron_block", "minecraft:raw_gold_block",
         "minecraft:raw_copper_block"],
        ["minecraft:powered_rail", "minecraft:rail",
         "minecraft:detector_rail", "minecraft:activator_rail",
         "minecraft:minecart", "minecraft:chest_minecart",
         "minecraft:hopper_minecart", "minecraft:tnt_minecart"],
    ],

    "nova_structures:chests/illager_hideout": [
        ["minecraft:crossbow", "minecraft:bow", "minecraft:shield"],
        ["minecraft:iron_helmet", "minecraft:iron_chestplate",
         "minecraft:iron_leggings", "minecraft:iron_boots"],
        ["minecraft:chainmail_helmet", "minecraft:chainmail_chestplate",
         "minecraft:chainmail_leggings", "minecraft:chainmail_boots"],
        ["minecraft:diamond_sword", "minecraft:diamond_axe",
         "minecraft:diamond_helmet", "minecraft:diamond_chestplate",
         "minecraft:diamond_leggings", "minecraft:diamond_boots"],
        ["minecraft:tnt", "minecraft:dispenser", "minecraft:observer",
         "minecraft:piston", "minecraft:sticky_piston"],
        ["minecraft:enchanting_table", "minecraft:anvil",
         "minecraft:grindstone", "minecraft:smithing_table"],
    ],

    "nova_structures:chests/illager_hideout_vegitarian": [
        ["minecraft:composter", "minecraft:barrel",
         "minecraft:flower_pot", "minecraft:bowl"],
        ["minecraft:bread", "minecraft:pumpkin_pie",
         "minecraft:cake", "minecraft:cookie", "minecraft:dried_kelp_block"],
        ["minecraft:hay_block", "minecraft:melon", "minecraft:melon_slice"],
    ],

    "nova_structures:chests/illager_camp": [
        ["minecraft:crossbow", "minecraft:bow", "minecraft:arrow"],
        ["minecraft:leather_helmet", "minecraft:leather_chestplate",
         "minecraft:leather_leggings", "minecraft:leather_boots"],
        ["minecraft:dark_oak_fence", "minecraft:dark_oak_fence_gate",
         "minecraft:dark_oak_planks", "minecraft:dark_oak_slab",
         "minecraft:dark_oak_stairs"],
    ],

    "nova_structures:chests/lost_bunker": [
        ["minecraft:iron_door", "minecraft:iron_trapdoor",
         "minecraft:iron_bars", "minecraft:iron_block"],
        ["minecraft:piston", "minecraft:sticky_piston",
         "minecraft:dispenser", "minecraft:dropper",
         "minecraft:hopper", "minecraft:observer"],
        ["minecraft:repeater", "minecraft:comparator",
         "minecraft:redstone_torch", "minecraft:redstone_lamp",
         "minecraft:daylight_detector", "minecraft:target"],
        ["minecraft:tnt", "minecraft:fire_charge", "minecraft:flint_and_steel"],
    ],

    "nova_structures:chests/desert_ruins": [
        ["minecraft:sandstone", "minecraft:sandstone_slab",
         "minecraft:sandstone_stairs", "minecraft:sandstone_wall",
         "minecraft:cut_sandstone", "minecraft:chiseled_sandstone",
         "minecraft:smooth_sandstone", "minecraft:smooth_sandstone_slab",
         "minecraft:smooth_sandstone_stairs"],
        ["minecraft:red_sandstone", "minecraft:red_sandstone_slab",
         "minecraft:red_sandstone_stairs", "minecraft:red_sandstone_wall",
         "minecraft:cut_red_sandstone", "minecraft:chiseled_red_sandstone",
         "minecraft:smooth_red_sandstone", "minecraft:smooth_red_sandstone_slab",
         "minecraft:smooth_red_sandstone_stairs"],
        ["minecraft:tnt", "minecraft:fire_charge",
         "minecraft:white_terracotta", "minecraft:orange_terracotta",
         "minecraft:yellow_terracotta", "minecraft:red_terracotta",
         "minecraft:brown_terracotta", "minecraft:gray_terracotta"],
    ],

    "nova_structures:chests/jungle_ruins": [
        ["minecraft:jungle_planks", "minecraft:jungle_slab",
         "minecraft:jungle_stairs", "minecraft:jungle_door",
         "minecraft:jungle_fence", "minecraft:jungle_fence_gate"],
        ["minecraft:mossy_cobblestone", "minecraft:mossy_stone_bricks",
         "minecraft:chiseled_stone_bricks", "minecraft:cracked_stone_bricks"],
        ["minecraft:piston", "minecraft:sticky_piston",
         "minecraft:dispenser", "minecraft:tripwire_hook"],
        ["minecraft:bow", "minecraft:arrow", "minecraft:bamboo_planks",
         "minecraft:bamboo_slab", "minecraft:bamboo_stairs",
         "minecraft:bamboo_door", "minecraft:bamboo_raft"],
    ],

    "nova_structures:chests/swamp_village": [
        ["minecraft:brewing_stand", "minecraft:cauldron",
         "minecraft:flower_pot", "minecraft:composter"],
        ["minecraft:oak_boat", "minecraft:spruce_boat",
         "minecraft:oak_chest_boat", "minecraft:spruce_chest_boat",
         "minecraft:fishing_rod", "minecraft:bucket"],
        ["minecraft:slime_block"],
        ["minecraft:oak_planks", "minecraft:oak_slab", "minecraft:oak_stairs",
         "minecraft:oak_door", "minecraft:oak_fence", "minecraft:oak_fence_gate"],
    ],

    "nova_structures:chests/lone_citadel": [
        ["minecraft:diamond_sword", "minecraft:diamond_pickaxe",
         "minecraft:diamond_axe", "minecraft:diamond_shovel",
         "minecraft:diamond_hoe"],
        ["minecraft:diamond_helmet", "minecraft:diamond_chestplate",
         "minecraft:diamond_leggings", "minecraft:diamond_boots"],
        ["minecraft:enchanting_table", "minecraft:anvil",
         "minecraft:smithing_table", "minecraft:grindstone"],
        ["minecraft:netherite_sword", "minecraft:netherite_pickaxe",
         "minecraft:netherite_axe"],
        ["minecraft:netherite_helmet", "minecraft:netherite_chestplate",
         "minecraft:netherite_leggings", "minecraft:netherite_boots"],
        ["minecraft:netherite_block", "minecraft:lodestone"],
    ],

    "nova_structures:chests/nether_keep": [
        ["minecraft:nether_brick", "minecraft:nether_brick_slab",
         "minecraft:nether_brick_stairs", "minecraft:nether_brick_wall",
         "minecraft:nether_brick_fence"],
        ["minecraft:red_nether_bricks", "minecraft:red_nether_brick_slab",
         "minecraft:red_nether_brick_stairs", "minecraft:red_nether_brick_wall"],
        ["minecraft:blaze_powder", "minecraft:magma_cream",
         "minecraft:brewing_stand", "minecraft:magma_block"],
        ["minecraft:golden_helmet", "minecraft:golden_chestplate",
         "minecraft:golden_leggings", "minecraft:golden_boots"],
        ["minecraft:netherite_sword", "minecraft:netherite_axe",
         "minecraft:netherite_pickaxe", "minecraft:netherite_hoe"],
        ["minecraft:respawn_anchor", "minecraft:crying_obsidian"],
    ],

    "nova_structures:chests/stray_fort": [
        ["minecraft:packed_ice", "minecraft:blue_ice", "minecraft:snow_block"],
        ["minecraft:soul_torch", "minecraft:soul_lantern", "minecraft:soul_campfire"],
        ["minecraft:chainmail_helmet", "minecraft:chainmail_chestplate",
         "minecraft:chainmail_leggings", "minecraft:chainmail_boots"],
    ],

    "nova_structures:chests/creeping_crypt": [
        ["minecraft:tnt", "minecraft:dispenser",
         "minecraft:piston", "minecraft:sticky_piston"],
        ["minecraft:stone_bricks", "minecraft:mossy_stone_bricks",
         "minecraft:cracked_stone_bricks", "minecraft:chiseled_stone_bricks",
         "minecraft:stone_brick_slab", "minecraft:stone_brick_stairs",
         "minecraft:stone_brick_wall"],
    ],

    "nova_structures:chests/nether_skeleton_camp": [
        ["minecraft:bone_block", "minecraft:soul_sand", "minecraft:soul_soil"],
        ["minecraft:nether_brick", "minecraft:nether_brick_fence",
         "minecraft:nether_brick_slab"],
    ],

    "nova_structures:chests/piglin_outstation": [
        ["minecraft:golden_helmet", "minecraft:golden_chestplate",
         "minecraft:golden_leggings", "minecraft:golden_boots"],
        ["minecraft:golden_sword", "minecraft:golden_pickaxe",
         "minecraft:golden_axe", "minecraft:golden_shovel"],
        ["minecraft:gold_block", "minecraft:golden_apple", "minecraft:golden_carrot"],
        ["minecraft:crying_obsidian", "minecraft:respawn_anchor"],
    ],

    "nova_structures:chests/end_castle": [
        ["minecraft:end_stone_bricks", "minecraft:end_stone_brick_slab",
         "minecraft:end_stone_brick_stairs", "minecraft:end_stone_brick_wall"],
        ["minecraft:purpur_block", "minecraft:purpur_pillar",
         "minecraft:purpur_slab", "minecraft:purpur_stairs"],
        ["minecraft:end_crystal", "minecraft:popped_chorus_fruit"],
        ["minecraft:netherite_sword", "minecraft:netherite_axe",
         "minecraft:netherite_helmet", "minecraft:netherite_chestplate",
         "minecraft:netherite_leggings", "minecraft:netherite_boots"],
        ["minecraft:diamond_sword", "minecraft:diamond_pickaxe",
         "minecraft:diamond_helmet", "minecraft:diamond_chestplate",
         "minecraft:diamond_leggings", "minecraft:diamond_boots"],
    ],
}


def table_to_filename(table_id: str) -> str:
    """Convert 'minecraft:chests/simple_dungeon' → 'minecraft__chests__simple_dungeon'"""
    return table_id.replace(":", "__").replace("/", "__")


def make_glm(table_id: str, recipe_groups: list) -> dict:
    return {
        "type": f"{MODID}:add_recipe_book",
        "conditions": [
            {
                "condition": "forge:loot_table_id",
                "loot_table_id": table_id
            }
        ],
        "recipe_groups": recipe_groups
    }


def generate():
    glm_dir = f"{OUT}/{MODID}/loot_modifiers"
    forge_dir = f"{OUT}/forge/loot_modifiers"
    os.makedirs(glm_dir, exist_ok=True)
    os.makedirs(forge_dir, exist_ok=True)

    entry_names = []

    for table_id, recipe_groups in TABLES.items():
        filename = table_to_filename(table_id)
        glm = make_glm(table_id, recipe_groups)
        path = f"{glm_dir}/{filename}.json"
        with open(path, "w") as f:
            json.dump(glm, f, indent=2)
        entry_names.append(f"{MODID}:{filename}")

    # global_loot_modifiers.json lists all our modifiers
    global_list = {
        "replace": False,
        "entries": entry_names
    }
    with open(f"{forge_dir}/global_loot_modifiers.json", "w") as f:
        json.dump(global_list, f, indent=2)

    print(f"✓ Generated {len(entry_names)} GLM files")
    print(f"  Vanilla structures: {sum(1 for t in TABLES if t.startswith('minecraft:'))}")
    print(f"  D&T structures:     {sum(1 for t in TABLES if t.startswith('nova_structures:'))}")


if __name__ == "__main__":
    generate()
