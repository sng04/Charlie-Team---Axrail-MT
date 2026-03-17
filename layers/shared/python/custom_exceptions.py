"""Custom exception hierarchy mapped to HTTP status codes."""


class BadRequestError(Exception):
    """400 — Missing or invalid input."""
    pass


class UnauthorizedError(Exception):
    """401 — Missing or invalid auth token."""
    pass


class ForbiddenError(Exception):
    """403 — Authenticated but insufficient permissions."""
    pass


class NotFoundError(Exception):
    """404 — Resource doesn't exist."""
    pass


class ConflictError(Exception):
    """409 — Duplicate or concurrent modification."""
    pass
