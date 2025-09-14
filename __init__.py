# -*- coding: utf-8 -*-
from .nodes.quality_queen import QualityQueen
from .nodes.scene_seductress import SceneSeductress
from .nodes.body_bard import BodyBard
from .nodes.glamour_goddess import GlamourGoddess
from .nodes.aesthetic_alchemist import AestheticAlchemist
from .nodes.pose_priestess import PosePriestess
from .nodes.encoding_enchantress import EncodingEnchantress
from .nodes.negativity_nullifier import NegativityNullifier
from .nodes.character_creator import CharacterCreator
from .nodes.character_cache import CharacterCache

NODE_CLASS_MAPPINGS = {
    "EncodingEnchantress": EncodingEnchantress,
    "QualityQueen": QualityQueen,
    "SceneSeductress": SceneSeductress,
    "BodyBard": BodyBard,
    "GlamourGoddess": GlamourGoddess,
    "AestheticAlchemist": AestheticAlchemist,
    "PosePriestess": PosePriestess,
    "NegativityNullifier": NegativityNullifier,
    "CharacterCreator": CharacterCreator,
    "CharacterCache": CharacterCache
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EncodingEnchantress": "🧬 Encoding Enchantress",
    "QualityQueen": "👑 Quality Queen",
    "SceneSeductress": "🎭 Scene Seductress",
    "BodyBard": "💃 Body Bard",
    "GlamourGoddess": "✨ Glamour Goddess",
    "AestheticAlchemist": "💋 Aesthetic Alchemist",
    "PosePriestess": "🤩 Pose Priestess",
    "NegativityNullifier": "🚫 Negativity Nullifier",
    "CharacterCreator": "💖 Character Creator",
    "CharacterCache": "🗃️ Character Cache"
}
