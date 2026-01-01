class CustomFieldsModule:
    def __init__(self, client):
        self.client = client

    def list(self, shop_id: int | str):
        """Retrieve all custom fields"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/custom-fields",
        )

    def create(
        self,
        shop_id: int | str,
        name: str,
        type: str,
        placeholder: str | None = None,
        hint: str | None = None,
        options: str | None = None,
        default: str | None = None,
        regex: str | None = None,
        is_required: bool | None = None,
    ):
        """Create a new custom field"""
        body = {
            "name": name,
            "type": type,
        }

        optional_fields = {
            "placeholder": placeholder,
            "hint": hint,
            "options": options,
            "default": default,
            "regex": regex,
            "is_required": is_required,
        }

        for k, v in optional_fields.items():
            if v is not None:
                body[k] = v

        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/custom-fields",
            data=body,
        )

    def update(
        self,
        shop_id: int | str,
        custom_field_id: str,
        name: str,
        type: str,
        placeholder: str | None = None,
        hint: str | None = None,
        options: str | None = None,
        default: str | None = None,
        regex: str | None = None,
        is_required: bool | None = None,
    ):
        """Update an existing custom field"""
        body = {
            "name": name,
            "type": type,
        }

        optional_fields = {
            "placeholder": placeholder,
            "hint": hint,
            "options": options,
            "default": default,
            "regex": regex,
            "is_required": is_required,
        }

        for k, v in optional_fields.items():
            if v is not None:
                body[k] = v

        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/custom-fields/{custom_field_id}",
            data=body,
        )

    def delete(self, shop_id: int | str, custom_field_id: str):
        """Delete a custom field"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/custom-fields/{custom_field_id}",
        )
