from rest_framework import mixins


class UpdateDeleteViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    def perform_update(self, serializer):
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
