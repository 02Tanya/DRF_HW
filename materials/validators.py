from rest_framework import serializers


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val and "youtube.com" not in val:
            raise serializers.ValidationError(
                "Your link should be only from youtube.com"
            )
