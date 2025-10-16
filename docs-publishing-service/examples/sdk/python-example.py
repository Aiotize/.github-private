"""
Python SDK Example for Documentation Publishing Service

This example demonstrates how to use the Documentation Publishing Service
from a Python application.
"""

import os
import re
import json
from typing import Dict, List, Optional, Any
from pathlib import Path

import requests
from requests.exceptions import RequestException


class DocsPublishingClient:
    """Client for Documentation Publishing Service API"""

    def __init__(
        self,
        api_key: str,
        api_url: str = "https://api.docs-publishing.example.com/v1",
        brand: str = "example-brand",
    ):
        """
        Initialize the client.

        Args:
            api_key: API authentication key
            api_url: Base URL for the API
            brand: Default brand identifier
        """
        if not api_key:
            raise ValueError("API key is required")

        self.api_url = api_url.rstrip("/")
        self.brand = brand
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
        )

    def publish(
        self,
        content: str = None,
        source: str = None,
        format: str = "markdown",
        category: str = "general",
        metadata: Dict[str, Any] = None,
        brand: str = None,
        options: Dict[str, bool] = None,
    ) -> Dict[str, Any]:
        """
        Publish a document.

        Args:
            content: Document content (alternative to source)
            source: Path or URL to source document
            format: Document format (markdown, html, rst, etc.)
            category: Documentation category
            metadata: Document metadata
            brand: Brand identifier (uses default if not specified)
            options: Publishing options

        Returns:
            Dictionary with publication result
        """
        payload = {
            "format": format,
            "brand": brand or self.brand,
            "category": category,
            "metadata": metadata or {},
            "options": options
            or {"validate": True, "transform": True, "publish": True},
        }

        if content:
            payload["content"] = content
        elif source:
            payload["source"] = source
        else:
            raise ValueError("Either content or source must be provided")

        response = self._request("POST", "/publish", json=payload)
        return response.json()

    def publish_file(
        self,
        file_path: str,
        category: str = None,
        metadata: Dict[str, Any] = None,
        brand: str = None,
    ) -> Dict[str, Any]:
        """
        Publish a document from a file.

        Args:
            file_path: Path to the document file
            category: Documentation category
            metadata: Additional metadata
            brand: Brand identifier

        Returns:
            Dictionary with publication result
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        content = path.read_text(encoding="utf-8")
        file_metadata = self._extract_frontmatter(content)

        # Merge metadata
        final_metadata = {
            "title": path.stem.replace("-", " ").title(),
            **file_metadata,
            **(metadata or {}),
        }

        return self.publish(
            content=content,
            format=path.suffix.lstrip(".") or "markdown",
            category=category or file_metadata.get("category", "general"),
            metadata=final_metadata,
            brand=brand,
        )

    def validate(
        self, content: str, format: str = "markdown", brand: str = None
    ) -> Dict[str, Any]:
        """
        Validate a document without publishing.

        Args:
            content: Document content
            format: Document format
            brand: Brand identifier

        Returns:
            Dictionary with validation results
        """
        payload = {
            "content": content,
            "format": format,
            "brand": brand or self.brand,
        }

        response = self._request("POST", "/validate", json=payload)
        return response.json()

    def transform(
        self,
        content: str,
        from_format: str,
        to_format: str,
        brand: str = None,
        apply_styles: bool = True,
        include_toc: bool = True,
    ) -> Dict[str, Any]:
        """
        Transform a document from one format to another.

        Args:
            content: Document content
            from_format: Source format
            to_format: Target format
            brand: Brand identifier
            apply_styles: Whether to apply brand styles
            include_toc: Whether to include table of contents

        Returns:
            Dictionary with transformed content
        """
        payload = {
            "content": content,
            "from": from_format,
            "to": to_format,
            "options": {
                "brand": brand or self.brand,
                "apply_styles": apply_styles,
                "include_toc": include_toc,
            },
        }

        response = self._request("POST", "/transform", json=payload)
        return response.json()

    def get_document(self, doc_id: str) -> Dict[str, Any]:
        """
        Get a document by ID.

        Args:
            doc_id: Document identifier

        Returns:
            Dictionary with document details
        """
        response = self._request("GET", f"/documents/{doc_id}")
        return response.json()

    def list_documents(
        self,
        brand: str = None,
        category: str = None,
        status: str = None,
        page: int = 1,
        limit: int = 20,
    ) -> Dict[str, Any]:
        """
        List documents with optional filtering.

        Args:
            brand: Filter by brand
            category: Filter by category
            status: Filter by status
            page: Page number
            limit: Items per page

        Returns:
            Dictionary with documents list and pagination
        """
        params = {
            "brand": brand or self.brand,
            "page": page,
            "limit": limit,
        }

        if category:
            params["category"] = category
        if status:
            params["status"] = status

        response = self._request("GET", "/documents", params=params)
        return response.json()

    def update_document(
        self, doc_id: str, updates: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update an existing document.

        Args:
            doc_id: Document identifier
            updates: Updates to apply

        Returns:
            Dictionary with updated document
        """
        response = self._request("PUT", f"/documents/{doc_id}", json=updates)
        return response.json()

    def delete_document(self, doc_id: str) -> Dict[str, Any]:
        """
        Delete a document.

        Args:
            doc_id: Document identifier

        Returns:
            Dictionary with deletion confirmation
        """
        response = self._request("DELETE", f"/documents/{doc_id}")
        return response.json()

    def get_brand_config(self, brand: str = None) -> Dict[str, Any]:
        """
        Get brand configuration.

        Args:
            brand: Brand identifier

        Returns:
            Dictionary with brand configuration
        """
        brand_id = brand or self.brand
        response = self._request("GET", f"/brands/{brand_id}/config")
        return response.json()

    def list_brands(self) -> Dict[str, Any]:
        """
        List available brands.

        Returns:
            Dictionary with brands list
        """
        response = self._request("GET", "/brands")
        return response.json()

    def _request(
        self, method: str, endpoint: str, **kwargs
    ) -> requests.Response:
        """
        Make an API request.

        Args:
            method: HTTP method
            endpoint: API endpoint
            **kwargs: Additional arguments for requests

        Returns:
            Response object

        Raises:
            RequestException: If request fails
        """
        url = f"{self.api_url}{endpoint}"

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except RequestException as e:
            if e.response is not None:
                try:
                    error_data = e.response.json()
                    error_msg = error_data.get("error", {}).get(
                        "message", str(e)
                    )
                except json.JSONDecodeError:
                    error_msg = str(e)
                raise RequestException(f"API Error: {error_msg}") from e
            raise

    @staticmethod
    def _extract_frontmatter(content: str) -> Dict[str, str]:
        """
        Extract YAML frontmatter from content.

        Args:
            content: Document content

        Returns:
            Dictionary with frontmatter key-value pairs
        """
        pattern = r"^---\n(.*?)\n---"
        match = re.search(pattern, content, re.DOTALL)

        if not match:
            return {}

        frontmatter = match.group(1)
        metadata = {}

        for line in frontmatter.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip('"\'')

        return metadata


# ============================================================================
# Usage Examples
# ============================================================================


def main():
    """Run example usage"""

    # Initialize client
    api_key = os.getenv("DOCS_API_KEY")
    if not api_key:
        print("Error: DOCS_API_KEY environment variable not set")
        return

    client = DocsPublishingClient(
        api_key=api_key,
        brand=os.getenv("BRAND", "example-brand"),
    )

    # Example 1: Publish a simple document
    print("\n=== Example 1: Publishing a document ===")
    try:
        result = client.publish(
            content="# Hello World\n\nThis is a test document.",
            category="guides",
            metadata={
                "title": "Hello World Guide",
                "author": "Documentation Team",
                "version": "1.0.0",
            },
        )
        print(f"Published: {result['id']}")
        print(f"URL: {result['url']}")
    except Exception as e:
        print(f"Error: {e}")

    # Example 2: Validate before publishing
    print("\n=== Example 2: Validating a document ===")
    try:
        validation = client.validate("# Test Document\n\nSome content here.")
        print(f"Validation passed: {validation['valid']}")
        print(f"Quality score: {validation['score']}")
        if validation["warnings"]:
            print(f"Warnings: {len(validation['warnings'])}")
    except Exception as e:
        print(f"Error: {e}")

    # Example 3: Transform document format
    print("\n=== Example 3: Transforming document ===")
    try:
        result = client.transform(
            content="# Markdown Document\n\nWith **bold** text.",
            from_format="markdown",
            to_format="html",
            apply_styles=True,
        )
        print("Transformed to HTML (first 100 chars):")
        print(result["content"][:100] + "...")
    except Exception as e:
        print(f"Error: {e}")

    # Example 4: List documents
    print("\n=== Example 4: Listing documents ===")
    try:
        documents = client.list_documents(category="guides", limit=5)
        print(f"Found {documents['pagination']['total']} documents")
        for doc in documents["documents"]:
            print(f"- {doc['title']} ({doc['id']})")
    except Exception as e:
        print(f"Error: {e}")

    # Example 5: Get brand configuration
    print("\n=== Example 5: Getting brand config ===")
    try:
        config = client.get_brand_config()
        print(f"Brand: {config['brand']}")
        print(f"Categories: {', '.join(config['categories'])}")
    except Exception as e:
        print(f"Error: {e}")

    # Example 6: Batch publish multiple files
    print("\n=== Example 6: Batch publishing ===")
    files = ["doc1.md", "doc2.md", "doc3.md"]

    results = []
    for file_name in files:
        try:
            result = client.publish_file(f"./docs/{file_name}")
            results.append({"file": file_name, "id": result["id"]})
        except Exception as e:
            results.append({"file": file_name, "error": str(e)})

    successful = [r for r in results if "id" in r]
    failed = [r for r in results if "error" in r]

    print(f"Published {len(successful)} documents")
    if failed:
        print(f"Failed: {len(failed)}")
        for r in failed:
            print(f"  - {r['file']}: {r['error']}")

    print("\nAll examples completed!")


if __name__ == "__main__":
    main()
