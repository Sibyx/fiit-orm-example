from datetime import date
from typing import List

from django.db import connection, transaction
from django.db.models import Count, Q
from django.db.models.functions import Length

from apps.core.models import Member, Party


def select_all() -> List[Member]:
    """
    Select all users in table members using model Member
    :return:
    """
    # SELECT "members"."id", "members"."created_at", "members"."updated_at", "members"."deleted_at", "members"."name",
    # "members"."surname", "members"."born_at" FROM "members" WHERE "members"."deleted_at" IS NULL;
    members = Member.objects.all()
    return members


def select_one() -> Member:
    """
    Return exactly one member (if possible) with surname `Poliačik`
    :return:
    """
    member = Member.objects.get(name='Robert')
    return member


def select_first() -> Party:
    """
    Select first record from table parties
    :return:
    """
    return Party.objects.first()


def select_youngest() -> Member:
    """
    Select the youngest member of parliament ever
    :return:
    """
    return Member.objects.order_by('-born_at').first()


def create_party() -> Party:
    """
    Create party with name: `Friends of Douglas Adams`
    :return:
    """
    return Party.objects.create(
        name='Friends of Douglas Adams',
        color='darkblue'
    )


def party_exists() -> bool:
    """
    Is there a party with name `Združenie robotníkov Slovenska`?
    :return:
    """
    return Party.objects.filter(name='Združenie robotníkov Slovenska').exists()


def longest_party_name() -> str:
    party_name = Party.objects.annotate(
        name_length=Length('name')
    ).order_by('-name_length').first().name

    return party_name


def most_experienced_member() -> Member:
    member = Member.objects.annotate(
        experience=Count('government_members__id')
    ).order_by('-experience').first()

    return member


def communists_or_socialists() -> List[Party]:
    """
    Select all parties where type is SOCIALISTS or LIBERAL
    :return:
    """
    return Party.objects.filter(type__in=[Party.PartyEnum.SOCIALISTS, Party.PartyEnum.COMMUNIST])
    # return Party.objects.filter(
    #     Q(type=Party.PartyEnum.SOCIALISTS) | Q(type=Party.PartyEnum.COMMUNIST)
    # )


def communists_or_socialists_with_robo() -> List[Party]:
    """
    Select all parties with members named Robert
    :return:
    """
    pass


def best_tourist() -> Member:
    """
    Who often changes party?
    :return:
    """
    pass


def party_type_for_mazurek() -> str:
    """
    In what kind of party is member with last name `Mazurek`
    :return:
    """
    pass


def disco_members() -> List[Member]:
    """
    Which members born in 70'
    :return:
    """
    pass


def select_raw() -> List[dict]:
    """
    Execute raw select `SELECT * FROM parties;` and converts it to dictionary
    :return:
    """
    pass


def cleansing():
    """
    Delete all nazi party members inside of transaction and than throw exception
    :return:
    """
    with transaction.atomic():
        Member.objects.filter(government_members__party__type=Party.PartyEnum.NAZI).delete()
        raise Exception("We are better than them!")
