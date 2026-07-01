from rest_framework.permissions import BasePermission
from Passenger.models import User_war_struck
from typing import Literal

class IsInspectorMember(BasePermission):
    def has_permission(self, request, view)-> Literal[True] | bool:
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # بررسی وضعیت owner یا inspector بودن
        try:
            passenger = User_war_struck.objects.get(user=user)
            return passenger.Is_inspector or passenger.Is_owner
        except User_war_struck.DoesNotExist:
            return False