package com.mc_recipe_discovery;

import com.mc_recipe_discovery.loot.ModLootModifiers;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod(RecipeDiscovery.MODID)
public class RecipeDiscovery {

    public static final String MODID = "mc_recipe_discovery";

    public RecipeDiscovery() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();

        // Register Global Loot Modifier serializers
        ModLootModifiers.LOOT_MODIFIERS.register(modEventBus);

        modEventBus.addListener(this::commonSetup);
        MinecraftForge.EVENT_BUS.register(this);
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
        // Nothing needed here — all logic is data-driven via JSON GLM files
    }
}
