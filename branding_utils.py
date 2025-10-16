"""
Aiotize Branding Utilities
Python utility class for working with the branding configuration
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Union, Any


class BrandingManager:
    """Manages branding configuration and provides utility methods"""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize BrandingManager with configuration

        Args:
            config: Dictionary containing branding configuration
        """
        self.config = config
        self.current_theme = "light"

    @classmethod
    def load(cls, path: Union[str, Path] = "branding-config.json") -> "BrandingManager":
        """
        Load branding configuration from JSON file

        Args:
            path: Path to branding-config.json

        Returns:
            BrandingManager instance
        """
        with open(path, 'r') as f:
            config = json.load(f)
        return cls(config)

    def get_theme(self, theme_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Get theme configuration

        Args:
            theme_name: Theme name (light, dark, custom). Uses current_theme if None.

        Returns:
            Theme configuration dictionary
        """
        theme = theme_name or self.current_theme
        return self.config["themes"][theme]

    def set_theme(self, theme_name: str) -> None:
        """
        Set the active theme

        Args:
            theme_name: Theme name (light, dark, custom)

        Raises:
            KeyError: If theme doesn't exist
        """
        if theme_name not in self.config["themes"]:
            raise KeyError(f'Theme "{theme_name}" not found')
        self.current_theme = theme_name

    def get_color(self, color_name: str, theme_name: Optional[str] = None) -> Optional[str]:
        """
        Get a color from the specified or current theme

        Args:
            color_name: Color name (primary, secondary, etc.)
            theme_name: Optional theme name

        Returns:
            Hex color value or None if not found
        """
        theme = self.get_theme(theme_name)
        return theme["colors"].get(color_name)

    def get_text_color(self, text_type: str = "primary", theme_name: Optional[str] = None) -> str:
        """
        Get text color from the specified or current theme

        Args:
            text_type: Text type (primary, secondary, disabled)
            theme_name: Optional theme name

        Returns:
            Hex color value
        """
        theme = self.get_theme(theme_name)
        return theme["colors"]["text"].get(text_type, theme["colors"]["text"]["primary"])

    def get_palette_color(
        self,
        palette_name: str,
        color_name: str,
        shade: int = 2
    ) -> Optional[str]:
        """
        Get a color from a specific palette

        Args:
            palette_name: Palette name (brand, semantic)
            color_name: Color name within the palette
            shade: Shade index (0-4)

        Returns:
            Hex color value or None if not found
        """
        palette = self.config["colorPalettes"].get(palette_name, {})
        colors = palette.get(color_name, [])
        if not colors:
            return None
        return colors[shade] if shade < len(colors) else colors[0]

    def get_typography(self, element: Optional[str] = None) -> Dict[str, Any]:
        """
        Get typography configuration

        Args:
            element: Element type (h1, h2, etc.) or None for all typography config

        Returns:
            Typography configuration dictionary
        """
        if element and element.startswith("h"):
            return self.config["typography"]["headings"].get(element, {})
        return self.config["typography"]

    def get_font_family(self, font_type: str = "primary") -> str:
        """
        Get font family

        Args:
            font_type: Font type (primary, secondary, monospace, display)

        Returns:
            Font family CSS value
        """
        return self.config["typography"]["fontFamilies"].get(font_type, "")

    def get_spacing(self, scale: Union[str, int]) -> str:
        """
        Get spacing value

        Args:
            scale: Spacing scale (0, 1, 2, 3, 4, etc.)

        Returns:
            Spacing value in rem
        """
        scale_str = str(scale)
        return self.config["spacing"]["scale"].get(scale_str, self.config["spacing"]["scale"]["0"])

    def get_layout(self, layout_type: str) -> Dict[str, Any]:
        """
        Get layout configuration

        Args:
            layout_type: Layout type (containers, margins, padding, header, footer)

        Returns:
            Layout configuration dictionary
        """
        return self.config["layout"].get(layout_type, {})

    def get_container(self, size: str = "xl") -> str:
        """
        Get container max-width

        Args:
            size: Container size (sm, md, lg, xl, 2xl)

        Returns:
            Max-width value
        """
        return self.config["layout"]["containers"].get(size, "")

    def get_hyperlink_style(self, state: str = "style") -> Dict[str, Any]:
        """
        Get hyperlink styles

        Args:
            state: Link state (style, hover, visited, active)

        Returns:
            Link style configuration dictionary
        """
        return self.config["hyperlinks"].get(state, {})

    def get_numbering(self, numbering_type: str) -> Dict[str, Any]:
        """
        Get numbering configuration

        Args:
            numbering_type: Numbering type (lists, headings, figures, tables)

        Returns:
            Numbering configuration dictionary
        """
        return self.config["numbering"].get(numbering_type, {})

    def get_imagery_parameters(
        self,
        category: str,
        variant: str = "standard"
    ) -> Optional[Dict[str, Any]]:
        """
        Get imagery parameters

        Args:
            category: Category (lens, tone, warmth)
            variant: Variant within category

        Returns:
            Imagery parameters dictionary or None
        """
        params = self.config["imagery"]["parameters"].get(category, {})
        return params.get(variant)

    def get_imagery_guidelines(self, guideline_type: str) -> Dict[str, Any]:
        """
        Get imagery guidelines

        Args:
            guideline_type: Guideline type (aspectRatios, formats, resolution, optimization)

        Returns:
            Imagery guidelines dictionary
        """
        return self.config["imagery"]["guidelines"].get(guideline_type, {})

    def get_brand_style(self) -> Dict[str, Any]:
        """
        Get brand style for imagery

        Returns:
            Brand style configuration dictionary
        """
        return self.config["imagery"]["brandStyle"]

    def get_topic_structure(self) -> Dict[str, Any]:
        """
        Get topic chronology structure

        Returns:
            Topic structure configuration dictionary
        """
        return self.config["topicChronology"]

    def generate_css_variables(self, theme_name: Optional[str] = None) -> str:
        """
        Generate CSS custom properties from configuration

        Args:
            theme_name: Optional theme name, uses current_theme if None

        Returns:
            CSS string with custom properties
        """
        theme = self.get_theme(theme_name)
        css_lines = [":root {"]

        # Add colors
        for key, value in theme["colors"].items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    css_lines.append(f"  --color-{key}-{sub_key}: {sub_value};")
            else:
                css_lines.append(f"  --color-{key}: {value};")

        # Add spacing
        for key, value in self.config["spacing"]["scale"].items():
            css_lines.append(f"  --spacing-{key}: {value};")

        css_lines.append("}")
        return "\n".join(css_lines)

    def export_config(self, pretty: bool = True) -> str:
        """
        Export configuration as JSON

        Args:
            pretty: Whether to format JSON with indentation

        Returns:
            JSON string
        """
        if pretty:
            return json.dumps(self.config, indent=2)
        return json.dumps(self.config)

    def get_available_themes(self) -> List[str]:
        """
        Get all available themes

        Returns:
            List of theme names
        """
        return list(self.config["themes"].keys())

    @staticmethod
    def check_color_contrast(foreground: str, background: str) -> Dict[str, Union[float, bool, str]]:
        """
        Validate color contrast for accessibility

        Args:
            foreground: Foreground color (hex)
            background: Background color (hex)

        Returns:
            Dictionary with contrast ratio and WCAG compliance
        """
        def hex_to_rgb(hex_color: str) -> tuple:
            """Convert hex color to RGB tuple"""
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        def get_luminance(rgb: tuple) -> float:
            """Calculate relative luminance"""
            r, g, b = [val / 255 for val in rgb]
            r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
            g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
            b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        try:
            fg_rgb = hex_to_rgb(foreground)
            bg_rgb = hex_to_rgb(background)

            l1 = get_luminance(fg_rgb)
            l2 = get_luminance(bg_rgb)
            ratio = (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

            return {
                "ratio": round(ratio, 2),
                "AA": ratio >= 4.5,
                "AAA": ratio >= 7,
                "AA_large": ratio >= 3,
                "AAA_large": ratio >= 4.5
            }
        except (ValueError, IndexError) as e:
            return {"error": f"Invalid color format: {str(e)}"}

    def to_dict(self) -> Dict[str, Any]:
        """
        Get the full configuration as a dictionary

        Returns:
            Configuration dictionary
        """
        return self.config


# Example usage
if __name__ == "__main__":
    # Load configuration
    branding = BrandingManager.load("branding-config.json")

    # Print available themes
    print("Available themes:", branding.get_available_themes())

    # Get primary color from light theme
    primary_color = branding.get_color("primary")
    print(f"Primary color (light theme): {primary_color}")

    # Switch to dark theme
    branding.set_theme("dark")
    primary_color_dark = branding.get_color("primary")
    print(f"Primary color (dark theme): {primary_color_dark}")

    # Check color contrast
    contrast = BrandingManager.check_color_contrast("#FFFFFF", "#0066CC")
    print(f"Contrast ratio: {contrast['ratio']}, WCAG AA: {contrast['AA']}")

    # Get typography for h1
    h1_config = branding.get_typography("h1")
    print(f"H1 font size: {h1_config['fontSize']}")

    # Get spacing value
    spacing = branding.get_spacing(4)
    print(f"Spacing scale 4: {spacing}")
