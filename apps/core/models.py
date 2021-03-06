from enum import Enum

from django.db import models
from django.utils import timezone
from django_enum_choices.fields import EnumChoiceField

from apps.core.managers import BaseManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = BaseManager()
    all_objects = BaseManager(alive_only=False)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()


class Permission(BaseModel):
    class Meta:
        db_table = 'permissions'
        app_label = 'core'

    title = models.CharField(max_length=100, unique=True)


class Role(BaseModel):
    class Meta:
        db_table = 'roles'
        app_label = 'core'

    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission, db_table='role_permissions')

    def __str__(self) -> str:
        return self.name


class Party(BaseModel):
    class Meta:
        db_table = 'parties'
        app_label = 'core'

    class PartyEnum(Enum):
        NAZI = 'nazi'
        LIBERAL = 'liberals'
        POPULIST = 'populists'
        COMMUNIST = 'communists'
        CONSERVATIVES = 'conservatives'
        SOCIALISTS = 'socialists'
        NATIONALISTS = 'nationalists'
        DEMOCRATS = 'democrats'

    name = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=15, null=True)
    type = EnumChoiceField(PartyEnum, null=True)
    founded_at = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name


class Government(BaseModel):
    class Meta:
        db_table = 'governments'
        app_label = 'core'

    started_at = models.DateField()
    end_at = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.started_at} - {self.end_at}"


class Member(BaseModel):
    class Meta:
        db_table = 'members'
        app_label = 'core'

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    born_at = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname} ({self.born_at})"


class GovernmentMember(BaseModel):
    class Meta:
        db_table = 'government_members'
        app_label = 'core'

    government = models.ForeignKey(Government, on_delete=models.CASCADE, related_name='government_members')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='government_members')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='government_members')
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='government_members')

    def __str__(self):
        return f"{self.member} is member of {self.government} for party {self.party} as {self.role}"


class InboxMessage(BaseModel):
    class Meta:
        db_table = 'inbox'
        app_label = 'core'

    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='messages')
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_fake = models.BooleanField(default=False)
    published_at = models.DateTimeField()

