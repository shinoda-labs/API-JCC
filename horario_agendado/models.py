from django.db import models
from usuario.models import Usuario
from horario.models import Horario
from servico.models import Servico


class HorarioAgendado(models.Model):
    class Meta:
        db_table = 'tb_horario_agendado'

    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, editable=False)
    data = models.DateField()
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    criado = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)
    status = models.IntegerField(default=0)

    database = 'db_jcc'

    def __str__(self):
        return self.id
