"""Unit tests for changelog_utils SharedLayer module."""

from unittest.mock import MagicMock, patch

from changelog_utils import _strip_sensitive, _extract_admin, log_admin_change, log_audit_event


class TestStripSensitive:
    def test_removes_password(self):
        data = {"email": "a@b.com", "password": "secret123", "name": "Test"}
        result = _strip_sensitive(data)
        assert "password" not in result
        assert result["email"] == "a@b.com"
        assert result["name"] == "Test"

    def test_removes_multiple_sensitive(self):
        data = {"token": "abc", "secret": "xyz", "name": "ok"}
        result = _strip_sensitive(data)
        assert "token" not in result
        assert "secret" not in result
        assert result["name"] == "ok"

    def test_empty_dict(self):
        assert _strip_sensitive({}) == {}

    def test_none_returns_empty(self):
        assert _strip_sensitive(None) == {}


class TestExtractAdmin:
    def test_extracts_from_authorizer(self):
        event = {"requestContext": {"authorizer": {"user_id": "u1", "username": "admin"}}}
        uid, uname = _extract_admin(event)
        assert uid == "u1"
        assert uname == "admin"

    def test_defaults_to_system(self):
        uid, uname = _extract_admin({})
        assert uid == "system"
        assert uname == "system"


class TestLogAdminChange:
    @patch("changelog_utils._get_table")
    def test_writes_entry(self, mock_get_table):
        mock_table = MagicMock()
        mock_get_table.return_value = mock_table

        event = {"requestContext": {"authorizer": {"user_id": "u1", "username": "admin"}}}
        log_admin_change(event, "project", "p1", "create", data={"name": "Test"}, entity_name="Test Project")

        mock_table.put_item.assert_called_once()
        item = mock_table.put_item.call_args[1]["Item"]
        assert item["entity_type"] == "project"
        assert item["action"] == "create"
        assert item["admin_username"] == "admin"
        assert item["entity_name"] == "Test Project"

    @patch("changelog_utils._get_table")
    def test_fire_and_forget_on_error(self, mock_get_table):
        mock_table = MagicMock()
        mock_table.put_item.side_effect = Exception("DDB error")
        mock_get_table.return_value = mock_table

        # Should not raise
        log_admin_change({}, "user", "u1", "delete")

    @patch("changelog_utils._get_table")
    def test_no_table_returns_silently(self, mock_get_table):
        mock_get_table.return_value = None
        log_admin_change({}, "user", "u1", "create")  # Should not raise


class TestLogAuditEvent:
    @patch("changelog_utils._get_table")
    def test_writes_login_event(self, mock_get_table):
        mock_table = MagicMock()
        mock_get_table.return_value = mock_table

        log_audit_event("login_attempt", "admin", "login_success", username="admin")

        mock_table.put_item.assert_called_once()
        item = mock_table.put_item.call_args[1]["Item"]
        assert item["entity_type"] == "login_attempt"
        assert item["action"] == "login_success"
        assert item["admin_username"] == "admin"
