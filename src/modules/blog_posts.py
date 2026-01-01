class BlogPostsModule:
    def __init__(self, client):
        self.client = client

    def list(
        self,
        shop_id: int | str,
        page: int | None = None,
        per_page: int | None = None,
        order_column: str | None = None,
        order_direction: str | None = None,
        title: str | None = None,
    ):
        """
        Get blog posts with optional filters and pagination.
        GET /v1/shops/{shop_id}/blog-posts
        """
        data = {}
        if page is not None:
            data["page"] = page
        if per_page is not None:
            data["perPage"] = per_page
        if order_column is not None:
            data["orderColumn"] = order_column
        if order_direction is not None:
            data["orderDirection"] = order_direction
        if title is not None:
            data["title"] = title

        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/blog-posts",
            data=data if data else None,
        )

    def get(self, shop_id: int | str, blog_post_id: str):
        """Retrieve a specific blog post"""
        return self.client.request(
            method="GET",
            endpoint=f"/v1/shops/{shop_id}/blog-posts/{blog_post_id}",
        )

    def create(
        self,
        shop_id: int | str,
        title: str,
        content: str,
        path: str | None = None,
        summary: str | None = None,
        image_id: str | None = None,
        meta_title: str | None = None,
        meta_description: str | None = None,
    ):
        """Create a new blog post"""
        body = {
            "title": title,
            "content": content,
        }

        if path is not None:
            body["path"] = path
        if summary is not None:
            body["summary"] = summary
        if image_id is not None:
            body["image_id"] = image_id
        if meta_title is not None:
            body["meta_title"] = meta_title
        if meta_description is not None:
            body["meta_description"] = meta_description

        return self.client.request(
            method="POST",
            endpoint=f"/v1/shops/{shop_id}/blog-posts",
            data=body,
        )

    def update(
        self,
        shop_id: int | str,
        blog_post_id: str,
        title: str,
        content: str,
        path: str | None = None,
        summary: str | None = None,
        image_id: str | None = None,
        meta_title: str | None = None,
        meta_description: str | None = None,
    ):
        """Update a blog post"""
        body = {
            "id": blog_post_id,
            "title": title,
            "content": content,
        }

        if path is not None:
            body["path"] = path
        if summary is not None:
            body["summary"] = summary
        if image_id is not None:
            body["image_id"] = image_id
        if meta_title is not None:
            body["meta_title"] = meta_title
        if meta_description is not None:
            body["meta_description"] = meta_description

        return self.client.request(
            method="PUT",
            endpoint=f"/v1/shops/{shop_id}/blog-posts/{blog_post_id}",
            data=body,
        )

    def delete(self, shop_id: int | str, blog_post_id: str):
        """Delete a blog post"""
        return self.client.request(
            method="DELETE",
            endpoint=f"/v1/shops/{shop_id}/blog-posts/{blog_post_id}",
        )
