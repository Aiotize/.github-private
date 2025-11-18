/**
 * Aiotize Branding Utilities
 * Utility functions for working with the branding configuration
 */

class BrandingManager {
  constructor(config) {
    this.config = config;
    this.currentTheme = 'light';
  }

  /**
   * Load branding configuration from JSON file
   * @param {string} path - Path to branding-config.json
   * @returns {Promise<BrandingManager>}
   */
  static async load(path = './branding-config.json') {
    const response = await fetch(path);
    const config = await response.json();
    return new BrandingManager(config);
  }

  /**
   * Get the current theme configuration
   * @returns {Object} Theme configuration object
   */
  getTheme(themeName = this.currentTheme) {
    return this.config.themes[themeName];
  }

  /**
   * Set the active theme
   * @param {string} themeName - Theme name (light, dark, custom)
   */
  setTheme(themeName) {
    if (!this.config.themes[themeName]) {
      throw new Error(`Theme "${themeName}" not found`);
    }
    this.currentTheme = themeName;
    document.documentElement.setAttribute('data-theme', themeName);
    localStorage.setItem('theme', themeName);
  }

  /**
   * Get a color from the current theme
   * @param {string} colorName - Color name (primary, secondary, etc.)
   * @returns {string} Hex color value
   */
  getColor(colorName) {
    const theme = this.getTheme();
    return theme.colors[colorName] || null;
  }

  /**
   * Get text color from the current theme
   * @param {string} type - Text type (primary, secondary, disabled)
   * @returns {string} Hex color value
   */
  getTextColor(type = 'primary') {
    const theme = this.getTheme();
    return theme.colors.text[type] || theme.colors.text.primary;
  }

  /**
   * Get a color from a specific palette
   * @param {string} paletteName - Palette name (brand, semantic)
   * @param {string} colorName - Color name within the palette
   * @param {number} shade - Shade index (0-4)
   * @returns {string} Hex color value
   */
  getPaletteColor(paletteName, colorName, shade = 2) {
    const palette = this.config.colorPalettes[paletteName];
    if (!palette || !palette[colorName]) {
      return null;
    }
    return palette[colorName][shade] || palette[colorName][0];
  }

  /**
   * Get typography configuration
   * @param {string} element - Element type (h1, h2, etc.)
   * @returns {Object} Typography configuration
   */
  getTypography(element) {
    if (element.startsWith('h')) {
      return this.config.typography.headings[element];
    }
    return this.config.typography;
  }

  /**
   * Get font family
   * @param {string} type - Font type (primary, secondary, monospace, display)
   * @returns {string} Font family CSS value
   */
  getFontFamily(type = 'primary') {
    return this.config.typography.fontFamilies[type];
  }

  /**
   * Get spacing value
   * @param {string|number} scale - Spacing scale (0, 1, 2, 3, 4, etc.)
   * @returns {string} Spacing value in rem
   */
  getSpacing(scale) {
    return this.config.spacing.scale[scale] || this.config.spacing.scale['0'];
  }

  /**
   * Get layout configuration
   * @param {string} type - Layout type (containers, margins, padding, header, footer)
   * @returns {Object} Layout configuration
   */
  getLayout(type) {
    return this.config.layout[type];
  }

  /**
   * Get container max-width
   * @param {string} size - Container size (sm, md, lg, xl, 2xl)
   * @returns {string} Max-width value
   */
  getContainer(size = 'xl') {
    return this.config.layout.containers[size];
  }

  /**
   * Get hyperlink styles
   * @param {string} state - Link state (style, hover, visited, active)
   * @returns {Object} Link style configuration
   */
  getHyperlinkStyle(state = 'style') {
    return this.config.hyperlinks[state];
  }

  /**
   * Get numbering configuration
   * @param {string} type - Numbering type (lists, headings, figures, tables)
   * @returns {Object} Numbering configuration
   */
  getNumbering(type) {
    return this.config.numbering[type];
  }

  /**
   * Get imagery parameters
   * @param {string} category - Category (lens, tone, warmth)
   * @param {string} variant - Variant within category (standard, wide, professional, etc.)
   * @returns {Object} Imagery parameters
   */
  getImageryParameters(category, variant = 'standard') {
    return this.config.imagery.parameters[category]?.[variant];
  }

  /**
   * Get imagery guidelines
   * @param {string} type - Guideline type (aspectRatios, formats, resolution, optimization)
   * @returns {Object} Imagery guidelines
   */
  getImageryGuidelines(type) {
    return this.config.imagery.guidelines[type];
  }

  /**
   * Get brand style for imagery
   * @returns {Object} Brand style configuration
   */
  getBrandStyle() {
    return this.config.imagery.brandStyle;
  }

  /**
   * Get topic chronology structure
   * @returns {Object} Topic structure configuration
   */
  getTopicStructure() {
    return this.config.topicChronology;
  }

  /**
   * Apply theme to document root
   */
  applyTheme() {
    const theme = this.getTheme();
    const root = document.documentElement;

    // Apply colors
    Object.entries(theme.colors).forEach(([key, value]) => {
      if (typeof value === 'object') {
        // Handle nested objects like text colors
        Object.entries(value).forEach(([subKey, subValue]) => {
          root.style.setProperty(`--color-${key}-${subKey}`, subValue);
        });
      } else {
        root.style.setProperty(`--color-${key}`, value);
      }
    });
  }

  /**
   * Generate CSS custom properties from configuration
   * @returns {string} CSS string with custom properties
   */
  generateCSS() {
    const theme = this.getTheme();
    let css = ':root {\n';

    // Add colors
    Object.entries(theme.colors).forEach(([key, value]) => {
      if (typeof value === 'object') {
        Object.entries(value).forEach(([subKey, subValue]) => {
          css += `  --color-${key}-${subKey}: ${subValue};\n`;
        });
      } else {
        css += `  --color-${key}: ${value};\n`;
      }
    });

    // Add spacing
    Object.entries(this.config.spacing.scale).forEach(([key, value]) => {
      css += `  --spacing-${key}: ${value};\n`;
    });

    css += '}\n';
    return css;
  }

  /**
   * Get saved theme preference from localStorage
   * @returns {string} Saved theme name or default 'light'
   */
  static getSavedTheme() {
    return localStorage.getItem('theme') || 'light';
  }

  /**
   * Initialize theme from saved preference
   */
  initializeTheme() {
    const savedTheme = BrandingManager.getSavedTheme();
    this.setTheme(savedTheme);
  }

  /**
   * Export configuration as JSON
   * @returns {string} JSON string
   */
  exportConfig() {
    return JSON.stringify(this.config, null, 2);
  }

  /**
   * Get all available themes
   * @returns {Array} Array of theme names
   */
  getAvailableThemes() {
    return Object.keys(this.config.themes);
  }

  /**
   * Validate color contrast for accessibility
   * @param {string} foreground - Foreground color (hex)
   * @param {string} background - Background color (hex)
   * @returns {Object} Contrast ratio and WCAG compliance
   */
  static checkColorContrast(foreground, background) {
    // Convert hex to RGB
    const hexToRgb = (hex) => {
      const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
      return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
      } : null;
    };

    // Calculate relative luminance
    const getLuminance = (rgb) => {
      const [r, g, b] = [rgb.r, rgb.g, rgb.b].map(val => {
        val = val / 255;
        return val <= 0.03928 ? val / 12.92 : Math.pow((val + 0.055) / 1.055, 2.4);
      });
      return 0.2126 * r + 0.7152 * g + 0.0722 * b;
    };

    const fg = hexToRgb(foreground);
    const bg = hexToRgb(background);

    if (!fg || !bg) {
      return { error: 'Invalid color format' };
    }

    const l1 = getLuminance(fg);
    const l2 = getLuminance(bg);
    const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);

    return {
      ratio: ratio.toFixed(2),
      AA: ratio >= 4.5,
      AAA: ratio >= 7,
      AALarge: ratio >= 3,
      AAALarge: ratio >= 4.5
    };
  }
}

// Export for use in Node.js or browsers
if (typeof module !== 'undefined' && module.exports) {
  module.exports = BrandingManager;
} else if (typeof window !== 'undefined') {
  window.BrandingManager = BrandingManager;
}
