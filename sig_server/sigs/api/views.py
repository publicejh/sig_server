from rest_framework import generics
from rest_framework.response import Response
from sigs.models import Sig, SigParticipate, SigInvitationToken
from .serializers import SigSerializer, SigParticipateSerializer, SigParticipateDetailSerializer,\
    SigInvitationTokenSerializer


class SigListCreateView(generics.ListCreateAPIView):
    queryset = Sig.objects.all()
    serializer_class = SigSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        sig_id_list = []

        for sig_obj in SigParticipate.get_participated_sigs(user_id):
            sig_id_list.append(sig_obj.sig_id)
        queryset = Sig.objects.filter(id__in=sig_id_list)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SigSerializer(queryset, many=True)
        return Response(serializer.data)


class SigRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sig.objects.all()
    serializer_class = SigSerializer


class SigParticipateCreateView(generics.CreateAPIView):
    queryset = SigParticipate
    serializer_class = SigParticipateSerializer


class SigParticipateListCreateView(generics.ListCreateAPIView):
    serializer_class = SigParticipateDetailSerializer
    lookup_field = 'sig_id'

    def get_queryset(self, **kwargs):
        sig_id = self.kwargs.get(self.lookup_field, None)
        queryset = SigParticipate.objects.filter(sig_id=sig_id)
        return queryset.order_by('-is_sig_leader')


class SigInvitationTokenCreateView(generics.CreateAPIView):
    queryset = SigInvitationToken
    serializer_class = SigInvitationTokenSerializer


class SigInvitationTokenRetrieveView(generics.RetrieveAPIView):
    queryset = SigInvitationToken.objects.all()
    serializer_class = SigInvitationTokenSerializer
    lookup_field = 'token'

    def get_queryset(self):
        queryset = SigInvitationToken.objects.all()
        token = self.kwargs.get(self.lookup_field, None)
        return queryset.filter(token=token)
