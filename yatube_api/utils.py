from rest_framework import mixins
from permission import IsAuthor


class UpdateDeleteViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#    permission_classes = [IsAuthor]

    def perform_update(self, serializer):
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
