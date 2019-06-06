from rest_framework import serializers
from sigs.models import Sig, SigParticipate, SigInvitationToken
from sigs.views import get_user_detail


class SigSerializer(serializers.ModelSerializer):
    members = serializers.SerializerMethodField()

    # @staticmethod
    def get_members(self, obj):
        return SigParticipateSerializer(obj.members(), many=True).data

    class Meta:
        fields = ('id', 'name', 'cover_img_path', 'members', )
        model = Sig


class SigParticipateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = SigParticipate


class SigParticipateDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        user_detail = get_user_detail(obj.user_id)
        return user_detail['username']

    class Meta:
        fields = ('user_id', 'is_sig_leader', 'sig', 'username', )
        model = SigParticipate


class SigInvitationTokenSerializer(serializers.ModelSerializer):
    sig_name = serializers.SerializerMethodField()

    def get_sig_name(self, obj):
        return obj.sig.name

    class Meta:
        fields = ('id', 'token', 'sig', 'sig_name', )
        model = SigInvitationToken
