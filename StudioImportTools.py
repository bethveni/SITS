bl_info = {
    "name": "Studio Import Tools",
    "author": "Created by BethVeni, with help from KingSidorak for the UI",
    "version": (1, 1, 0),
    "blender": (3, 5, 1),
    "location": "",
    "description": "Tools for setting up and optimizing models imported from Bricklink Stud.io.",
    "warning": "CHECK GITHUB FOR UPDATES. Reccomend following the instructions, heeding warnings, and making a backup of your blender file before use.",
    "wiki_url": "https://github.com/bethveni/SITS",
    "category": "!BV"
}

import bpy

def applyColor():
    # WARNING: THE COLORS MAY BE SLIGHTLY DIFFERENT CHANGE SCENE CONTEXT TO STOP GAMMA CORRECTION
    # This will keep the colors somewhat consistent to the HEX (HEX # will still be different with Gamma Correction)
    sce = bpy.context.scene
    sce.display_settings.display_device = 'None'
    color = bpy.data.materials
    # Need num of colors - Dots Stroke color
    numcolors = len(bpy.data.materials)
    # DICTIONARY OF LEGO COLORS
    LEGO_colors = dict([('RUBBER-LIGHT_BLUISH_GRAY',[155,161,157]),('RUBBER-BLACK',[5,19,29]),('PEARL-FLAT_DARK_GOLD',[180,132,85]),('PEARL-FLAT_SILVER',[150,150,150]),('PEARL-LIGHT_GRAY',[156,163,168]),('PEARL-DARK_GRAY',[88,88,88]),('SOLID-BLACK',[5,19,29]),('SOLID-BLUE',[0,85,191]),('SOLID-GREEN',[35,120,65]),('SOLID-DARK_TURQUOISE',[0,143,155]),('SOLID-RED',[201,26,9]),('SOLID-DARK_PINK',[200,112,160]),('SOLID-BROWN',[88,57,39]),('SOLID-LIGHT_GRAY',[155,161,157]),('SOLID-DARK_GRAY',[109,110,92]),('SOLID-LIGHT_BLUE',[180,210,227]),('SOLID-BRIGHT_GREEN',[75,159,74]),('SOLID-LIGHT_TURQUOISE',[85,165,175]),('SOLID-SALMON',[242,112,94]),('SOLID-PINK',[252,151,172]),('SOLID-YELLOW',[242,205,55]),('SOLID-WHITE',[255,255,255]),('SOLID-LIGHT_GREEN',[194,218,184]),('SOLID-LIGHT_YELLOW',[251,230,150]),('SOLID-TAN',[228,205,158]),('SOLID-LIGHT_VIOLET',[201,202,226]),('SOLID-GLOW_IN_DARK_OPAQUE',[212,213,201]),('SOLID-PURPLE',[129,0,123]),('SOLID-DARK_BLUE-VIOLET',[32,50,176]),('SOLID-ORANGE',[254,138,24]),('SOLID-MAGENTA',[146,57,120]),('SOLID-LIME',[187,233,11]),('SOLID-DARK_TAN',[149,138,115]),('SOLID-BRIGHT_PINK',[228,173,200]),('SOLID-MEDIUM_LAVENDER',[172,120,186]),('SOLID-LAVENDER',[225,213,237]),('TRANS-DARK_BLUE',[0,32,160]),('TRANS-GREEN',[132,182,141]),('TRANS-BRIGHT_GREEN',[217,228,167]),('TRANS-RED',[201,26,9]),('TRANS-BLACK',[99,95,82]),('TRANS-LIGHT_BLUE',[174,239,236]),('TRANS-NEON_GREEN',[248,241,132]),('TRANS-VERY_LT_BLUE',[193,223,240]),('TRANS-DARK_PINK',[223,102,149]),('TRANS-YELLOW',[245,205,47]),('TRANS-CLEAR',[252,252,252]),('TRANS-PURPLE',[165,165,203]),('TRANS-NEON_YELLOW',[218,176,0]),('TRANS-NEON_ORANGE',[255,128,13]),('SOLID-CHROME_ANTIQUE_BRASS',[100,90,76]),('SOLID-CHROME_BLUE',[108,150,191]),('SOLID-CHROME_GREEN',[60,179,113]),('SOLID-CHROME_PINK',[170,77,142]),('SOLID-CHROME_BLACK',[27,42,52]),('SOLID-VERY_LIGHT_ORANGE',[243,207,155]),('SOLID-LIGHT_PURPLE',[205,98,152]),('SOLID-REDDISH_BROWN',[88,42,18]),('SOLID-LIGHT_BLUISH_GRAY',[160,165,169]),('SOLID-DARK_BLUISH_GRAY',[108,110,104]),('SOLID-MEDIUM_BLUE',[90,147,219]),('SOLID-MEDIUM_GREEN',[115,220,161]),('SOLID-SPECKLE_BLACK-COPPER',[5,19,29]),('SOLID-SPECKLE_DBGRAY-SILVER',[108,110,104]),('SOLID-LIGHT_PINK',[254,204,207]),('SOLID-LIGHT_FLESH',[246,215,179]),('SOLID-MILKY_WHITE',[255,255,255]),('SOLID-METALLIC_SILVER',[165,169,180]),('SOLID-METALLIC_GREEN',[137,155,95]),('SOLID-METALLIC_GOLD',[219,172,52]),('SOLID-MEDIUM_DARK_FLESH',[204,112,42]),('SOLID-DARK_PURPLE',[63,54,145]),('SOLID-DARK_FLESH',[124,80,58]),('SOLID-FLESH',[208,145,104]),('SOLID-LIGHT_SALMON',[254,186,189]),('SOLID-VIOLET',[67,84,163]),('SOLID-BLUE-VIOLET',[104,116,202]),('GLITTER_TRANS-DARK_PINK',[223,102,149]),('SOLID-MEDIUM_LIME',[199,210,60]),('GLITTER_TRANS-CLEAR',[255,255,255]),('SOLID-AQUA',[179,215,209]),('SOLID-LIGHT_LIME',[217,228,167]),('SOLID-LIGHT_ORANGE',[249,186,97]),('GLITTER_TRANS-PURPLE',[165,165,203]),('SOLID-SPECKLE_BLACK-SILVER',[5,19,29]),('SOLID-SPECKLE_BLACK-GOLD',[5,19,29]),('SOLID-COPPER',[174,122,89]),('SOLID-PEARL_LIGHT_GRAY',[156,163,168]),('SOLID-METAL_BLUE',[121,136,161]),('SOLID-PEARL_LIGHT_GOLD',[220,188,129]),('TRANS-MEDIUM_BLUE',[207,226,247]),('SOLID-PEARL_DARK_GRAY',[87,88,87]),('SOLID-PEARL_VERY_LIGHT_GRAY',[171,173,172]),('SOLID-VERY_LIGHT_BLUISH_GRAY',[230,227,224]),('SOLID-YELLOWISH_GREEN',[223,238,165]),('SOLID-FLAT_DARK_GOLD',[180,132,85]),('SOLID-FLAT_SILVER',[137,135,136]),('TRANS-ORANGE',[240,143,28]),('SOLID-PEARL_WHITE',[242,243,242]),('SOLID-BRIGHT_LIGHT_ORANGE',[248,187,61]),('SOLID-BRIGHT_LIGHT_BLUE',[159,195,233]),('SOLID-RUST',[179,16,4]),('SOLID-BRIGHT_LIGHT_YELLOW',[255,240,58]),('TRANS-PINK',[228,173,200]),('SOLID-SKY_BLUE',[125,191,221]),('TRANS-LIGHT_PURPLE',[150,112,159]),('SOLID-DARK_BLUE',[10,52,99]),('SOLID-DARK_GREEN',[24,70,50]),('GLOW_IN_DARK_TRANS',[189,198,173]),('SOLID-PEARL_GOLD',[170,127,46]),('SOLID-DARK_BROWN',[53,33,0]),('SOLID-MAERSK_BLUE',[53,146,195]),('SOLID-DARK_RED',[114,14,15]),('SOLID-DARK_AZURE',[7,139,201]),('SOLID-MEDIUM_AZURE',[54,174,191]),('SOLID-LIGHT_AQUA',[173,195,192]),('SOLID-OLIVE_GREEN',[155,154,90]),('SOLID-CHROME_GOLD',[187,165,61]),('SOLID-SAND_RED',[214,117,114]),('SOLID-MEDIUM_DARK_PINK',[247,133,177]),('SOLID-EARTH_ORANGE',[250,156,28]),('SOLID-SAND_PURPLE',[132,94,132]),('SOLID-SAND_GREEN',[160,188,172]),('SOLID-SAND_BLUE',[96,116,161]),('SOLID-CHROME_SILVER',[224,224,224]),('SOLID-FABULAND_BROWN',[182,123,80]),('SOLID-MEDIUM_ORANGE',[255,167,11]),('SOLID-DARK_ORANGE',[169,85,0]),('SOLID-VERY_LIGHT_GRAY',[230,227,218]),('SOLID-GLOW_IN_DARK_WHITE',[217,217,217]),('SOLID-MEDIUM_VIOLET',[147,145,0]),('GLITTER_TRANS-NEON_GREEN',[192,245,0]),('GLITTER_TRANS-LIGHT_BLUE',[104,188,197]),('TRANS-FLAME_YELLOWISH_ORANGE',[252,183,109]),('TRANS-FIRE_YELLOW',[251,232,144]),('TRANS-LIGHT_ROYAL_BLUE',[180,212,247]),('SOLID-REDDISH_LILAC',[142,85,151]),('SOLID-VINTAGE_BLUE',[3,156,189]),('SOLID-VINTAGE_GREEN',[30,96,30]),('SOLID-VINTAGE_RED',[202,31,8]),('SOLID-VINTAGE_YELLOW',[243,195,5]),('SOLID-FABULAND_ORANGE',[239,145,33]),('SOLID-MODULEX_WHITE',[244,244,244]),('SOLID-MODULEX_LIGHT_BLUISH_GRAY',[175,181,199]),('SOLID-MODULEX_LIGHT_GRAY',[156,156,156]),('SOLID-MODULEX_CHARCOAL_GRAY',[89,93,96]),('SOLID-MODULEX_TILE_GRAY',[107,90,90]),('SOLID-MODULEX_BLACK',[77,76,82]),('SOLID-MODULEX_TILE_BROWN',[51,0,0]),('SOLID-MODULEX_TERRACOTTA',[92,80,48]),('SOLID-MODULEX_BROWN',[144,116,80]),('SOLID-MODULEX_BUFF',[222,198,156]),('SOLID-MODULEX_RED',[181,44,32]),('SOLID-MODULEX_PINK_RED',[244,92,64]),('SOLID-MODULEX_ORANGE',[244,123,48]),('SOLID-MODULEX_LIGHT_ORANGE',[247,173,99]),('SOLID-MODULEX_LIGHT_YELLOW',[255,227,113]),('SOLID-MODULEX_OCHRE_YELLOW',[254,213,87]),('SOLID-MODULEX_LEMON',[189,198,24]),('SOLID-MODULEX_PASTEL_GREEN',[125,181,56]),('SOLID-MODULEX_OLIVE_GREEN',[124,144,81]),('SOLID-MODULEX_AQUA_GREEN',[39,134,126]),('SOLID-MODULEX_TEAL_BLUE',[70,112,131]),('SOLID-MODULEX_TILE_BLUE',[0,87,166]),('SOLID-MODULEX_MEDIUM_BLUE',[97,175,255]),('SOLID-MODULEX_PASTEL_BLUE',[104,174,206]),('SOLID-MODULEX_VIOLET',[189,125,133]),('SOLID-MODULEX_PINK',[247,133,177]),('SOLID-MODULEX_CLEAR',[255,255,255]),('SOLID-CORAL',[255,105,143]),('SOLID-PASTEL_BLUE',[90,196,218]),('GLITTER_TRANS-ORANGE',[240,143,28]),('TRANS-BLUE_OPAL',[104,188,197]),('TRANS-MEDIUM_REDDISH_VIOLET_OPAL',[206,29,155]),('TRANS-CLEAR_OPAL',[252,252,252]),('TRANS-BROWN_OPAL',[88,57,39]),('TRANS-LIGHT_BRIGHT_GREEN',[201,231,136]),('TRANS-LIGHT_GREEN',[148,229,171]),('TRANS-PURPLE_OPAL',[131,32,183]),('TRANS-GREEN_OPAL',[132,182,141]),('TRANS-DARK_BLUE_OPAL',[0,32,160]),('SOLID-VIBRANT_YELLOW',[235,216,0])])
    LEGO_colors1 = dict([('RUBBER-LIGHT_BLUISH_GRAY.001',[155,161,157]),('RUBBER-BLACK.001',[5,19,29]),('PEARL-FLAT_DARK_GOLD.001',[180,132,85]),('PEARL-FLAT_SILVER.001',[150,150,150]),('PEARL-LIGHT_GRAY.001',[156,163,168]),('PEARL-DARK_GRAY.001',[88,88,88]),('SOLID-BLACK.001',[5,19,29]),('SOLID-BLUE.001',[0,85,191]),('SOLID-GREEN.001',[35,120,65]),('SOLID-DARK_TURQUOISE.001',[0,143,155]),('SOLID-RED.001',[201,26,9]),('SOLID-DARK_PINK.001',[200,112,160]),('SOLID-BROWN.001',[88,57,39]),('SOLID-LIGHT_GRAY.001',[155,161,157]),('SOLID-DARK_GRAY.001',[109,110,92]),('SOLID-LIGHT_BLUE.001',[180,210,227]),('SOLID-BRIGHT_GREEN.001',[75,159,74]),('SOLID-LIGHT_TURQUOISE.001',[85,165,175]),('SOLID-SALMON.001',[242,112,94]),('SOLID-PINK.001',[252,151,172]),('SOLID-YELLOW.001',[242,205,55]),('SOLID-WHITE.001',[255,255,255]),('SOLID-LIGHT_GREEN.001',[194,218,184]),('SOLID-LIGHT_YELLOW.001',[251,230,150]),('SOLID-TAN.001',[228,205,158]),('SOLID-LIGHT_VIOLET.001',[201,202,226]),('SOLID-GLOW_IN_DARK_OPAQUE.001',[212,213,201]),('SOLID-PURPLE.001',[129,0,123]),('SOLID-DARK_BLUE-VIOLET.001',[32,50,176]),('SOLID-ORANGE.001',[254,138,24]),('SOLID-MAGENTA.001',[146,57,120]),('SOLID-LIME.001',[187,233,11]),('SOLID-DARK_TAN.001',[149,138,115]),('SOLID-BRIGHT_PINK.001',[228,173,200]),('SOLID-MEDIUM_LAVENDER.001',[172,120,186]),('SOLID-LAVENDER.001',[225,213,237]),('TRANS-DARK_BLUE.001',[0,32,160]),('TRANS-GREEN.001',[132,182,141]),('TRANS-BRIGHT_GREEN.001',[217,228,167]),('TRANS-RED.001',[201,26,9]),('TRANS-BLACK.001',[99,95,82]),('TRANS-LIGHT_BLUE.001',[174,239,236]),('TRANS-NEON_GREEN.001',[248,241,132]),('TRANS-VERY_LT_BLUE.001',[193,223,240]),('TRANS-DARK_PINK.001',[223,102,149]),('TRANS-YELLOW.001',[245,205,47]),('TRANS-CLEAR.001',[252,252,252]),('TRANS-PURPLE.001',[165,165,203]),('TRANS-NEON_YELLOW.001',[218,176,0]),('TRANS-NEON_ORANGE.001',[255,128,13]),('SOLID-CHROME_ANTIQUE_BRASS.001',[100,90,76]),('SOLID-CHROME_BLUE.001',[108,150,191]),('SOLID-CHROME_GREEN.001',[60,179,113]),('SOLID-CHROME_PINK.001',[170,77,142]),('SOLID-CHROME_BLACK.001',[27,42,52]),('SOLID-VERY_LIGHT_ORANGE.001',[243,207,155]),('SOLID-LIGHT_PURPLE.001',[205,98,152]),('SOLID-REDDISH_BROWN.001',[88,42,18]),('SOLID-LIGHT_BLUISH_GRAY.001',[160,165,169]),('SOLID-DARK_BLUISH_GRAY.001',[108,110,104]),('SOLID-MEDIUM_BLUE.001',[90,147,219]),('SOLID-MEDIUM_GREEN.001',[115,220,161]),('SOLID-SPECKLE_BLACK-COPPER.001',[5,19,29]),('SOLID-SPECKLE_DBGRAY-SILVER.001',[108,110,104]),('SOLID-LIGHT_PINK.001',[254,204,207]),('SOLID-LIGHT_FLESH.001',[246,215,179]),('SOLID-MILKY_WHITE.001',[255,255,255]),('SOLID-METALLIC_SILVER.001',[165,169,180]),('SOLID-METALLIC_GREEN.001',[137,155,95]),('SOLID-METALLIC_GOLD.001',[219,172,52]),('SOLID-MEDIUM_DARK_FLESH.001',[204,112,42]),('SOLID-DARK_PURPLE.001',[63,54,145]),('SOLID-DARK_FLESH.001',[124,80,58]),('SOLID-FLESH.001',[208,145,104]),('SOLID-LIGHT_SALMON.001',[254,186,189]),('SOLID-VIOLET.001',[67,84,163]),('SOLID-BLUE-VIOLET.001',[104,116,202]),('GLITTER_TRANS-DARK_PINK.001',[223,102,149]),('SOLID-MEDIUM_LIME.001',[199,210,60]),('GLITTER_TRANS-CLEAR.001',[255,255,255]),('SOLID-AQUA.001',[179,215,209]),('SOLID-LIGHT_LIME.001',[217,228,167]),('SOLID-LIGHT_ORANGE.001',[249,186,97]),('GLITTER_TRANS-PURPLE.001',[165,165,203]),('SOLID-SPECKLE_BLACK-SILVER.001',[5,19,29]),('SOLID-SPECKLE_BLACK-GOLD.001',[5,19,29]),('SOLID-COPPER.001',[174,122,89]),('SOLID-PEARL_LIGHT_GRAY.001',[156,163,168]),('SOLID-METAL_BLUE.001',[121,136,161]),('SOLID-PEARL_LIGHT_GOLD.001',[220,188,129]),('TRANS-MEDIUM_BLUE.001',[207,226,247]),('SOLID-PEARL_DARK_GRAY.001',[87,88,87]),('SOLID-PEARL_VERY_LIGHT_GRAY.001',[171,173,172]),('SOLID-VERY_LIGHT_BLUISH_GRAY.001',[230,227,224]),('SOLID-YELLOWISH_GREEN.001',[223,238,165]),('SOLID-FLAT_DARK_GOLD.001',[180,132,85]),('SOLID-FLAT_SILVER.001',[137,135,136]),('TRANS-ORANGE.001',[240,143,28]),('SOLID-PEARL_WHITE.001',[242,243,242]),('SOLID-BRIGHT_LIGHT_ORANGE.001',[248,187,61]),('SOLID-BRIGHT_LIGHT_BLUE.001',[159,195,233]),('SOLID-RUST.001',[179,16,4]),('SOLID-BRIGHT_LIGHT_YELLOW.001',[255,240,58]),('TRANS-PINK.001',[228,173,200]),('SOLID-SKY_BLUE.001',[125,191,221]),('TRANS-LIGHT_PURPLE.001',[150,112,159]),('SOLID-DARK_BLUE.001',[10,52,99]),('SOLID-DARK_GREEN.001',[24,70,50]),('GLOW_IN_DARK_TRANS.001',[189,198,173]),('SOLID-PEARL_GOLD.001',[170,127,46]),('SOLID-DARK_BROWN.001',[53,33,0]),('SOLID-MAERSK_BLUE.001',[53,146,195]),('SOLID-DARK_RED.001',[114,14,15]),('SOLID-DARK_AZURE.001',[7,139,201]),('SOLID-MEDIUM_AZURE.001',[54,174,191]),('SOLID-LIGHT_AQUA.001',[173,195,192]),('SOLID-OLIVE_GREEN.001',[155,154,90]),('SOLID-CHROME_GOLD.001',[187,165,61]),('SOLID-SAND_RED.001',[214,117,114]),('SOLID-MEDIUM_DARK_PINK.001',[247,133,177]),('SOLID-EARTH_ORANGE.001',[250,156,28]),('SOLID-SAND_PURPLE.001',[132,94,132]),('SOLID-SAND_GREEN.001',[160,188,172]),('SOLID-SAND_BLUE.001',[96,116,161]),('SOLID-CHROME_SILVER.001',[224,224,224]),('SOLID-FABULAND_BROWN.001',[182,123,80]),('SOLID-MEDIUM_ORANGE.001',[255,167,11]),('SOLID-DARK_ORANGE.001',[169,85,0]),('SOLID-VERY_LIGHT_GRAY.001',[230,227,218]),('SOLID-GLOW_IN_DARK_WHITE.001',[217,217,217]),('SOLID-MEDIUM_VIOLET.001',[147,145,0]),('GLITTER_TRANS-NEON_GREEN.001',[192,245,0]),('GLITTER_TRANS-LIGHT_BLUE.001',[104,188,197]),('TRANS-FLAME_YELLOWISH_ORANGE.001',[252,183,109]),('TRANS-FIRE_YELLOW.001',[251,232,144]),('TRANS-LIGHT_ROYAL_BLUE.001',[180,212,247]),('SOLID-REDDISH_LILAC.001',[142,85,151]),('SOLID-VINTAGE_BLUE.001',[3,156,189]),('SOLID-VINTAGE_GREEN.001',[30,96,30]),('SOLID-VINTAGE_RED.001',[202,31,8]),('SOLID-VINTAGE_YELLOW.001',[243,195,5]),('SOLID-FABULAND_ORANGE.001',[239,145,33]),('SOLID-MODULEX_WHITE.001',[244,244,244]),('SOLID-MODULEX_LIGHT_BLUISH_GRAY.001',[175,181,199]),('SOLID-MODULEX_LIGHT_GRAY.001',[156,156,156]),('SOLID-MODULEX_CHARCOAL_GRAY.001',[89,93,96]),('SOLID-MODULEX_TILE_GRAY.001',[107,90,90]),('SOLID-MODULEX_BLACK.001',[77,76,82]),('SOLID-MODULEX_TILE_BROWN.001',[51,0,0]),('SOLID-MODULEX_TERRACOTTA.001',[92,80,48]),('SOLID-MODULEX_BROWN.001',[144,116,80]),('SOLID-MODULEX_BUFF.001',[222,198,156]),('SOLID-MODULEX_RED.001',[181,44,32]),('SOLID-MODULEX_PINK_RED.001',[244,92,64]),('SOLID-MODULEX_ORANGE.001',[244,123,48]),('SOLID-MODULEX_LIGHT_ORANGE.001',[247,173,99]),('SOLID-MODULEX_LIGHT_YELLOW.001',[255,227,113]),('SOLID-MODULEX_OCHRE_YELLOW.001',[254,213,87]),('SOLID-MODULEX_LEMON.001',[189,198,24]),('SOLID-MODULEX_PASTEL_GREEN.001',[125,181,56]),('SOLID-MODULEX_OLIVE_GREEN.001',[124,144,81]),('SOLID-MODULEX_AQUA_GREEN.001',[39,134,126]),('SOLID-MODULEX_TEAL_BLUE.001',[70,112,131]),('SOLID-MODULEX_TILE_BLUE.001',[0,87,166]),('SOLID-MODULEX_MEDIUM_BLUE.001',[97,175,255]),('SOLID-MODULEX_PASTEL_BLUE.001',[104,174,206]),('SOLID-MODULEX_VIOLET.001',[189,125,133]),('SOLID-MODULEX_PINK.001',[247,133,177]),('SOLID-MODULEX_CLEAR.001',[255,255,255]),('SOLID-CORAL.001',[255,105,143]),('SOLID-PASTEL_BLUE.001',[90,196,218]),('GLITTER_TRANS-ORANGE.001',[240,143,28]),('TRANS-BLUE_OPAL.001',[104,188,197]),('TRANS-MEDIUM_REDDISH_VIOLET_OPAL.001',[206,29,155]),('TRANS-CLEAR_OPAL.001',[252,252,252]),('TRANS-BROWN_OPAL.001',[88,57,39]),('TRANS-LIGHT_BRIGHT_GREEN.001',[201,231,136]),('TRANS-LIGHT_GREEN.001',[148,229,171]),('TRANS-PURPLE_OPAL.001',[131,32,183]),('TRANS-GREEN_OPAL.001',[132,182,141]),('TRANS-DARK_BLUE_OPAL.001',[0,32,160]),('SOLID-VIBRANT_YELLOW.001',[235,216,0]),])
    LEGO_colors2 = dict([('RUBBER-LIGHT_BLUISH_GRAY.002',[155,161,157]),('RUBBER-BLACK.002',[5,19,29]),('PEARL-FLAT_DARK_GOLD.002',[180,132,85]), ('PEARL-FLAT_SILVER.002',[150,150,150]),('PEARL-LIGHT_GRAY.002',[156,163,168]),('PEARL-DARK_GRAY.002',[88,88,88]),('SOLID-BLACK.002',[5,19,29]),('SOLID-BLUE.002',[0,85,191]),('SOLID-GREEN.002',[35,120,65]),('SOLID-DARK_TURQUOISE.002',[0,143,155]),('SOLID-RED.002',[201,26,9]),('SOLID-DARK_PINK.002',[200,112,160]),('SOLID-BROWN.002',[88,57,39]),('SOLID-LIGHT_GRAY.002',[155,161,157]),('SOLID-DARK_GRAY.002',[109,110,92]),('SOLID-LIGHT_BLUE.002',[180,210,227]),('SOLID-BRIGHT_GREEN.002',[75,159,74]),('SOLID-LIGHT_TURQUOISE.002',[85,165,175]),('SOLID-SALMON.002',[242,112,94]),('SOLID-PINK.002',[252,151,172]),('SOLID-YELLOW.002',[242,205,55]),('SOLID-WHITE.002',[255,255,255]),('SOLID-LIGHT_GREEN.002',[194,218,184]),('SOLID-LIGHT_YELLOW.002',[251,230,150]),('SOLID-TAN.002',[228,205,158]),('SOLID-LIGHT_VIOLET.002',[201,202,226]),('SOLID-GLOW_IN_DARK_OPAQUE.002',[212,213,201]),('SOLID-PURPLE.002',[129,0,123]),('SOLID-DARK_BLUE-VIOLET.002',[32,50,176]),('SOLID-ORANGE.002',[254,138,24]),('SOLID-MAGENTA.002',[146,57,120]),('SOLID-LIME.002',[187,233,11]),('SOLID-DARK_TAN.002',[149,138,115]),('SOLID-BRIGHT_PINK.002',[228,173,200]),('SOLID-MEDIUM_LAVENDER.002',[172,120,186]),('SOLID-LAVENDER.002',[225,213,237]),('TRANS-DARK_BLUE.002',[0,32,160]),('TRANS-GREEN.002',[132,182,141]),('TRANS-BRIGHT_GREEN.002',[217,228,167]),('TRANS-RED.002',[201,26,9]),('TRANS-BLACK.002',[99,95,82]),('TRANS-LIGHT_BLUE.002',[174,239,236]),('TRANS-NEON_GREEN.002',[248,241,132]),('TRANS-VERY_LT_BLUE.002',[193,223,240]),('TRANS-DARK_PINK.002',[223,102,149]),('TRANS-YELLOW.002',[245,205,47]),('TRANS-CLEAR.002',[252,252,252]),('TRANS-PURPLE.002',[165,165,203]),('TRANS-NEON_YELLOW.002',[218,176,0]),('TRANS-NEON_ORANGE.002',[255,128,13]),('SOLID-CHROME_ANTIQUE_BRASS.002',[100,90,76]),('SOLID-CHROME_BLUE.002',[108,150,191]),('SOLID-CHROME_GREEN.002',[60,179,113]),('SOLID-CHROME_PINK.002',[170,77,142]),('SOLID-CHROME_BLACK.002',[27,42,52]),('SOLID-VERY_LIGHT_ORANGE.002',[243,207,155]),('SOLID-LIGHT_PURPLE.002',[205,98,152]),('SOLID-REDDISH_BROWN.002',[88,42,18]),('SOLID-LIGHT_BLUISH_GRAY.002',[160,165,169]),('SOLID-DARK_BLUISH_GRAY.002',[108,110,104]),('SOLID-MEDIUM_BLUE.002',[90,147,219]),('SOLID-MEDIUM_GREEN.002',[115,220,161]),('SOLID-SPECKLE_BLACK-COPPER.002',[5,19,29]),('SOLID-SPECKLE_DBGRAY-SILVER.002',[108,110,104]),('SOLID-LIGHT_PINK.002',[254,204,207]),('SOLID-LIGHT_FLESH.002',[246,215,179]),('SOLID-MILKY_WHITE.002',[255,255,255]),('SOLID-METALLIC_SILVER.002',[165,169,180]),('SOLID-METALLIC_GREEN.002',[137,155,95]),('SOLID-METALLIC_GOLD.002',[219,172,52]),('SOLID-MEDIUM_DARK_FLESH.002',[204,112,42]),('SOLID-DARK_PURPLE.002',[63,54,145]),('SOLID-DARK_FLESH.002',[124,80,58]),('SOLID-FLESH.002',[208,145,104]),('SOLID-LIGHT_SALMON.002',[254,186,189]),('SOLID-VIOLET.002',[67,84,163]),('SOLID-BLUE-VIOLET.002',[104,116,202]),('GLITTER_TRANS-DARK_PINK.002',[223,102,149]),('SOLID-MEDIUM_LIME.002',[199,210,60]),('GLITTER_TRANS-CLEAR.002',[255,255,255]),('SOLID-AQUA.002',[179,215,209]),('SOLID-LIGHT_LIME.002',[217,228,167]),('SOLID-LIGHT_ORANGE.002',[249,186,97]),('GLITTER_TRANS-PURPLE.002',[165,165,203]),('SOLID-SPECKLE_BLACK-SILVER.002',[5,19,29]),('SOLID-SPECKLE_BLACK-GOLD.002',[5,19,29]),('SOLID-COPPER.002',[174,122,89]),('SOLID-PEARL_LIGHT_GRAY.002',[156,163,168]),('SOLID-METAL_BLUE.002',[121,136,161]),('SOLID-PEARL_LIGHT_GOLD.002',[220,188,129]),('TRANS-MEDIUM_BLUE.002',[207,226,247]),('SOLID-PEARL_DARK_GRAY.002',[87,88,87]),('SOLID-PEARL_VERY_LIGHT_GRAY.002',[171,173,172]),('SOLID-VERY_LIGHT_BLUISH_GRAY.002',[230,227,224]),('SOLID-YELLOWISH_GREEN.002',[223,238,165]),('SOLID-FLAT_DARK_GOLD.002',[180,132,85]),('SOLID-FLAT_SILVER.002',[137,135,136]),('TRANS-ORANGE.002',[240,143,28]),('SOLID-PEARL_WHITE.002',[242,243,242]),('SOLID-BRIGHT_LIGHT_ORANGE.002',[248,187,61]),('SOLID-BRIGHT_LIGHT_BLUE.002',[159,195,233]),('SOLID-RUST.002',[179,16,4]),('SOLID-BRIGHT_LIGHT_YELLOW.002',[255,240,58]),('TRANS-PINK.002',[228,173,200]),('SOLID-SKY_BLUE.002',[125,191,221]),('TRANS-LIGHT_PURPLE.002',[150,112,159]),('SOLID-DARK_BLUE.002',[10,52,99]),('SOLID-DARK_GREEN.002',[24,70,50]),('GLOW_IN_DARK_TRANS.002',[189,198,173]),('SOLID-PEARL_GOLD.002',[170,127,46]),('SOLID-DARK_BROWN.002',[53,33,0]),('SOLID-MAERSK_BLUE.002',[53,146,195]),('SOLID-DARK_RED.002',[114,14,15]),('SOLID-DARK_AZURE.002',[7,139,201]),('SOLID-MEDIUM_AZURE.002',[54,174,191]),('SOLID-LIGHT_AQUA.002',[173,195,192]),('SOLID-OLIVE_GREEN.002',[155,154,90]),('SOLID-CHROME_GOLD.002',[187,165,61]),('SOLID-SAND_RED.002',[214,117,114]),('SOLID-MEDIUM_DARK_PINK.002',[247,133,177]),('SOLID-EARTH_ORANGE.002',[250,156,28]),('SOLID-SAND_PURPLE.002',[132,94,132]),('SOLID-SAND_GREEN.002',[160,188,172]),('SOLID-SAND_BLUE.002',[96,116,161]),('SOLID-CHROME_SILVER.002',[224,224,224]),('SOLID-FABULAND_BROWN.002',[182,123,80]),('SOLID-MEDIUM_ORANGE.002',[255,167,11]),('SOLID-DARK_ORANGE.002',[169,85,0]),('SOLID-VERY_LIGHT_GRAY.002',[230,227,218]),('SOLID-GLOW_IN_DARK_WHITE.002',[217,217,217]),('SOLID-MEDIUM_VIOLET.002',[147,145,0]),('GLITTER_TRANS-NEON_GREEN.002',[192,245,0]),('GLITTER_TRANS-LIGHT_BLUE.002',[104,188,197]),('TRANS-FLAME_YELLOWISH_ORANGE.002',[252,183,109]),('TRANS-FIRE_YELLOW.002',[251,232,144]),('TRANS-LIGHT_ROYAL_BLUE.002',[180,212,247]),('SOLID-REDDISH_LILAC.002',[142,85,151]),('SOLID-VINTAGE_BLUE.002',[3,156,189]),('SOLID-VINTAGE_GREEN.002',[30,96,30]),('SOLID-VINTAGE_RED.002',[202,31,8]),('SOLID-VINTAGE_YELLOW.002',[243,195,5]),('SOLID-FABULAND_ORANGE.002',[239,145,33]),('SOLID-MODULEX_WHITE.002',[244,244,244]),('SOLID-MODULEX_LIGHT_BLUISH_GRAY.002',[175,181,199]),('SOLID-MODULEX_LIGHT_GRAY.002',[156,156,156]),('SOLID-MODULEX_CHARCOAL_GRAY.002',[89,93,96]),('SOLID-MODULEX_TILE_GRAY.002',[107,90,90]),('SOLID-MODULEX_BLACK.002',[77,76,82]),('SOLID-MODULEX_TILE_BROWN.002',[51,0,0]),('SOLID-MODULEX_TERRACOTTA.002',[92,80,48]),('SOLID-MODULEX_BROWN.002',[144,116,80]),('SOLID-MODULEX_BUFF.002',[222,198,156]),('SOLID-MODULEX_RED.002',[181,44,32]),('SOLID-MODULEX_PINK_RED.002',[244,92,64]),('SOLID-MODULEX_ORANGE.002',[244,123,48]),('SOLID-MODULEX_LIGHT_ORANGE.002',[247,173,99]),('SOLID-MODULEX_LIGHT_YELLOW.002',[255,227,113]),('SOLID-MODULEX_OCHRE_YELLOW.002',[254,213,87]),('SOLID-MODULEX_LEMON.002',[189,198,24]),('SOLID-MODULEX_PASTEL_GREEN.002',[125,181,56]),('SOLID-MODULEX_OLIVE_GREEN.002',[124,144,81]),('SOLID-MODULEX_AQUA_GREEN.002',[39,134,126]),('SOLID-MODULEX_TEAL_BLUE.002',[70,112,131]),('SOLID-MODULEX_TILE_BLUE.002',[0,87,166]),('SOLID-MODULEX_MEDIUM_BLUE.002',[97,175,255]),('SOLID-MODULEX_PASTEL_BLUE.002',[104,174,206]),('SOLID-MODULEX_VIOLET.002',[189,125,133]),('SOLID-MODULEX_PINK.002',[247,133,177]),('SOLID-MODULEX_CLEAR.002',[255,255,255]),('SOLID-CORAL.002',[255,105,143]),('SOLID-PASTEL_BLUE.002',[90,196,218]),('GLITTER_TRANS-ORANGE.002',[240,143,28]),('TRANS-BLUE_OPAL.002',[104,188,197]),('TRANS-MEDIUM_REDDISH_VIOLET_OPAL.002',[206,29,155]),('TRANS-CLEAR_OPAL.002',[252,252,252]),('TRANS-BROWN_OPAL.002',[88,57,39]),('TRANS-LIGHT_BRIGHT_GREEN.002',[201,231,136]),('TRANS-LIGHT_GREEN.002',[148,229,171]),('TRANS-PURPLE_OPAL.002',[131,32,183]),('TRANS-GREEN_OPAL.002',[132,182,141]),('TRANS-DARK_BLUE_OPAL.002',[0,32,160]),('SOLID-VIBRANT_YELLOW.002',[235,216,0]),])
    LEGO_colors = {**LEGO_colors, **LEGO_colors1, **LEGO_colors2}
    # Loop through list of materials. Ignore Dots Stroke Color and un-named Materials
    for i in range(0,numcolors):
        if color[i].name[0] != "0" and color[i].name != "Material" and color[i].name != 'Dots Stroke':
            # Look up material's RGB as a list from the LEGO dictionary
            RGB = LEGO_colors.get(color[i].name)
            if bool(RGB):
                # Normalize the RGB list
                RGBnorm = [RGB[0]/255, RGB[1]/255, RGB[2]/255, 1]
                # Assign RGB array to material's color
                color[i].diffuse_color = (RGBnorm[0],RGBnorm[1],RGBnorm[2],RGBnorm[3])
                print(color[i].name, "has been applied.")

            else: print("ERROR:", color[i].name, "was not defined in the color dictionary.")

def colorConvert():
    bpy.context.scene.display_settings.display_device = "None"
    # ONLY WORKS IF THIS IS YOUR FIRST TIME IMPORTING THE .dae FILE INTO BLENDER
    # IF YOU HAVE SAVED AND QUIT, THIS TOOL WILL RUN INTO ERRORS!
    for part in bpy.data.objects:
        for color in part.material_slots:
            if color.name[0] != "0" and color.name != "Material" and color.name != 'Dots Stroke' and color.name[-4:-1] != ".00":
                print("Applying Stud.io color for",color.name,"in",part.name)
                studiocolor = color.name + ".001"
                color.material = bpy.data.materials[studiocolor]

def deleteNodes():
    # Collect group and number of objects
    group =  bpy.data.collections[0].objects
    grouplen = len(group)

    # Unparent objects from nodes: [A] -> [Alt P] -> Obj Keep Transform
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

    # DESELECT CAMERA AND LIGHT NDOES
    group['Camera_Node'].select_set(False)
    group['Light_Node_1'].select_set(False)
    group['Light_Node_2'].select_set(False)

    # REMEMBER TO FLIP UPSIDE DOWN!
    bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True))
    bpy.ops.object.select_all(action='DESELECT')

    # Loop through colleciton
    for i in range(0,grouplen):
        # If the object is an EMPTY NODE, select for deletion
        # This will correspond to the NODE for each OBJECT
        if group[i].type == 'EMPTY':
            group[i].select_set(True)

    # Delete all Nodes
    bpy.ops.object.delete()
    bpy.ops.object.select_all(action='DESELECT')

def flipObjects():
    for o in bpy.data.collections[0].objects:
        if o.type == 'OBJECT':
            o.select_set(True)
    bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True))
    bpy.ops.object.select_all(action='DESELECT')

def cleanMesh():
    meshrecord = []  # List of unique mesh names
    parts = bpy.data.collections[0].objects
    numparts = len(parts)
    cont = bpy.context.area.type
    print("OPTIMIZING MESH VERTICES FOR COLLECTION")
    print("========================================")
    # For each obj: [Tab] -> [A] -> [M] -> Vertices by distance -> [Alt J]
    for i in range(0, numparts):  # Any objects w/ same mesh dont get affected twice
        # Only optimize the mesh if it is unique and hasnt been edited before
        if not parts[i].data.name in meshrecord:
            parts[i].select_set(True)
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.remove_doubles()
            bpy.ops.mesh.tris_convert_to_quads()
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
            bpy.ops.object.editmode_toggle()
            bpy.context.object.data.use_auto_smooth = True
            parts[i].select_set(False)
            meshrecord.append(parts[i].data.name)
    # Cycle through each unique piece's mesh and auto-smooth
    for piece in bpy.data.meshes:
        piece.use_auto_smooth = True
    print("Objects in collection were successfully optimized.\n")

def delinkMesh():
    parts = bpy.data.collections[0].objects
    numparts = len(parts)
    cont = bpy.context.area.type
    print("UNLINKING MESH DATA FOR COLLECTION")
    print("========================================")
    for i in range(0,numparts):
        # Set the mesh data of the object equal to a copy of the mesh.
        parts[i].data = parts[i].data.copy()
        print("Delinking", parts[i].name)

def setOrigin():
    parts = bpy.data.collections[0].objects
    numparts = len(parts)
    cont = bpy.context.area.type
    # Set all objects to the world origin
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    bpy.context.area.type = 'VIEW_3D'
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
    bpy.context.area.type = 'TEXT_EDITOR'
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.context.area.type = 'VIEW_3D'

    # For reach object get data -> make data copy -> set original equal to that.
    for obj in bpy.data.objects:
        obj.data = obj.data.copy()

def renameMeshListPolys():
    # This function renames meshes based on vertix data
    # To rename them from generic Object tag to part ID
    # Also includes list of Polygons for each mesh
    # For export to spreadsheets
    sumfaces = []
    bpy.ops.wm.console_toggle()
    print("\n=========================")
    print("Mesh Properties List")
    print("=========================")
    print("Part ID# : Tris: Polys:")
    for o in bpy.data.collections[0].objects:
        if o.type != 'MESH':
            continue
        # o.data = object.data
        me = o.data
        o.name = bpy.data.objects[o.name].data.name
        # Cut "Part-" from the name (first 5 letters)
        if o.name[:5] == "Part-": o.name = o.name[5:]
        # Cut "_dot_dat" from name (last 8 letters)
        if o.name[-8:] == "_dot_dat": o.name = o.name[:-8]
        elif o.name[-8:-1] == "_dat.00": o.name = o.name[:-12]
        elif o.name[-8:-1] == "_dat.01": o.name = o.name[:-12]
        elif o.name[-8:-1] == "_dat.02": o.name = o.name[:-12]
        # print(o.name)
        # Get vertices, edges, and polygons from meshes
        verts = len(me.vertices)
        edges = len(me.edges)
        faces = len(me.polygons)
        # https://b3d.interplanety.org/en/how-to-get-the-number-of-triangles-in-a-mesh/
        # Calculate the Tris for each mesh and store in variable
        me.calc_loop_triangles()
        tris = len(me.loop_triangles)
        sumfaces.append(faces)
    #    print("%s: verts:%d edges:%d polys: %d tris: %d"
    #            % (o.name, verts, edges, faces, tris))
    # Just print out the Polygons and Tris. Split data in excel.
        print("%s;%d;%d"
            % (o.name,tris, faces))

    print("Total Polys: %d" % sum(sumfaces))

def rankPolys():
    # This function prints out part IDs and their tris,
    # number of instances, and total tri contribution
    # from least to greatest in value.
    """
    Print out a list ranking mesh IDs by number of Tris by inputting "tris"
    Print out list ranking mesh IDs by total contributing Tris by leaving input as ""
    """
    trisdictionary = {}
    trisumdictionary = {}
    usersdictionary = {}
    tristotal = 0
    print("\n=========================")
    print("Mesh Properties List")
    print("=========================")
    print("Part ID# : Tris: Uses: TriSum")
    for me in bpy.data.meshes:
        # o.data = object.data
        meshname = me.name
        # Cut "Part-" from the name (first 5 letters)
        if meshname[:5] == "Part-": meshname = meshname[5:]
        # Cut "_dot_dat" from name (last 8 letters)
        if meshname[-8:] == "_dot_dat":
            meshname = meshname[:-8]
        # The following may be redundant if the above line works in every case
        elif meshname[-8:-1] == "_dat.00":
            meshname = meshname[:-12]
        elif meshname[-8:-1] == "_dat.01":
            meshname = meshname[:-12]
        elif meshname[-8:-1] == "_dat.02":
            meshname = meshname[:-12]

        # https://b3d.interplanety.org/en/how-to-get-the-number-of-triangles-in-a-mesh/
        # Calculate the Tris for the mesh and multiply by number of mesh instances
        tris = len(me.loop_triangles)
        users = me.users
        trisum = tris * users

        # Add to total tri counter
        tristotal += trisum

        # Update dictionaries
        trisdictionary.update({meshname: tris})
        trisumdictionary.update({meshname: trisum})
        usersdictionary.update({meshname: users})

    # Rank the dictionary's tri counts from smallest to largest
    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    trisorted = dict(sorted(trisdictionary.items(), key=lambda item: item[1]))
    trisumsorted = dict(sorted(trisumdictionary.items(), key=lambda item: item[1]))

    for mesh in trisumsorted:
        meshtris = trisorted[mesh]
        meshtrisum = trisumsorted[mesh]
        meshusers = usersdictionary[mesh]
        # Print results with commas (f"{num:,}")
        print("%s; %s; %d; %s:" % (mesh, f'{meshtris:,}', meshusers, f'{meshtrisum:,}'))
    print("Meshes have been ranked from smallest to largest polygon contribution.")
    print("Total Polys:", f'{tristotal:,}')

class StudioTools(bpy.types.Panel):
    # THIS TYPE OF CLASS DEFINES A PANEL.
    # USE THIS AS A TEMPLATE TO MAKE MORE PANELS FOR YOUR TOOL
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Studio Import Tools V1.0"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Studio Import Tools")
        layout.operator("wm.collada_import", text="Import Collada (.dae)")
        layout.operator("studiotools.legocolors", text="Lego Colors")
        layout.operator("studiotools.studiocolors", text="Studio Colors")
        layout.operator("studiotools.flipclean", text="Flip & Clean")

        layout.label(text="Mesh Editing Tools (CAUTION)")
        layout.operator("studiotools.cleanparts", text="Clean Parts")
        layout.operator("studiotools.unlinkparts", text="Unlink Parts")
        layout.operator("studiotools.setatorigin", text="Set At Origin")

        layout.label(text="Data Gathering Tools")
        layout.operator("studiotools.relabelparts", text="Label Part IDs")
        layout.operator("studiotools.printtriranks", text="Print Tris Ranked")
        layout.operator("studiotools.openconsole", text="Toggle Console")

        layout.label(text="Support the Project!")
        layout.operator("studiotools.githubpage", text="SITS Github")
        layout.operator("studiotools.donationpage", text="Ko-Fi Donations")

class LegoColors(bpy.types.Operator):
    """Swap the objects in the scene to Lego Colors"""
    bl_idname = "studiotools.legocolors"
    bl_label = "Lego Colors"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        applyColor()
        return {'FINISHED'}

class StudioColors(bpy.types.Operator):
    """Swap the objects in the scene to Studio Colors"""
    bl_idname = "studiotools.studiocolors"
    bl_label = "Studio Colors"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        colorConvert()
        return {'FINISHED'}

class FlipAndNodeDelete(bpy.types.Operator):
    """Delete nodes and flip model upright"""
    bl_idname = "studiotools.flipclean"
    bl_label = "Flip & Clean"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        deleteNodes()
        return {'FINISHED'}

class CleanParts(bpy.types.Operator):
    """Optimize vertices, convert Tris to Quads, apply auto-smooth, and remove custom split normal data"""
    bl_idname = "studiotools.cleanparts"
    bl_label = "Clean Parts"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        cleanMesh()
        return {'FINISHED'}

class UnlinkParts(bpy.types.Operator):
    """Unlink mesh data between parts of the same shape in the first collection"""
    bl_idname = "studiotools.unlinkparts"
    bl_label = "Unlink Parts"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        delinkMesh()
        return {'FINISHED'}

class SetAtOrigin(bpy.types.Operator):
    """Set the Collection at the world origin using the selected object as a reference point. Please use in OBJECT MODE and make sure you have the desired active object selected."""
    bl_idname = "studiotools.setatorigin"
    bl_label = "Set At Origin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        setOrigin()
        return {'FINISHED'}

class LabelPartIDs(bpy.types.Operator):
    """Renames parts to their IDs and prints their polygons in System Console"""
    bl_idname = "studiotools.relabelparts"
    bl_label = "Label Part IDs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        renameMeshListPolys()
        return {'FINISHED'}

class PrintTriRanks(bpy.types.Operator):
    """Prints in the System Console all unique meshes and their Tris, Instances, and total Tri contribution"""
    bl_idname = "studiotools.printtriranks"
    bl_label = "Print Tris Ranked"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        rankPolys()
        return {'FINISHED'}

class OpenConsole(bpy.types.Operator):
    """View the System Console for data results and messages from scripts. Click again to close"""
    bl_idname = "studiotools.openconsole"
    bl_label = "Toggle Console"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.console_toggle()
        return {'FINISHED'}

class GithubPage(bpy.types.Operator):
    """Check out the most up-to-date version of the SITS tool on Github"""
    bl_idname = "studiotools.githubpage"
    bl_label = "SITS Github"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.url_open(url = "https://github.com/bethveni/SITS")
        return {'FINISHED'}

class DonationPage(bpy.types.Operator):
    """Support the ongoing development of this project by donating on Ko-Fi! Monthly donations add you to the Supporters list on Github"""
    bl_idname = "studiotools.donationpage"
    bl_label = "Fund SITS on Ko-Fi"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.url_open(url = "https://ko-fi.com/bethveni")
        return {'FINISHED'}



def register():
    bpy.utils.register_class(StudioTools)
    bpy.utils.register_class(LegoColors)
    bpy.utils.register_class(StudioColors)
    bpy.utils.register_class(FlipAndNodeDelete)
    bpy.utils.register_class(CleanParts)
    bpy.utils.register_class(UnlinkParts)
    bpy.utils.register_class(SetAtOrigin)
    bpy.utils.register_class(LabelPartIDs)
    bpy.utils.register_class(PrintTriRanks)
    bpy.utils.register_class(OpenConsole)
    bpy.utils.register_class(GithubPage)
    bpy.utils.register_class(DonationPage)

def unregister():
    bpy.utils.unregister_class(StudioTools)
    bpy.utils.unregister_class(LegoColors)
    bpy.utils.unregister_class(StudioColors)
    bpy.utils.unregister_class(FlipAndNodeDelete)
    bpy.utils.unregister_class(CleanParts)
    bpy.utils.unregister_class(UnlinkParts)
    bpy.utils.unregister_class(SetAtOrigin)
    bpy.utils.unregister_class(LabelPartIDs)
    bpy.utils.unregister_class(PrintTriRanks)
    bpy.utils.unregister_class(OpenConsole)
    bpy.utils.unregister_class(GithubPage)
    bpy.utils.unregister_class(DonationPage)

if __name__ == "__main__":
    register()
