from django.conf.urls import patterns, url

from ajax import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^configJunosInterfaces/$', views.config_junos_interfaces, name='configJunosInterfaces'),
                       url(r'^preconfigJunosDomain/$', views.preconfig_junos_domain, name='preconfigJunosDomain'),
                       url(r'^preconfigFirefly/$', views.preconfig_firefly, name='preconfigFirefly'),
                       url(r'^preconfigLinuxDomain/$', views.preconfig_linux_domain, name='preconfigLinuxDomain'),
                       url(r'^getJunosConfig/$', views.get_junos_config, name='getJunosConfig'),
                       url(r'^getConfigTemplates/$', views.get_config_templates, name='getConfigTemplates'),
                       url(r'^applyConfigTemplate/$', views.apply_config_template, name='applyConfigTemplate'),
                       url(r'^getJunosStartupState/$', views.get_junos_startup_state, name='getJunosStartupState'),
                       url(r'^getLinuxStartupState/$', views.get_linux_startup_state, name='getLinuxStartupState'),
                       url(r'^syncLinkData/$', views.sync_link_data, name='syncLinkData'),
                       url(r'^refreshDeploymentStatus/$', views.refresh_deployment_status,
                           name='refreshDeploymentStatus'),
                       url(r'^refreshHypervisorStatus/$', views.refresh_hypervisor_status,
                           name='refreshHypervisorStatus'),
                       url(r'^refreshHostLoad/$', views.refresh_host_load, name='refreshHostLoad'),
                       url(r'^multiCloneTopology/$', views.multi_clone_topology, name='multiCloneTopology'),
                       url(r'^deployTopology/$', views.deploy_topology, name='deployTopology'),
                       url(r'^startTopology/$', views.start_topology, name='startTopology'),
                       url(r'^manageDomain/$', views.manage_domain, name='manageDomain'),
                       url(r'^manageNetwork/$', views.manage_network, name='manageNetwork'),
                       url(r'^manageHypervisor/$', views.manage_hypervisor, name='manage_hypervisor'),
                       url(r'^executeCli/$', views.execute_cli, name='executeCli'),
                       url(r'^executeLinuxCli/$', views.execute_linux_cli, name='executeLinuxCli'),
                       url(r'^launchWebConsole/$', views.launch_web_console, name='launchWebConsole'),
                       url(r'^pushConfigSet/$', views.push_config_set, name='pushConfigSet'),
                       url(r'^deleteConfigSet/$', views.delete_config_set, name='deleteConfigSet'),
                       url(r'^viewNetwork/(?P<network_name>[^/]+)$', views.view_network, name='viewNetwork'),
                       url(r'^viewDomain/(?P<domain_id>[^/]+)$', views.view_domain, name='viewDomain'),
                       url(r'^checkIp/$', views.check_ip, name='check_ip'),
                       )
