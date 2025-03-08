# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Usercredential(models.Model):

    #__Usercredential_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    ssh_port = models.IntegerField(null=True, blank=True)
    snmp_community = models.CharField(max_length=255, null=True, blank=True)
    snmp_version = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Usercredential_FIELDS__END

    class Meta:
        verbose_name        = _("Usercredential")
        verbose_name_plural = _("Usercredential")


class Deviceinventory(models.Model):

    #__Deviceinventory_FIELDS__
    user_credential = models.ForeignKey(UserCredential, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    type_of_office = models.CharField(max_length=255, null=True, blank=True)
    no_of_employees = models.IntegerField(null=True, blank=True)
    router_make_model = models.CharField(max_length=255, null=True, blank=True)
    type_of_device = models.CharField(max_length=255, null=True, blank=True)
    bandwidth = models.CharField(max_length=255, null=True, blank=True)
    cp_number = models.CharField(max_length=255, null=True, blank=True)
    lan_ip_address = models.CharField(max_length=255, null=True, blank=True)
    wan_ip_address = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_updated = models.DateTimeField(blank=True, null=True, default=timezone.now)
    device_name = models.CharField(max_length=255, null=True, blank=True)

    #__Deviceinventory_FIELDS__END

    class Meta:
        verbose_name        = _("Deviceinventory")
        verbose_name_plural = _("Deviceinventory")


class Devicestats(models.Model):

    #__Devicestats_FIELDS__
    device = models.ForeignKey(DeviceInventory, on_delete=models.CASCADE)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    uptime = models.CharField(max_length=255, null=True, blank=True)
    cpu_idle = models.IntegerField(null=True, blank=True)
    cpu_used = models.IntegerField(null=True, blank=True)
    mem_total = models.IntegerField(null=True, blank=True)
    mem_used = models.IntegerField(null=True, blank=True)
    mem_avail = models.IntegerField(null=True, blank=True)
    os_version = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)

    #__Devicestats_FIELDS__END

    class Meta:
        verbose_name        = _("Devicestats")
        verbose_name_plural = _("Devicestats")


class Networkinterface(models.Model):

    #__Networkinterface_FIELDS__
    device = models.ForeignKey(DeviceInventory, on_delete=models.CASCADE)
    interface_name = models.CharField(max_length=255, null=True, blank=True)
    opr_v4 = models.CharField(max_length=255, null=True, blank=True)
    opr_v6 = models.CharField(max_length=255, null=True, blank=True)
    mode = models.CharField(max_length=255, null=True, blank=True)
    port_sap_id = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    pfx_state = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_updated = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Networkinterface_FIELDS__END

    class Meta:
        verbose_name        = _("Networkinterface")
        verbose_name_plural = _("Networkinterface")



#__MODELS__END
