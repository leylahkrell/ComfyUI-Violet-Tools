import yaml
import os
import random

class GlamourGoddess:
    """
    A ComfyUI node that assembles descriptive strings for hair and makeup using modular aesthetic features.
    Pulls options from feature_lists/glamour_goddess.yaml with field-specific color lists.
    """

    style_path = os.path.join(os.path.dirname(__file__), "feature_lists", "glamour_goddess.yaml")
    
    with open(style_path, "r", encoding="utf-8") as f:
        FEATURES = yaml.safe_load(f)

    @classmethod
    def INPUT_TYPES(cls):
        """
        Define the input parameters for the ComfyUI node interface.
        All fields now use their complete lists from the YAML file.
        
        Returns:
            dict: Node input configuration with dropdown selections
        """
        types = {"required": {}}
        
        for key, options in cls.FEATURES.items():
            # All fields now have complete lists including colors
            types["required"][key] = (
                ["Unspecified", "Random"] + options,
                {"default": "Unspecified"}
            )
        
        types["required"]["extra"] = ("STRING", {"multiline": True, "default": ""})
        return types

    RETURN_TYPES = ("GLAMOUR_STRING",)
    RETURN_NAMES = ("glamour",)
    FUNCTION = "invoke"
    CATEGORY = "Violet Tools 💅"

    @staticmethod
    def IS_CHANGED(**kwargs):
        import time
        return time.time()

    def pick(self, key, choice):
        """
        Process field selection with simplified handling since all options are now complete.
        
        Args:
            key (str): Field name
            choice (str): User selection from dropdown
            
        Returns:
            str: Processed field value
        """
        if choice == "Unspecified":
            return ""
        elif choice == "Random":
            return random.choice(self.FEATURES[key])
        else:
            return choice

    def invoke(self, **kwargs):
        parts = []

        for key in self.FEATURES:
            val = self.pick(key, kwargs.get(key, "Unspecified"))
            if val:
                parts.append(val.lower())

        if kwargs.get("extra"):
            extra = kwargs["extra"].strip()
            if extra:
                parts.append(extra)

        glamour = ", ".join(parts)
        return (glamour,)

NODE_CLASS_MAPPINGS = {
    "GlamourGoddess": GlamourGoddess,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GlamourGoddess": "✨ Glamour Goddess",
}