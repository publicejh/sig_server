from rest_framework import generics
from sigs.models import Sig, SigParticipate
from .serializers import SigSerializer


class SigList(generics.ListAPIView):
    queryset = Sig.objects.all()
    serializer_class = SigSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        sig_id_list = []

        for sig_obj in SigParticipate.get_participated_sigs(user_id):
            sig_id_list.append(sig_obj.sig_id)
        queryset = Sig.objects.filter(id__in=sig_id_list)

        return queryset


class SigRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sig.objects.all()
    serializer_class = SigSerializer
