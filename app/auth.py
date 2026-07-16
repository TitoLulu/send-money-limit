class AuthError(Exception):
    """Raised when a request is not authenticated."""


def build_context(session, request):
    """Build the GraphQL execution context for a request.

    Session tokens are validated by the edge auth layer, which forwards the
    already-authenticated user id on the ``X-User-Id`` header. We look that
    user up once here and stash it on the context. Resolvers should obtain the
    acting user via ``get_authenticated_user`` rather than reading the header
    (or any client-supplied id) themselves.
    """
    from .models import User

    context = {"session": session, "current_user": None}
    user_id = request.headers.get("X-User-Id")
    if user_id is not None:
        context["current_user"] = session.get(User, int(user_id))
    return context


def get_authenticated_user(info):
    """Return the authenticated ``User`` for this request, or raise.

    This is the only sanctioned way for a resolver to learn who is acting.
    The acting user is always derived from the validated session, never from
    a user id passed in the GraphQL arguments.
    """
    user = info.context.get("current_user")
    if user is None:
        raise AuthError("authentication required")
    return user
