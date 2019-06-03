from django.db import models


class Sig(models.Model):
    name = models.CharField(max_length=45)
    cover_img_path = models.CharField(max_length=200)
    # members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='SigParticipate')

    def __str__(self):
        return self.name

    def members(self):
        return SigParticipate.objects.filter(sig=self)


class SigParticipate(models.Model):
    sig = models.ForeignKey('Sig', on_delete=models.CASCADE)
    user_id = models.IntegerField()
    is_sig_leader = models.BooleanField(default=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('sig', 'user_id', ), )

    def __str__(self):
        return 'user {} in sig {}'.format(self.user_id, self.sig)

    @classmethod
    def get_participated_sigs(cls, user_id):
        return cls.objects.filter(user_id=user_id).only('sig')


class SigInvitationToken(models.Model):
    sig = models.ForeignKey('Sig', on_delete=models.CASCADE)
    token = models.CharField(unique=True, max_length=45)

    def __str__(self):
        return self.token
