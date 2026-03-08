package com.mc_recipe_discovery.loot;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import it.unimi.dsi.fastutil.objects.ObjectArrayList;
import net.minecraft.core.component.DataComponents;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.level.storage.loot.LootContext;
import net.minecraft.world.level.storage.loot.predicates.LootItemCondition;
import net.minecraftforge.common.loot.IGlobalLootModifier;
import net.minecraftforge.common.loot.LootModifier;

import java.util.List;
import java.util.function.Supplier;

/**
 * RecipeBookLootModifier
 *
 * A Forge Global Loot Modifier that injects a Knowledge Book into any
 * loot table it is applied to. The book is chosen from one of the
 * provided recipe_groups at random (weighted by list position).
 *
 * Because this is a GLM and NOT a loot table override, it stacks
 * non-destructively with any other mod that modifies the same tables.
 * No load-order issues, no conflicts.
 *
 * JSON format (in data/mc_recipe_discovery/loot_modifiers/<name>.json):
 * {
 *   "type": "mc_recipe_discovery:add_recipe_book",
 *   "conditions": [
 *     { "condition": "forge:loot_table_id",
 *       "loot_table_id": "minecraft:chests/simple_dungeon" }
 *   ],
 *   "recipe_groups": [
 *     ["minecraft:crafting_table", "minecraft:chest", "minecraft:furnace"],
 *     ["minecraft:wooden_pickaxe", "minecraft:wooden_axe", "minecraft:wooden_sword"]
 *   ]
 * }
 *
 * Each inner list is a "book": one entry is chosen at random per chest opening.
 * If recipe_groups is empty, no book is added.
 */
public class RecipeBookLootModifier extends LootModifier {

    /**
     * Codec — handles serialization of this modifier from/to JSON.
     * Extends codecStart() to automatically include the "conditions" field.
     */
    public static final Supplier<Codec<RecipeBookLootModifier>> CODEC = () ->
            RecordCodecBuilder.create(instance ->
                    codecStart(instance).and(
                            Codec.list(Codec.list(ResourceLocation.CODEC))
                                    .fieldOf("recipe_groups")
                                    .forGetter(m -> m.recipeGroups)
                    ).apply(instance, RecipeBookLootModifier::new)
            );

    /** All possible books for this table. One is chosen at random per opening. */
    private final List<List<ResourceLocation>> recipeGroups;

    protected RecipeBookLootModifier(LootItemCondition[] conditions,
                                     List<List<ResourceLocation>> recipeGroups) {
        super(conditions);
        this.recipeGroups = recipeGroups;
    }

    @Override
    protected ObjectArrayList<ItemStack> doApply(ObjectArrayList<ItemStack> generatedLoot,
                                                  LootContext context) {
        if (recipeGroups.isEmpty()) {
            return generatedLoot;
        }

        // Pick a random recipe group (earlier groups have equal chance — use uniform random)
        int index = context.getRandom().nextInt(recipeGroups.size());
        List<ResourceLocation> chosenRecipes = recipeGroups.get(index);

        if (chosenRecipes.isEmpty()) {
            return generatedLoot;
        }

        // Build the Knowledge Book with the chosen recipes
        ItemStack book = new ItemStack(Items.KNOWLEDGE_BOOK);
        book.set(DataComponents.RECIPES, chosenRecipes);

        generatedLoot.add(book);
        return generatedLoot;
    }

    @Override
    public Codec<? extends IGlobalLootModifier> codec() {
        return CODEC.get();
    }
}
