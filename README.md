# .github-private

## Aiotize Brand & Design System

This repository contains the comprehensive branding and design system configuration for Aiotize, including custom layouts, themes, typography, spacing, and imagery guidelines.

## Features

### 🎨 Custom Themes
- **Light Theme**: Clean, bright design for optimal readability
- **Dark Theme**: Reduced eye strain with elegant dark colors
- **Custom Theme**: Branded theme with custom color palettes

### 📝 Typography System
- Hierarchical heading styles (h1-h6) with automatic numbering
- Multiple font families: Inter (primary), Montserrat (display), Georgia (secondary), Fira Code (monospace)
- Comprehensive font size and weight scales
- Configurable line heights for different content types

### 📐 Layout & Spacing
- Consistent spacing scale based on 0.25rem units
- Responsive container sizes (sm, md, lg, xl, 2xl)
- Standardized margins and padding
- Sticky header and footer configurations

### 🔗 Hyperlinks & Navigation
- Styled hyperlinks with hover, visited, and active states
- Accessibility-focused design with proper focus indicators
- Configurable underline styles and colors

### 🔢 Numbering Systems
- Automatic heading numbering (1.1, 1.2, etc.)
- Figure and table numbering
- Ordered and unordered list styles

### 🖼️ Imagery Guidelines
- Standard lens parameters (focal length, aperture, perspective)
- Tone configurations (professional, friendly, dramatic)
- Warmth settings (cool, neutral, warm)
- Aspect ratios for different use cases (16:9, 4:3, 1:1, etc.)
- Image optimization guidelines

### 📊 Color Palettes
- Primary, secondary, and accent colors
- Semantic colors (success, warning, error, info)
- Theme-specific color variations
- Comprehensive brand color scales

## Files

- **`branding-config.json`**: Complete branding configuration in JSON format
- **`styles.css`**: CSS implementation of the design system
- **`example.html`**: Live demonstration of all branding features

## Usage

### Using the Design System

1. **Include the stylesheet in your HTML:**
   ```html
   <link rel="stylesheet" href="styles.css">
   ```

2. **Set the theme (optional):**
   ```html
   <html data-theme="light">  <!-- or "dark" or "custom" -->
   ```

3. **Enable heading numbering (optional):**
   ```html
   <body class="numbered-headings numbered-figures numbered-tables">
   ```

4. **Use semantic HTML with provided classes:**
   ```html
   <div class="container">
     <section>
       <h1>Your Content</h1>
       <p>Your text...</p>
     </section>
   </div>
   ```

### Viewing the Example

Open `example.html` in a web browser to see a live demonstration of:
- All three themes with theme switcher
- Typography hierarchy
- Color palettes
- Spacing and layout
- Hyperlink styles
- Lists and numbering
- Imagery guidelines
- UI components (buttons, cards, tables)
- Topic chronology structure

### Using the Configuration

The `branding-config.json` file can be imported into your build tools or applications:

```javascript
// JavaScript/Node.js
const brandingConfig = require('./branding-config.json');
const primaryColor = brandingConfig.themes.light.colors.primary;
```

```python
# Python
import json
with open('branding-config.json') as f:
    config = json.load(f)
    primary_color = config['themes']['light']['colors']['primary']
```

## Customization

### Modifying Themes

Edit `branding-config.json` to customize colors, typography, spacing, or any other aspect of the design system. The CSS file uses CSS variables that automatically adapt to theme changes.

### Adding New Themes

Add new theme configurations to the `themes` object in `branding-config.json`:

```json
{
  "themes": {
    "myTheme": {
      "name": "My Custom Theme",
      "colors": {
        "primary": "#YOUR_COLOR",
        ...
      }
    }
  }
}
```

### Extending the CSS

The CSS file is organized into sections:
- CSS Variables (theme definitions)
- Base Styles
- Typography
- Layout
- Components
- Utilities

Add custom styles in any section while maintaining the existing structure.

## Design Principles

1. **Consistency**: All elements follow the same spacing, color, and typography rules
2. **Accessibility**: WCAG compliant colors, focus states, and semantic HTML
3. **Responsiveness**: Mobile-first design with adaptive layouts
4. **Scalability**: Modular system that grows with your needs
5. **Maintainability**: Clear documentation and organized code structure

## Topic Chronology

Content should follow this chronological structure:

1. **Introduction**: Overview, objectives, scope
2. **Main Content**: Context, details, examples, analysis
3. **Conclusion**: Summary, takeaways, next steps

This ensures optimal comprehension and navigation through content.

## License

MIT License - See [LICENSE](LICENSE) file for details.
**Author:** Aiotize Organization  
**Maintainer:** Aiotize Team  
**License:** MIT  
**Created:** 2025  

## Overview

This repository contains default community health files and organization-wide configurations for the Aiotize organization.

## Purpose

The `.github-private` repository serves as a centralized location for:
- Community health files
- Issue and PR templates
- Workflow configurations
- Organization standards and guidelines

## File Structure

```
.github-private/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml       # Bug report template with metadata
│   │   ├── feature_request.yml  # Feature request template
│   │   └── config.yml           # Issue template configuration
│   ├── PULL_REQUEST_TEMPLATE.md # PR template with metadata
│   ├── STYLE_GUIDE.md           # Comprehensive style guide
│   └── STANDARDS_SUMMARY.md     # Quick reference guide
├── README.md           # This file
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
├── CODEOWNERS          # Code ownership with author credentials
├── CODE_OF_CONDUCT.md  # Community guidelines with metadata
├── CONTRIBUTING.md     # Contribution guidelines with standards
└── SECURITY.md         # Security policy with metadata
```

## Metadata

- **Repository Type:** Organization Configuration
- **Visibility:** Private
- **Language:** Markdown
- **Framework:** GitHub Community Standards

## Standards and Guidelines

This repository establishes organization-wide standards for:

### Author Credentials
- All files include proper author attribution
- Metadata includes creation and modification dates
- Version tracking for all documents

### Text Formatting Standards
- **Standard text size:** 14-16px (web) / 11-12pt (documents)
- **Text intensity:** WCAG AA compliant (4.5:1 contrast ratio minimum)
- **Headers:** Hierarchical structure (H1: 32-36px, H2: 24-28px, H3: 20-24px)
- **Line height:** 1.5-1.6 for optimal readability

### Quick Reference
- **[Style Guide](.github/STYLE_GUIDE.md)** - Complete formatting and metadata standards
- **[Standards Summary](.github/STANDARDS_SUMMARY.md)** - Quick reference for common standards
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute with proper metadata
- **[Code of Conduct](CODE_OF_CONDUCT.md)** - Community guidelines

## Contact

For questions or issues, please contact the Aiotize team.

---

© 2025 Aiotize. All rights reserved.