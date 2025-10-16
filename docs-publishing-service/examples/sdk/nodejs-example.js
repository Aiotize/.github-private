/**
 * Node.js SDK Example for Documentation Publishing Service
 * 
 * This example demonstrates how to use the Documentation Publishing Service
 * from a Node.js application.
 */

const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');

// Configuration
const config = {
  apiUrl: process.env.DOCS_API_URL || 'https://api.docs-publishing.example.com/v1',
  apiKey: process.env.DOCS_API_KEY,
  brand: process.env.BRAND || 'example-brand',
};

// Validate configuration
if (!config.apiKey) {
  throw new Error('DOCS_API_KEY environment variable is required');
}

/**
 * Documentation Publishing Client
 */
class DocsPublishingClient {
  constructor(config) {
    this.config = config;
    this.client = axios.create({
      baseURL: config.apiUrl,
      headers: {
        'Authorization': `Bearer ${config.apiKey}`,
        'Content-Type': 'application/json',
      },
    });
  }

  /**
   * Publish a document
   */
  async publish(options) {
    try {
      const response = await this.client.post('/publish', {
        ...options,
        brand: options.brand || this.config.brand,
      });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Publish from a file
   */
  async publishFile(filePath, options = {}) {
    let content;
    try {
      content = await fs.readFile(filePath, 'utf-8');
    } catch (error) {
      throw new Error(`Failed to read file ${filePath}: ${error.message}`);
    }
    const fileName = path.basename(filePath, path.extname(filePath));
    
    // Extract metadata from frontmatter if present
    const metadata = this.extractFrontmatter(content);
    
    return this.publish({
      content,
      format: options.format || 'markdown',
      brand: options.brand || this.config.brand,
      category: options.category || metadata.category || 'general',
      metadata: {
        title: options.title || metadata.title || fileName,
        author: options.author || metadata.author,
        version: options.version || metadata.version || '1.0.0',
        ...metadata,
      },
      options: {
        validate: true,
        transform: true,
        publish: true,
        ...options.publishOptions,
      },
    });
  }

  /**
   * Validate a document
   */
  async validate(content, format = 'markdown', brand = null) {
    try {
      const response = await this.client.post('/validate', {
        content,
        format,
        brand: brand || this.config.brand,
      });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Transform document format
   */
  async transform(content, from, to, options = {}) {
    try {
      const response = await this.client.post('/transform', {
        content,
        from,
        to,
        options: {
          brand: options.brand || this.config.brand,
          apply_styles: options.applyStyles !== false,
          include_toc: options.includeToc !== false,
        },
      });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Get a document by ID
   */
  async getDocument(id) {
    try {
      const response = await this.client.get(`/documents/${id}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * List documents
   */
  async listDocuments(filters = {}) {
    try {
      const response = await this.client.get('/documents', {
        params: {
          brand: filters.brand || this.config.brand,
          category: filters.category,
          status: filters.status,
          page: filters.page || 1,
          limit: filters.limit || 20,
        },
      });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Update a document
   */
  async updateDocument(id, updates) {
    try {
      const response = await this.client.put(`/documents/${id}`, updates);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Delete a document
   */
  async deleteDocument(id) {
    try {
      const response = await this.client.delete(`/documents/${id}`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Get brand configuration
   */
  async getBrandConfig(brand = null) {
    try {
      const brandId = brand || this.config.brand;
      const response = await this.client.get(`/brands/${brandId}/config`);
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * List available brands
   */
  async listBrands() {
    try {
      const response = await this.client.get('/brands');
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Extract frontmatter from markdown content
   * 
   * NOTE: This is a simplified parser for demonstration.
   * For production use, install and use a proper YAML parser:
   *   npm install js-yaml
   * Then use: const yaml = require('js-yaml'); yaml.load(frontmatter);
   */
  extractFrontmatter(content) {
    const frontmatterRegex = /^---\n([\s\S]*?)\n---/;
    const match = content.match(frontmatterRegex);
    
    if (!match) return {};
    
    const frontmatter = match[1];
    const metadata = {};
    
    // Simple YAML parser for basic key-value pairs only
    // Does not handle arrays, nested objects, or multi-line values
    const lines = frontmatter.split('\n');
    lines.forEach(line => {
      const colonIndex = line.indexOf(':');
      if (colonIndex > 0 && !line.trim().startsWith('#')) {
        const key = line.substring(0, colonIndex).trim();
        let value = line.substring(colonIndex + 1).trim();
        // Remove surrounding quotes if present
        if ((value.startsWith('"') && value.endsWith('"')) || 
            (value.startsWith("'") && value.endsWith("'"))) {
          value = value.substring(1, value.length - 1);
        }
        metadata[key] = value;
      }
    });
    
    return metadata;
  }

  /**
   * Handle API errors
   */
  handleError(error) {
    if (error.response) {
      const apiError = new Error(
        error.response.data.error?.message || 'API request failed'
      );
      apiError.statusCode = error.response.status;
      apiError.code = error.response.data.error?.code;
      apiError.details = error.response.data.error?.details;
      return apiError;
    }
    return error;
  }
}

// ============================================================================
// Usage Examples
// ============================================================================

async function examples() {
  const client = new DocsPublishingClient(config);

  // Example 1: Publish a simple document
  console.log('\n=== Example 1: Publishing a document ===');
  try {
    const result = await client.publish({
      content: '# Hello World\n\nThis is a test document.',
      format: 'markdown',
      category: 'guides',
      metadata: {
        title: 'Hello World Guide',
        author: 'Documentation Team',
        version: '1.0.0',
      },
    });
    console.log('Published:', result.id);
    console.log('URL:', result.url);
  } catch (error) {
    console.error('Error:', error.message);
  }

  // Example 2: Publish from a file
  console.log('\n=== Example 2: Publishing from file ===');
  try {
    const result = await client.publishFile('./docs/getting-started.md', {
      category: 'tutorials',
      author: 'John Doe',
    });
    console.log('Published from file:', result.id);
  } catch (error) {
    console.error('Error:', error.message);
  }

  // Example 3: Validate before publishing
  console.log('\n=== Example 3: Validating a document ===');
  try {
    const validation = await client.validate(
      '# Test Document\n\nSome content here.'
    );
    console.log('Validation passed:', validation.valid);
    console.log('Quality score:', validation.score);
    if (validation.warnings.length > 0) {
      console.log('Warnings:', validation.warnings.length);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }

  // Example 4: Transform document format
  console.log('\n=== Example 4: Transforming document ===');
  try {
    const result = await client.transform(
      '# Markdown Document\n\nWith **bold** text.',
      'markdown',
      'html',
      { applyStyles: true }
    );
    console.log('Transformed to HTML (first 100 chars):');
    console.log(result.content.substring(0, 100) + '...');
  } catch (error) {
    console.error('Error:', error.message);
  }

  // Example 5: List documents
  console.log('\n=== Example 5: Listing documents ===');
  try {
    const documents = await client.listDocuments({
      category: 'guides',
      status: 'published',
      limit: 5,
    });
    console.log(`Found ${documents.pagination.total} documents`);
    documents.documents.forEach(doc => {
      console.log(`- ${doc.title} (${doc.id})`);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }

  // Example 6: Get brand configuration
  console.log('\n=== Example 6: Getting brand config ===');
  try {
    const brandConfig = await client.getBrandConfig();
    console.log('Brand:', brandConfig.brand);
    console.log('Categories:', brandConfig.categories.join(', '));
  } catch (error) {
    console.error('Error:', error.message);
  }

  // Example 7: Batch publish multiple files
  console.log('\n=== Example 7: Batch publishing ===');
  const files = ['doc1.md', 'doc2.md', 'doc3.md'];
  
  try {
    const results = await Promise.all(
      files.map(file => 
        client.publishFile(`./docs/${file}`, { category: 'guides' })
          .catch(err => ({ error: err.message, file }))
      )
    );
    
    const successful = results.filter(r => !r.error);
    const failed = results.filter(r => r.error);
    
    console.log(`Published ${successful.length} documents`);
    if (failed.length > 0) {
      console.log(`Failed: ${failed.length}`);
      failed.forEach(f => console.log(`  - ${f.file}: ${f.error}`));
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Run examples if this file is executed directly
if (require.main === module) {
  examples()
    .then(() => {
      console.log('\nAll examples completed!');
      process.exit(0);
    })
    .catch(error => {
      console.error('Fatal error:', error);
      process.exit(1);
    });
}

// Export client for use as a module
module.exports = { DocsPublishingClient };
