"""API routes for nes2.

This module contains all API endpoint route definitions organized by resource type:
- entities: Entity search, retrieval, and filtering endpoints
- relationships: Relationship search and query endpoints
- schemas: Entity and relationship type discovery endpoints
- health: Health check and status endpoints
"""

from . import entities, health, relationships, schemas

__all__ = ["entities", "relationships", "schemas", "health"]
