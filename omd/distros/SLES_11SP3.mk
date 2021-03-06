DISTRO_CODE     = sles11sp3
OS_PACKAGES     =
OS_PACKAGES    += libcap-progs # needed for setting special file permissions
OS_PACKAGES    += cron # needed for sites cron jobs
OS_PACKAGES      += net-tools # traceroute is needed for Check_MK parent scan
OS_PACKAGES    += apache2
OS_PACKAGES    += bind-utils
OS_PACKAGES    += curl
OS_PACKAGES    += dialog
OS_PACKAGES    += gd
OS_PACKAGES    += graphviz
OS_PACKAGES    += libpng12-0
OS_PACKAGES    += libevent-1_4-2
OS_PACKAGES    += libltdl7
OS_PACKAGES    += libreadline5
OS_PACKAGES    += libuuid1
OS_PACKAGES    += pango
OS_PACKAGES    += php53-fastcgi
OS_PACKAGES    += php53-gd
OS_PACKAGES    += php53-iconv
OS_PACKAGES    += php53-mbstring
OS_PACKAGES    += php53-pear
OS_PACKAGES    += php53-sockets
OS_PACKAGES    += php53-sqlite
OS_PACKAGES    += php53-openssl
OS_PACKAGES    += rsync
OS_PACKAGES    += samba-client
OS_PACKAGES    += unzip
OS_PACKAGES    += xinetd
OS_PACKAGES    += xorg-x11-fonts
OS_PACKAGES    += freeradius-client-libs
OS_PACKAGES    += binutils # Needed by Check_MK Agent Bakery
OS_PACKAGES    += libgio-2_0-0 # needed by msitools/Agent Bakery
OS_PACKAGES    += libgsf-1-114 # needed by msitools/Agent Bakery
OS_PACKAGES    += cpio # needed for Agent bakery (solaris pkgs)
OS_PACKAGES    += poppler-tools # needed for preview of PDF in reporting
OS_PACKAGES    += libpcap0 # needed for ICMP of CMC
OS_PACKAGES     += libffi43 # needed for pyOpenSSL and dependant
USERADD_OPTIONS   = -M
ADD_USER_TO_GROUP = groupmod -A %(user)s %(group)s
PACKAGE_INSTALL   = zypper -n refresh ; zypper -n install
ACTIVATE_INITSCRIPT = chkconfig --add %s
APACHE_CONF_DIR   = /etc/apache2/conf.d
APACHE_INIT_NAME  = apache2
APACHE_USER       = wwwrun
APACHE_GROUP      = www
APACHE_VERSION    = 2.2.12
APACHE_CTL        = /usr/sbin/apache2ctl
APACHE_MODULE_DIR = /usr/lib/apache2-prefork
APACHE_MODULE_DIR_64 = /usr/lib64/apache2-prefork
HTPASSWD_BIN      = /usr/bin/htpasswd2
PHP_FCGI_BIN	  = /usr/bin/php-cgi
APACHE_ENMOD      = a2enmod %s
BECOME_ROOT       = su -c
MOUNT_OPTIONS     =
INIT_CMD          = /etc/init.d/%(name)s %(action)s
