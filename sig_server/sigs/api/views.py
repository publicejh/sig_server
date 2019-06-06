from rest_framework import generics
from rest_framework.response import Response
from sigs.models import Sig, SigParticipate
from .serializers import SigSerializer, SigParticipateSerializer, SigParticipateDetailSerializer


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


class SigParticipateListView(generics.ListAPIView):
    # queryset = BandParticipate.objects.all()
    serializer_class = SigParticipateDetailSerializer
    lookup_field = 'sig_id'

    def get_queryset(self, **kwargs):
        sig_id = self.kwargs.get(self.lookup_field, None)
        queryset = SigParticipate.objects.filter(sig_id=sig_id)
        return queryset.order_by('-is_sig_leader')
