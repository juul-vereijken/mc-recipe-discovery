package com.mc_recipe_discovery.loot;

import com.mc_recipe_discovery.RecipeDiscovery;
import com.mojang.serialization.Codec;
import net.minecraftforge.common.loot.IGlobalLootModifier;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.function.Supplier;

public class ModLootModifiers {

    public static final DeferredRegister<Codec<? extends IGlobalLootModifier>> LOOT_MODIFIERS =
            DeferredRegister.create(ForgeRegistries.Keys.GLOBAL_LOOT_MODIFIER_SERIALIZERS, RecipeDiscovery.MODID);

    /**
     * The one serializer for our modifier type.
     * All structure-specific behaviour is defined in the JSON GLM files —
     * this single codec handles all of them.
     */
    public static final RegistryObject<Codec<RecipeBookLootModifier>> ADD_RECIPE_BOOK =
            LOOT_MODIFIERS.register("add_recipe_book",
                    (Supplier<Codec<RecipeBookLootModifier>>) RecipeBookLootModifier.CODEC::get);
}
